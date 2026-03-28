#!/usr/bin/env python3
"""草帽团 Agent 监控页面生成器 - 直接解析 transcript"""
import json, os, glob, datetime

TZ = datetime.timezone(datetime.timedelta(hours=8))
NOW = datetime.datetime.now(TZ)
AGENTS_DIR = os.path.expanduser("~/.openclaw/agents")
CHANNEL = "1487384180835749938"
OUTPUT = os.path.expanduser("~/Projects/kidstart-preview/agent-monitor.html")

AGENTS = [
    {"id": "nami", "emoji": "🍊", "name": "娜美", "role": "PM · 调研/Spec/设计"},
    {"id": "zoro", "emoji": "⚔️", "name": "索隆", "role": "开发 · 写代码/PR"},
    {"id": "franky", "emoji": "🔧", "name": "弗兰奇", "role": "QA · 验收/编译"},
    {"id": "main", "emoji": "🦌", "name": "乔巴", "role": "调度员 · 派活/跟进"},
]

def get_agent_status(agent_id):
    """从 sessions.json 找到对应频道的 transcript，解析最后的 assistant 消息"""
    sessions_file = os.path.join(AGENTS_DIR, agent_id, "sessions", "sessions.json")
    if not os.path.exists(sessions_file):
        return {"status": "offline", "msg": "未配置", "time": ""}
    
    sessions = json.load(open(sessions_file))
    transcript_path = None
    for key, val in sessions.items():
        if CHANNEL in key:
            transcript_path = val.get("sessionFile", "")
            break
    
    # 也检查其他频道的活动
    if not transcript_path:
        for key, val in sessions.items():
            if "discord" in key:
                transcript_path = val.get("sessionFile", "")
                break
    
    if not transcript_path or not os.path.exists(transcript_path):
        return {"status": "idle", "msg": "无活动记录", "time": ""}
    
    # 从后往前找最后一条 assistant 消息
    last_assistant_text = ""
    last_time = ""
    last_error = False
    mins_ago = 9999
    
    lines = open(transcript_path).readlines()
    for line in reversed(lines):
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
            msg = entry.get("message", entry)
            role = msg.get("role", "")
            if role not in ("assistant",):
                continue
            
            ts_str = entry.get("timestamp", "")
            if ts_str:
                try:
                    ts = datetime.datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                    last_time = ts.astimezone(TZ).strftime("%H:%M:%S")
                    mins_ago = (NOW - ts.astimezone(TZ)).total_seconds() / 60
                except:
                    pass
            
            stop = msg.get("stopReason", "")
            err = msg.get("errorMessage", "")
            if stop == "error" or err:
                last_error = True
            
            content = msg.get("content", [])
            for c in content:
                if c.get("type") == "text":
                    t = c.get("text", "").strip()
                    if t:
                        last_assistant_text = t[:120]
                        break
            
            if last_assistant_text:
                break
        except:
            continue
    
    if not last_assistant_text:
        return {"status": "idle", "msg": "暂无消息", "time": last_time}
    
    if last_error and mins_ago < 30:
        status = "stuck"
    elif mins_ago < 5:
        status = "working"
    elif mins_ago < 30:
        status = "recent"
    else:
        status = "idle"
    
    return {"status": status, "msg": last_assistant_text, "time": last_time, "mins_ago": int(mins_ago)}

STATUS_MAP = {
    "working": ("status-working", "🟢 工作中"),
    "recent": ("status-working", "🟢 最近活跃"),
    "stuck": ("status-stuck", "🔴 卡住"),
    "idle": ("status-idle", "💤 待命"),
    "offline": ("status-idle", "⚪ 离线"),
}

agents_html = ""
for a in AGENTS:
    s = get_agent_status(a["id"])
    cls, label = STATUS_MAP.get(s["status"], ("status-idle", "待命"))
    time_str = s.get("time", "")
    mins = s.get("mins_ago", "")
    time_display = f'{time_str} ({mins}分钟前)' if time_str and mins else time_str or "--:--"
    
    agents_html += f"""<div class="agent">
  <div class="agent-header">
    <span class="agent-avatar">{a['emoji']}</span>
    <div><div class="agent-name">{a['name']}</div><div class="agent-role">{a['role']}</div></div>
    <span class="status {cls}">{label}</span>
  </div>
  <div class="last-action">
    {s['msg']}
    <div class="time">{time_display}</div>
  </div>
</div>
"""

now_str = NOW.strftime("%Y-%m-%d %H:%M:%S")

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🏴‍☠️ 草帽团 Agent 监控</title>
<meta http-equiv="refresh" content="120">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0d1117;color:#e6edf3;padding:16px;max-width:600px;margin:0 auto}}
h1{{font-size:20px;margin-bottom:4px;text-align:center}}
.update-time{{text-align:center;font-size:12px;color:#7d8590;margin-bottom:16px}}
.agent{{background:#161b22;border:1px solid #30363d;border-radius:12px;padding:16px;margin-bottom:12px}}
.agent-header{{display:flex;align-items:center;gap:10px;margin-bottom:8px}}
.agent-avatar{{font-size:28px}}
.agent-name{{font-size:16px;font-weight:600}}
.agent-role{{font-size:12px;color:#7d8590}}
.status{{display:inline-block;padding:2px 8px;border-radius:12px;font-size:11px;font-weight:600;margin-left:auto}}
.status-working{{background:#1f6f2b;color:#3fb950}}
.status-idle{{background:#3d2e00;color:#d29922}}
.status-stuck{{background:#5c1a1a;color:#f85149;animation:pulse 1.5s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.5}}}}
.last-action{{font-size:13px;color:#b1bac4;margin-top:8px;padding:8px;background:#0d1117;border-radius:8px;line-height:1.5}}
.last-action .time{{color:#7d8590;font-size:11px;margin-top:4px}}
</style>
</head>
<body>
<h1>🏴‍☠️ 草帽团 Agent 监控</h1>
<div class="update-time">更新于 {now_str} · 每5分钟自动刷新</div>
{agents_html}
</body>
</html>"""

with open(OUTPUT, "w") as f:
    f.write(html)

# git push
os.system(f"cd {os.path.dirname(OUTPUT)} && git add agent-monitor.html && git commit -m 'monitor: update' --allow-empty && git push 2>/dev/null")
print("✅ Monitor updated")
