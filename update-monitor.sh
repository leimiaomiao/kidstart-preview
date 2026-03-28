#!/bin/bash
# 草帽团 Agent 监控页面生成器
# 用法: bash update-monitor.sh

cd "$(dirname "$0")"

AGENTS_HTML=""

# 函数：查询 agent 最近状态
get_agent_html() {
  local emoji="$1" name="$2" role="$3" session_key="$4"
  
  # 用 openclaw 的 session transcript 获取最新状态
  local transcript=""
  local status="idle"
  local status_class="status-idle"
  local status_text="待命"
  local last_action="暂无活动"
  local task=""
  local last_time=""

  # 检查 session 文件
  local agent_id=$(echo "$session_key" | cut -d: -f2)
  local sessions_dir="$HOME/.openclaw/agents/$agent_id/sessions"
  
  if [ -d "$sessions_dir" ]; then
    # 获取最新的 session 文件
    local latest=$(ls -t "$sessions_dir"/*.jsonl 2>/dev/null | head -1)
    if [ -n "$latest" ]; then
      # 获取最后一条 assistant 消息
      local last_msg=$(grep '"role":"assistant"' "$latest" 2>/dev/null | tail -1)
      if [ -n "$last_msg" ]; then
        # 提取时间戳
        last_time=$(echo "$last_msg" | python3 -c "
import sys,json
try:
  d=json.loads(sys.stdin.read())
  ts=d.get('timestamp',0)
  if ts:
    import datetime
    dt=datetime.datetime.fromtimestamp(ts/1000,tz=datetime.timezone(datetime.timedelta(hours=8)))
    print(dt.strftime('%H:%M:%S'))
except: pass
" 2>/dev/null)
        
        # 提取最后的文本消息
        last_action=$(echo "$last_msg" | python3 -c "
import sys,json
try:
  d=json.loads(sys.stdin.read())
  for c in d.get('content',[]):
    if c.get('type')=='text' and c.get('text','').strip():
      t=c['text'].strip()
      if len(t)>100: t=t[:100]+'...'
      print(t)
      break
except: pass
" 2>/dev/null)
        
        # 检查是否有错误
        local has_error=$(echo "$last_msg" | python3 -c "
import sys,json
try:
  d=json.loads(sys.stdin.read())
  sr=d.get('stopReason','')
  em=d.get('errorMessage','')
  if sr=='error' or em: print('yes')
  else: print('no')
except: print('no')
" 2>/dev/null)

        # 检查时间差（分钟）
        local mins_ago=$(echo "$last_msg" | python3 -c "
import sys,json,time
try:
  d=json.loads(sys.stdin.read())
  ts=d.get('timestamp',0)
  if ts: print(int((time.time()*1000-ts)/60000))
  else: print(999)
except: print(999)
" 2>/dev/null)
        
        if [ "$has_error" = "yes" ]; then
          status="error"; status_class="status-stuck"; status_text="⚠️ 卡住"
        elif [ -n "$mins_ago" ] && [ "$mins_ago" -lt 5 ]; then
          status="working"; status_class="status-working"; status_text="工作中"
        elif [ -n "$mins_ago" ] && [ "$mins_ago" -lt 30 ]; then
          status="idle"; status_class="status-idle"; status_text="待命"
        else
          status="idle"; status_class="status-idle"; status_text="待命"
        fi
      fi
    fi
  fi

  [ -z "$last_action" ] && last_action="暂无活动"
  [ -z "$last_time" ] && last_time="--:--"

  cat <<EOF
<div class="agent">
  <div class="agent-header">
    <span class="agent-avatar">$emoji</span>
    <div><div class="agent-name">$name</div><div class="agent-role">$role</div></div>
    <span class="status $status_class">$status_text</span>
  </div>
  <div class="last-action">
    $last_action
    <div class="time">$last_time</div>
  </div>
</div>
EOF
}

# 生成每个 agent 的状态
NAMI=$(get_agent_html "🍊" "娜美" "PM · 调研/Spec/设计" "agent:nami")
ZORO=$(get_agent_html "⚔️" "索隆" "开发 · 写代码/PR" "agent:zoro")
FRANKY=$(get_agent_html "🔧" "弗兰奇" "QA · 验收/编译" "agent:franky")
CHOPPER=$(get_agent_html "🦌" "乔巴" "调度员 · 派活/跟进" "agent:main")

AGENTS_HTML="$NAMI$ZORO$FRANKY$CHOPPER"

# 读取模板并替换
TEMPLATE=$(cat agent-monitor.html)
# 用 python 替换
python3 -c "
import sys
tpl = open('agent-monitor.html').read()
agents = sys.stdin.read()
result = tpl.replace('<!--AGENTS-->', agents)
# 更新时间
import datetime
tz = datetime.timezone(datetime.timedelta(hours=8))
now = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
result = result.replace('加载中...', f'更新于 {now} (每2分钟由乔巴更新)')
open('agent-monitor.html','w').write(result)
" <<< "$AGENTS_HTML"

# push
git add agent-monitor.html
git commit -m "monitor: update agent status" --allow-empty 2>/dev/null
git push 2>/dev/null

echo "✅ Monitor updated"
