![updated](https://img.shields.io/badge/updated-2026--10--19-blue) ![offers](https://img.shields.io/badge/offers-21-brightgreen) ![verified](https://img.shields.io/badge/verified-against%20official%20pages-success) ![scored](https://img.shields.io/badge/every%20row-scored%200--100-blueviolet)

# Tokenation

Tokenation collects free LLM API offers and checks every entry against the provider's own pages. Offers are split into two kinds:

**Evergreen free tiers**: standing free quotas with no announced end date, plus new-account trial allowances. \
Each row records the provider, the model ID, a one-line overview, the free quota, the deadline and the score.

**Limited-time offers**: announced by the provider as free for a limited time, either with a fixed end date \
or with no published deadline (the entry says so). Offers whose announced deadline has already passed are removed.

## Top 15 by Tokenation score

The 15 best deals on the site right now, ranked by the Tokenation score.

| Provider | Type | Model ID | Overview | Free quota | Free until | Score | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **WorkBuddy Intl (Tencent)** | Limited-time | `deepseek-v4.1-flash-1017` | October 2026 snapshot of DeepSeek V4.1 Flash. | DeepSeek V4.1 Flash etc., no credit burn | 2026-10-31 (over 7 days left) | **90.07** | [→](https://www.workbuddy.ai/) |
| **OpenCode Zen** | Limited-time | `deepseek-v4.1-flash-free` | Sparse MoE model from DeepSeek, first on its CED architecture. | 14 free models at $0, in-app only | No deadline announced | **90.07** | [→](https://opencode.ai/docs/zen/) |
| **WorkBuddy Intl (Tencent)** | Limited-time | `step-5-preview` | StepFun flagship for agentic work, sparse MoE with 27B active. | DeepSeek V4.1 Flash etc., no credit burn | 2026-10-31 (over 7 days left) | **89.13** | [→](https://www.workbuddy.ai/) |
| **OpenCode Go** | Limited-time | `minimax-m3.1-flash-free` | Multimodal model from MiniMax. | LongCat, Beam, MiniMax free | No deadline announced | **88.27** | [→](https://opencode.ai/docs/go/) |
| **OpenCode Zen** | Limited-time | `minimax-m3.1-flash-free` | Multimodal model from MiniMax. | 14 free models at $0, in-app only | No deadline announced | **88.27** | [→](https://opencode.ai/docs/zen/) |
| **OpenCode Zen** | Limited-time | `glm-5.3-flash-free` | Native multimodal model from Z.ai. | 14 free models at $0, in-app only | No deadline announced | **87.87** | [→](https://opencode.ai/docs/zen/) |
| **Qoder** | Limited-time | `Qwen3.8-Flash` | Multimodal reasoning model from Alibaba Qwen. | Qwen3.8-Flash free, 100 Credits daily | No deadline announced | **86.53** | [→](https://docs.qoder.com/zh/events/flashoffer) |
| **GroqCloud** | Evergreen | `qwen/qwen3.8-27b` | Open-weight dense vision-language model from Qwen. | 30 RPM, 1,000 RPD, 200K TPD | Ongoing | **82.47** | [→](https://console.groq.com/keys) |
| **OpenCode Go** | Limited-time | `beam-free` | Beam 1.0, Reflection's open-weight reasoning model for coding agents. | LongCat, Beam, MiniMax free | No deadline announced | **80.20** | [→](https://opencode.ai/docs/go/) |
| **Vercel AI Gateway** | Limited-time | `reflection/beam-free` | Beam 1.0, Reflection's open-weight reasoning model for coding agents. | 6 free models at $0, plus discounts | No deadline announced | **80.20** | [→](https://vercel.com/ai-gateway) |
| **Novita AI** | Evergreen | `apodex-1.1-mini` | Listed by Novita without a published model card. | Some models free, rest billed per token | Ongoing | **77.60** | [→](https://novita.ai/pricing) |
| **Google Gemini API** | Evergreen | `gemini-3.8-flash` | Google's strongest Flash model for coding, agents and multi-step reasoning. | Free tier capped by RPM/RPD/TPM | Ongoing | **75.25** | [→](https://aistudio.google.com/apikey) |
| **OpenCode Go** | Limited-time | `longcat-2.5-preview-free` | Meituan LongCat 2.5 preview. No card published for this version. | LongCat, Beam, MiniMax free | No deadline announced | **72.73** | [→](https://opencode.ai/docs/go/) |
| **Vercel AI Gateway** | Limited-time | `nvidia/nemotron-3.5-lightning-free` | NVIDIA open MoE with 3B active of 30B parameters. | 6 free models at $0, plus discounts | No deadline announced | **68.60** | [→](https://vercel.com/ai-gateway) |
| **GroqCloud** | Evergreen | `openai/gpt-oss-120b` | OpenAI open-weight 117B MoE for reasoning and agentic work. | 30 RPM, 1,000 RPD, 200K TPD | Ongoing | **67.73** | [→](https://console.groq.com/keys) |

Top 15 of 62 scored model rows. Scoring rule below. Full lists below.

## How the score works

Every offer here carries one number from 0 to 100, so an offer you have never touched can be compared against one you already pay for. Free API tiers change every week, and signing up to test each one costs a weekend, so the score compresses that decision into a single number. It measures how much usable inference you get for free right now. It is not a ranking of model quality.

- Intelligence, 40%: the model's Artificial Analysis index.
- Free quota, 60%: how much you can actually run before you hit a wall.
- Every score traces back to the provider's own page, rechecked daily.

- [Chinese: Evergreen free tiers](cn/EVERGREEN.md)
- [Chinese: Limited-time offers](cn/LIMIT-TIME.md)
- [English: Evergreen free tiers](en/EVERGREEN.md)
- [English: Limited-time offers](en/LIMIT-TIME.md)

---

# Tokenation（中文）

Tokenation 每日搜集免费 LLM API，并逐条回到厂商官方页面核实。条目分两类：

**常态免费（Evergreen）**，官方定价页长期挂着、无公告结束时间的免费额度，含新用户免费额度。\
每行记录平台、模型 ID、一段简介、免费额度、截止日与推荐指数。

**限时免费（Limit-time）**，官方明示的限时免费 offer，含两类：写明固定截止日的，以及只写「限时」\
未公布截止日的（会在日期字段注明）。已过公布截止日的条目一律移除。

## 推荐指数榜 · Top 15

本站此刻最值的 15 单，按推荐指数从高到低。

| 平台 | 类型 | 模型 ID | 介绍 | 免费额度 | 截止 | 推荐指数 | 链接 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **WorkBuddy 国际版（腾讯）** | 限时 | `deepseek-v4.1-flash-1017` | DeepSeek V4.1 Flash 的 10 月快照版本 | DeepSeek V4.1 Flash 等限免，调用不扣积分 | 2026-10-31（剩余超7天） | **90.07** | [→](https://www.workbuddy.ai/) |
| **OpenCode Zen** | 限时 | `deepseek-v4.1-flash-free` | DeepSeek 稀疏 MoE 模型，首个采用 CED 架构 | 14 个 free 模型 $0，仅限应用内调用 | 未公布截止日 | **90.07** | [→](https://opencode.ai/docs/zen/) |
| **WorkBuddy 国际版（腾讯）** | 限时 | `step-5-preview` | 阶跃旗舰，稀疏 MoE 激活 27B，面向 Agent | DeepSeek V4.1 Flash 等限免，调用不扣积分 | 2026-10-31（剩余超7天） | **89.13** | [→](https://www.workbuddy.ai/) |
| **OpenCode Go** | 限时 | `minimax-m3.1-flash-free` | MiniMax 多模态模型 | LongCat/Beam/MiniMax 三款限免 | 未公布截止日 | **88.27** | [→](https://opencode.ai/docs/go/) |
| **OpenCode Zen** | 限时 | `minimax-m3.1-flash-free` | MiniMax 多模态模型 | 14 个 free 模型 $0，仅限应用内调用 | 未公布截止日 | **88.27** | [→](https://opencode.ai/docs/zen/) |
| **OpenCode Zen** | 限时 | `glm-5.3-flash-free` | 智谱原生多模态模型 | 14 个 free 模型 $0，仅限应用内调用 | 未公布截止日 | **87.87** | [→](https://opencode.ai/docs/zen/) |
| **Qoder** | 限时 | `Qwen3.8-Flash` | 阿里通义多模态推理模型 | Qwen3.8-Flash 限免，每日领 100 Credits | 未公布截止日 | **86.53** | [→](https://docs.qoder.com/zh/events/flashoffer) |
| **GroqCloud** | 常态 | `qwen/qwen3.8-27b` | 通义开源 27B 稠密视觉语言模型 | 30 RPM、1,000 RPD、200K TPD | 长期有效 | **82.47** | [→](https://console.groq.com/keys) |
| **OpenCode Go** | 限时 | `beam-free` | Reflection 开源推理模型 Beam 1.0 | LongCat/Beam/MiniMax 三款限免 | 未公布截止日 | **80.20** | [→](https://opencode.ai/docs/go/) |
| **Vercel AI Gateway** | 限时 | `reflection/beam-free` | Reflection 开源推理模型 Beam 1.0 | 6 个免费模型（$0），另有折扣促销 | 未公布截止日 | **80.20** | [→](https://vercel.com/ai-gateway) |
| **Novita AI** | 常态 | `apodex-1.1-mini` | Novita 上架，但未公布模型说明 | 部分模型免费，其余按 Token 计 | 长期有效 | **77.60** | [→](https://novita.ai/pricing) |
| **Google Gemini API** | 常态 | `gemini-3.8-flash` | 谷歌最强 Flash，擅长编码、Agent 与多步推理 | 免费层按 RPM/RPD/TPM 限额 | 长期有效 | **75.25** | [→](https://aistudio.google.com/apikey) |
| **OpenCode Go** | 限时 | `longcat-2.5-preview-free` | 美团 LongCat 2.5 预览版，未公布该版本说明 | LongCat/Beam/MiniMax 三款限免 | 未公布截止日 | **72.73** | [→](https://opencode.ai/docs/go/) |
| **Vercel AI Gateway** | 限时 | `nvidia/nemotron-3.5-lightning-free` | 英伟达开源 MoE，激活 3B、总参 30B | 6 个免费模型（$0），另有折扣促销 | 未公布截止日 | **68.60** | [→](https://vercel.com/ai-gateway) |
| **GroqCloud** | 常态 | `openai/gpt-oss-120b` | OpenAI 开源 117B MoE，面向推理与 Agent | 30 RPM、1,000 RPD、200K TPD | 长期有效 | **67.73** | [→](https://console.groq.com/keys) |

上表从 62 行已评分条目中取前 15 行，评分口径见下节。完整清单见下方四个列表。

## 评分怎么看

本站每个条目都带一个 0 到 100 的分数，让你能拿一个没试过的免费额度，和一个已经在用的放在一起比。免费额度每周都在变，逐个注册去试要花掉一个周末，这个分数把这件事压缩成一个数字。它量的是此刻免费能拿到多少可用推理，不是模型强弱排名。

- 智能占 40%：取模型在 Artificial Analysis 智能指数上的位置。
- 免费额度占 60%：真跑起来撞墙之前能用多少。
- 每个分数都能追回厂商自己的页面，每天重新核实一次。

- [中文：常态免费](cn/EVERGREEN.md)
- [中文：限时免费](cn/LIMIT-TIME.md)
- [英文：常态免费](en/EVERGREEN.md)
- [英文：限时免费](en/LIMIT-TIME.md)
