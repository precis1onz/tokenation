# Tokenation

这个仓库收集仍然有效的免费 LLM API，并逐条核对官方页面。每条记录包含免费额度、限流数字、当前免费的模型 ID 和注册链接。

两份清单由同一份数据生成：

- [cn/ALL.md](cn/ALL.md) 中文版
- [en/ALL.md](en/ALL.md) 英文版

## 核对范围

每条记录都由 AI 助手核对服务商自己的定价页、限流页和模型页。博客与搜索摘要不作为依据。每条记录包含以下内容：

- 活动类型：常态免费、限时活动，或新用户额度。
- 有效期：截止日期，或明确标注长期有效。
- 频控限制：沿用服务商的单位，例如 RPM、RPD、TPM 或每月 Credits。
- 最多三个当天确实免费的模型 ID，写法与 API 一致。
- 官方注册页面。

服务商没有公布的限额会保留为未公布，不用估算的数字填空。

## 清单何时更新

定时任务用一份数据重新生成中英两份清单，并在同一次提交中发布。两份清单的条数与顺序始终一致，不会出现一份已更新、另一份过期的情况。带截止日期的活动，剩余时间必须超过七天才会保留。

## 条目结构

```text
1. **服务商名称**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：30 RPM、1,000 RPD

🤖 **推荐免费模型**（1~3个）：
• 模型1：openai/gpt-oss-120b（通用推理）

🔗 **获取/注册链接**：[Groq API Keys](https://console.groq.com/keys)
```

中英两份清单的字段顺序相同。模型 ID、服务商名称、链接和数字不做翻译。

## 收录范围

通用 API Key 与产品内额度分开记录。编程工具里的 Credits 不等于通用 API Key。每条记录会说明属于哪一种。没有官方截止日期的免费服务可以收录。带截止日期的活动，剩余时间超过七天才会收录。

---

（更新至 2026-10-19）

🎁 **最新有效免费 LLM API & 羊毛活动 TOP 50**（2026.10.19）

---

1. **Cloudflare Workers AI**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：Workers Free 方案每天 10,000 Neurons，UTC 00:00 重置，用尽后需升级 Workers Paid。

🤖 **推荐免费模型**（1~3个）：
• 模型1：@cf/google/gemma-4-26b-a4b-it（多模态与推理）

🔗 **获取/注册链接**：[Cloudflare Workers AI](https://dash.cloudflare.com/)

---

2. **GitHub Copilot Free**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：Free 方案每月 2,000 次代码补全，模型只能自动选择；仅限无组织授权的个人开发者。

🤖 **推荐免费模型**（1~3个）：
• 模型1：Auto (automatic model selection)（Free 方案仅支持自动选模型）

🔗 **获取/注册链接**：[Copilot plans](https://github.com/copilot)

---

3. **GroqCloud**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：免费方案下 gpt-oss-120b 与 qwen3.8-27b 均为 30 RPM、1,000 RPD、8K TPM、200K TPD。

🤖 **推荐免费模型**（1~3个）：
• 模型1：openai/gpt-oss-120b（30 RPM、1,000 RPD）
• 模型2：qwen/qwen3.8-27b（30 RPM、1,000 RPD）

🔗 **获取/注册链接**：[Groq API Keys](https://console.groq.com/keys)

---

4. **SiliconFlow（硅基流动）**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：免费模型限流固定，不随充值档位变化；语言模型整体 RPM 范围 1000-10000、TPM 50000-5000000。

🤖 **推荐免费模型**（1~3个）：
• 模型1：Qwen/Qwen2-7B-Instruct（免费模型）

🔗 **获取/注册链接**：[SiliconFlow console](https://cloud.siliconflow.com/)

---

5. **Zhipu AI（智谱）**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：Flash 系列模型官方标注免费，上下文 128K-200K，具体并发与 RPM 见各模型文档。

🤖 **推荐免费模型**（1~3个）：
• 模型1：glm-4.7-flash（免费文本模型，200K 上下文）
• 模型2：glm-4.6v-flash（免费视觉推理）

🔗 **获取/注册链接**：[BigModel console](https://open.bigmodel.cn/)

---

6. **Gemini CLI**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：用个人 Google 账号登录可免费使用，额度按请求数计时，官方未公布与 API Key 等价的 RPM 数值。

🤖 **推荐免费模型**（1~3个）：
• 模型1：gemini-4-flash（CLI 内免费额度）

🔗 **获取/注册链接**：[Gemini CLI](https://github.com/google-gemini/gemini-cli)

---

7. **Mistral AI Studio**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：Free 方案可使用 Studio 与限定的聊天、搜索、生图额度，官方未公布统一 RPM/RPD。

🤖 **推荐免费模型**（1~3个）：
• 模型1：mistral-small-latest（通用对话）

🔗 **获取/注册链接**：[Mistral Studio](https://console.mistral.ai/)

---

8. **OpenCode Zen**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：Zen 目录内 15 个免费模型（模型 ID 带 -free 或 Free 标记）限时免费，官方未公布 RPM/RPD。

🤖 **推荐免费模型**（1~3个）：
• 模型1：deepseek-v4.1-flash-free（限时免费模型）
• 模型2：glm-5.3-flash-free（限时免费模型）

🔗 **获取/注册链接**：[OpenCode Zen](https://opencode.ai/docs/zen/)

---

9. **Cohere Trial API**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：Trial key 调用免费但有限流，不可用于生产或商业用途；到期后需切换 Production key 按量计费。

🤖 **推荐免费模型**（1~3个）：
• 模型1：command-a-03-2025（通用生成）

🔗 **获取/注册链接**：[Cohere API Keys](https://dashboard.cohere.com/api-keys)

---

10. **Novita AI**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：定价页对部分模型标注免费，其余按 Tokens 计费，免费模型限流以模型详情页为准。

🤖 **推荐免费模型**（1~3个）：
• 模型1：apodex-1.1-mini（定价页标为 Free）

🔗 **获取/注册链接**：[Novita AI](https://novita.ai/pricing)

---

11. **OpenRouter**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：带 :free 后缀的模型受平台每分钟与每天免费请求上限约束，具体数值随账号累计充值额变化。

🤖 **推荐免费模型**（1~3个）：
• 模型1：nvidia/nemotron-3.5-super-vl:free（多模态与长上下文）
• 模型2：xingchen-agi/xing4.0-29b-a4b:free（中文与工具调用）

🔗 **获取/注册链接**：[OpenRouter sign-up](https://openrouter.ai/sign-up)

---

12. **WorkBuddy（腾讯）**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：Free 方案每月 100 Credits，新用户注册再送 250 Credits（14 天有效），Free 用户只能用 Auto 调度。

🤖 **推荐免费模型**（1~3个）：
• 模型1：Auto (automatic model routing)（Auto 模型调度，不提供单一模型 ID）

🔗 **获取/注册链接**：[WorkBuddy subscription](https://www.workbuddy.ai/docs/workbuddy/Subscription)

---

13. **Cerebras Inference**

🏷️ **活动/类型**：新用户免费额度

⏰ **免费有效日期**：30天（自开通或发放起算，剩余时间因账号而异）

⚡ **频控限制**：新账号添加已验证付款方式后获赠 5 美元额度，30 天过期，官方明确没有永久免费层。

🤖 **推荐免费模型**（1~3个）：
• 模型1：full public model catalog（公开目录全部模型，按模型单独限流）

🔗 **获取/注册链接**：[Cerebras Cloud](https://cloud.cerebras.ai/)

---

14. **Google Gemini API**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：免费层按 RPM、RPD、TPM 限额，数值见 AI Studio Rate Limit 页面，按项目计算，RPD 于太平洋时间午夜重置。

🤖 **推荐免费模型**（1~3个）：
• 模型1：gemini-3.5-flash-lite（免费层输入输出）
• 模型2：gemini-3.8-flash（免费层可用）

🔗 **获取/注册链接**：[AI Studio API Key](https://aistudio.google.com/apikey)

---

15. **Together AI**

🏷️ **活动/类型**：常态免费Tier

⏰ **免费有效日期**：长期有效

⚡ **频控限制**：定价页对部分开源模型标注 Free，其余按 Token 计费，免费模型的限流按模型页显示。

🤖 **推荐免费模型**（1~3个）：
• 模型1：tev1-4b-experimental（定价页标为 Free）

🔗 **获取/注册链接**：[Together AI](https://www.together.ai/pricing)

---

