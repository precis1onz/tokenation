![updated](https://img.shields.io/badge/updated-2026--11--22-blue) ![offers](https://img.shields.io/badge/offers-12-brightgreen) ![verified](https://img.shields.io/badge/verified-against%20official%20pages-success) ![scored](https://img.shields.io/badge/every%20row-scored%200--100-blueviolet)

# Tokenation<a id="top"></a>

Tokenation collects free LLM API offers and checks every entry against the provider's own pages. Offers are split into two kinds:

**Evergreen free tiers**: standing free quotas with no announced end date, plus new-account trial allowances. \
Each row records the provider, the model ID, a one-line overview, the free quota, the deadline and the score.

**Limited-time offers**: announced by the provider as free for a limited time, either with a fixed end date \
or with no published deadline (the entry says so). Offers whose announced deadline has already passed are removed.

## Top 11 by Tokenation score<a id="top15"></a>

The 11 best deals on the site right now, ranked by the Tokenation score.

| Provider | Type | Model ID | Overview | Free quota | AA | Free until | Score | Link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Google Gemini API** | Evergreen | `gemini-4-hydrogen` | Google's Gemini 4 flagship with a 1M-token context | Gemini 4 Hydrogen and 3.8 Flash… | 53.9 | Ongoing | **95.95** | [→](https://aistudio.google.com/apikey) |
| **AMD Radeon Cloud** | Evergreen | `deepseek-v4.1-flash` | October 2026 snapshot of DeepSeek V4.1 Flash | 12 free models, daily cap unpublished | 32.6 | Ongoing | **81.73** | [→](https://developer.amd.com.cn/radeon/tokenfactory) |
| **OpenCode Zen** | Limited-time | `deepseek-v4.1-flash-free` | DeepSeek V4.1 Flash free for a limited time | 12 limited-time free models; OpenCode… | 32.6 | No deadline announced | **81.73** | [→](https://opencode.ai/docs/zen/) |
| **OpenCode Go** | Limited-time | `beam-free` | Beam open-weight model, 501B total | 4 limited-time free models; outside the… | 30.3 | No deadline announced | **80.20** | [→](https://opencode.ai/docs/go/) |
| **Vercel AI Gateway** | Limited-time | `reflection/beam-free` | Beam open-weight model with ~501B total parameters | 4 tracked models at $0 in/out (27 promo… | 30.3 | No deadline announced | **80.20** | [→](https://vercel.com/ai-gateway) |
| **Google Gemini API** | Evergreen | `gemini-3.8-flash` | Google's strongest Flash model for coding, agents and multi-step reasoning. | Gemini 4 Hydrogen and 3.8 Flash… | 30.8 | Ongoing | **68.55** | [→](https://aistudio.google.com/apikey) |
| **AutoClaw (Z.ai / Zhipu)** | Limited-time | `glm-5.3` | Z.ai reasoning model for software engineering and long-horizon agent tasks. | 50M intl / 100M CN tokens; Nov 29 | 31.7 | 2026-11-29 (in 7 days) | **57.15** | [→](https://autoclaw.z.ai/) |
| **OpenRouter** | Evergreen | `thinkingmachines/inkling-2-small:free` | Multimodal MoE reasoning model from Thinking Machines. | :free models $0, 20 RPM, 50 RPD | 30.6 | Ongoing | **54.57** | [→](https://openrouter.ai/collections/free-models) |
| **AiHubMix** | Evergreen | `xiaomi-mimo-v2.6-pro-free` | Xiaomi MiMo V2.6 Pro flagship | 76 models at $0; 100 req/day, 1M tokens… | 46.3 | Ongoing | **53.47** | [→](https://aihubmix.com/models/free) |
| **AiHubMix** | Evergreen | `qwen3.8-max-free` | Qwen3.8 Max flagship | 76 models at $0; 100 req/day, 1M tokens… | 45.4 | Ongoing | **52.87** | [→](https://aihubmix.com/models/free) |
| **AiHubMix** | Evergreen | `coding-glm-5.3-free` | GLM 5.3 coding variant | 76 models at $0; 100 req/day, 1M tokens… | 44.8 | Ongoing | **52.47** | [→](https://aihubmix.com/models/free) |

Top 11 of 91 scored model rows. Scoring rule below. Full lists below.

## How the score works<a id="score"></a>

Every offer here carries one number from 0 to 100, so an offer you have never touched can be compared against one you already pay for. Free API tiers change every week, and signing up to test each one costs a weekend, so the score compresses that decision into a single number. It measures how much usable inference you get for free right now. It is not a ranking of model quality.

- Intelligence, 40%: the model's Artificial Analysis index.
- Free quota, 60%: how much you can actually run before you hit a wall.
- Every score traces back to the provider's own page, rechecked daily.
- Out of scope, so never scored: decision models that return typed answers instead of text, routing endpoints (an "auto" model selection), and models under 20B total parameters.

- [Evergreen free tiers](EVERGREEN.md)
- [Limited-time offers](LIMIT-TIME.md)

[↑ Back to top](#top)
