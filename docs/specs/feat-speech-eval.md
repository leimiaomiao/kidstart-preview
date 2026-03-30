# feat-speech-eval: 跟读发音评测

## 背景
当前跟读录音完成后直接播「读得真棒！」，没有实际评测发音是否正确。需要接入语音评测，给小朋友真实反馈。

## 方案
接入微信「智聆口语评测」小程序插件（已审核通过）。

## 插件信息
- 插件名：智聆口语评测
- AppID：`wx069ba97219f66d99`
- 文档：https://developers.weixin.qq.com/community/develop/doc/00086a6feec91060f189ac2d55b00c

## 改动清单

### 1. app.json 添加插件
```json
"plugins": {
  "WeSpeechPlugin": {
    "version": "latest",
    "provider": "wx069ba97219f66d99"
  }
}
```

### 2. pages/word-card/word-card.js 改造录音逻辑

**现状**（第 93-110 行）：
- `onRecordStart`: 开始录音
- `rm.onStop`: 录音结束 → 直接 `playGuide('读得真棒！')`
- 没有任何评测

**改为**：
- `rm.onStop` 回调里拿到录音文件路径
- 调用智聆插件评测，传入当前单词 + 录音文件
- 根据评分给不同反馈

**伪代码**：
```js
const plugin = requirePlugin('WeSpeechPlugin');

// rm.onStop 回调改为：
rm.onStop((res) => {
  this.setData({ isRecording: false });
  const filePath = res.tempFilePath;
  const word = this.data.word.word;
  const retryCount = this.data.speechRetryCount || 0;

  // 调用智聆评测
  plugin.textEvaluate({
    content: word,
    mode: 'word',
    audioData: filePath,
    success: (evalRes) => {
      const score = evalRes.pronunciationScore;
      if (score >= 80) {
        playGuide('读得真棒！');
        // 正常进入下一步
      } else if (retryCount >= 2) {
        // 已重试2次，不再卡住
        playGuide('读得真棒！');
      } else if (score >= 60) {
        this.setData({ speechRetryCount: retryCount + 1 });
        playGuide('不错哦，再试一次');
        // 留在当前步骤，可重试或跳过
      } else {
        this.setData({ speechRetryCount: retryCount + 1 });
        playGuide('跟我再读一遍');
        playWord(word);
        // 留在当前步骤，可重试或跳过
      }
    },
    fail: () => {
      // 评测失败 fallback，不卡住
      playGuide('读得真棒！');
    }
  });
});
```

### 3. 新增 data 字段
```js
data: {
  speechRetryCount: 0,  // 当前词的重试次数
}
```
每进入新词时重置为 0。

### 4. UI 变化
Step 3 跟读步骤新增「跳过」按钮：
- 位置：录音按钮下方
- 文案：「跳过 →」
- 点击后直接进入 Step 4，不卡住
- 样式：小字灰色，不抢眼

### 5. 新增引导语音频（3条）
需要在 CDN 补充：
- `guide/not-bad-try-again.mp3` — "不错哦，再试一次"
- `guide/follow-me-again.mp3` — "跟我再读一遍"

或复用现有引导语，在 audio.js 的 TEXT_TO_KEY 里映射。

## 反馈规则（铁律）

| 得分 | 反馈 | 行为 |
|------|------|------|
| ≥80 | 读得真棒！ | 进下一步 |
| 60-79 | 不错哦，再试一次 | 可重试/跳过 |
| <60 | 跟我再读一遍 + 重播单词 | 可重试/跳过 |
| 评测失败 | 读得真棒！ | 直接过 |
| 重试≥2次 | 读得真棒！ | 强制过 |

**绝对不能说"读错了"** — 6岁孩子需要正向鼓励
**最多重试2次** — 不能卡住导致挫败感

## 验收标准
1. [ ] 录音后有真实评测打分
2. [ ] ≥80分直接过，<80分可重试
3. [ ] 最多重试2次后自动通过
4. [ ] 评测失败/超时 fallback 不卡住
5. [ ] 有「跳过」按钮
6. [ ] 反馈语音正确播放
