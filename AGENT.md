# Tokenation Agent 工作规范

## 目标

每日搜集仍有效的免费 LLM API、额度和 AI 工具活动，核实后在公开仓库 `precisionz/tokenation` 发布五份 Markdown 清单（1 个双语导航 + 中英各 2 份）。仓库只发布羊毛汇总 Markdown，外加一个静态 `LICENSE`（CC BY 4.0，2026-10-19 Joe 授权加入）。本文是本地工作规范，严禁推送到 GitHub。

## 发布范围

每日流程允许更新、提交和推送的文件只有五个 Markdown（`LICENSE` 是静态文件，不参与每日更新，只有变更许可证时才动它）：

- `README.md`（双语导航页，GitHub 首页渲染；介绍两类 offer、接着一张「推荐指数最高的 15 个模型」表、表下一节「评分怎么看 / How the score works」讲清推荐指数怎么来怎么读，最后索引到 4 个文件）
- `cn/EVERGREEN.md`（中文常态免费清单）
- `cn/LIMIT-TIME.md`（中文限时免费清单）
- `en/EVERGREEN.md`（英文常态免费清单）
- `en/LIMIT-TIME.md`（英文限时免费清单）

（2026-10-19 由 `cn/ALL.md` / `en/ALL.md` 改名而来，原名不再使用。）

严禁发布或提交本规范、prompt、搜索记录、来源摘录、候选清单、脚本、测试、日志、凭证、结构化数据或逐日历史文件。GitHub 上只能存在上述五个 Markdown 文件与一个 `LICENSE`（CC BY 4.0）。发现其他远端文件时，先核实用途，仅按 Joe 明确授权清理。

只暂存这五个文件，逐条写路径，不得使用 `git add -A`。`LICENSE` 的加入已在 2026-10-19 由 Joe 明确授权，属**已授权的最终状态**；逐日发布流程不得再新增任何文件。

## 严格禁止在远程添加的文件（一次泄漏就会留下永久提交记录）

以下文件在 `prompt.README` 事故中曾被推送到远程：plan / todo / skill / 检索报告 / 中间产物 / 结构化数据 JSON / 脚本 / prompt 全文。**它们在本地也不应生成**。所有候选、结构化数据、抓取页面一律放在仓库外的 `/tmp/tok/` 下，仓库工作区只允许出现被跟踪的五个 Markdown 文件与静态 `LICENSE`。`AGENT.md`、`PLAN_*.md`、`tooling/`、`scripts/`、`tests/`、`*.db` 由本地（未跟踪的）`.gitignore` 忽略，不进远程。

## offer 分类：常态免费（evergreen）vs 限时活动（limit-time）

全部 offer 按「有没有公告的截止时间」和「截止时间的口径是否因人而异」分成三类，这是收录与渲染判定的唯一依据：

- **常态免费（evergreen）**：官方定价页长期挂着的免费额度/Tier，没有公告的结束时间。`kind: free_tier`，`is_forever: true`，不填 `expires_on`。日期字段渲染为「长期有效」。
- **限时活动（limit-time）**：官方明示为限时免费即可入选，分两型——
  1. **日期型**：官方公告了固定日历截止日，且对所有人相同。用 `expires_on` 写该日期。
  2. **措辞型**：官方只写「for a limited time / 限时免费 / available for a limited time」，**未公布截止日**。`expires_on` 留空，渲染为「未公布截止日 / No deadline announced」。
  - **措辞型扩义（2026-10-19 Joe 定）**：官方没写"限时"字样、但明示**可随时结束**的（"实验期免费 / while the API is experimental / subject to change or withdrawal"）也归措辞型 → LIMIT-TIME。它不属于一次性额度（额度按周期可用），只是没有公告截止时间。正文必须写明"实验期，随时可能结束"，**不得写成"长期有效"**。首个案例：Hetzner Inference API。
  两型都用 `kind: promotion`，**禁止同时填 `window_days`**（因账号而异的才叫 trial）。
- **一次性试用额度（trial）：不收（2026-10-19 Joe 定案，R1）**。指注册送 $N / N 次调用，**用完为止、不按周期重置、也没有对所有用户统一的活动截止日**。既不是长期可用的免费 tier，也不是有时效性的羊毛——日期字段对它无话可说（写"长期有效"是假话，写截止日是编的）。
  - **`kind: trial` 自此退役**，`offers.json` 不再产生该类型；DB 里历史 `trial` 行保留审计价值但渲染器不再输出（Cerebras $5/30 天即此类，2026-10-19 下架）。
  - 判定只看**额度形态**，不看厂商大小：官方写明"one-time credit / 有效期 N 天 / 需绑定付款方式"的一律不收。
  - 例外说明：**周期性重置**（每日/每周/每月）不是一次性，仍属常态免费（EVERGREEN），例：每天 N tokens、每月 $5。
- **私有 / 自部署端点：不收（2026-10-19 Joe 定案，R2）**。本地推理栈（llama.cpp、本地 Ollama、LM Studio、Jan、GPT4All、KoboldCpp、text-generation-webui、llamafile、bentoml 自托管）与"自家服务器上的私有端点"。理由：没有额度/限流概念，五个字段填不满，也没有可注册入口。**Ollama Cloud 不属于此类**（托管、发 key、有月度免费额度）。

判定要点：

- 关键区分是**截止时间的口径**，不是「会不会结束」。所有人同一时刻截止 → 日期型限时；剩余时间因账号而异 → 新账号额度（trial）。
- 地区、学生、绑卡等**资格**限制不改变限时属性，只要截止日对符合资格的用户是同一个固定日历时间。
- 「前 N 名」「邀请制」「先到先得且名额不定」这类**资格或名额因人/因时变动**的活动仍不作为限时活动收录。
- 入选门槛（2026-10-19 放宽）：**日期型**只要本次执行时未过期就收录（限时侧不设剩余天数下限）；**措辞型**只要官方明示限时即可收录。
- **证据来源**：首选厂商官网/官方 changelog/官方社媒。当官方页面拿不到（JS 渲染、仅站内公告）时，**新闻线（如 PANews）或聚合站可作为日期证据来源**（Joe 2026-10-19 授权）；能同时拿到官方源时优先官方。
- 日期字段文案对照：常态免费 → 长期有效；日期型限时 → `截止日（剩余超7天）`，**剩余 ≤7 天时改写成 `截止日（剩余 N 天）`**（2026-10-19 新增：剩余天数下限取消后，日期型条目可以只剩几天，"剩余超7天"会变成假话）；措辞型限时 → `未公布截止日`；新账号额度 → `N天（自开通或发放起算，剩余时间因账号而异）`。
- **中转站「注册送 / 新用户赠送」（2026-10-19 Joe 改判：一律不收，R1 宽口径）**：这是**一次性额度**——注册送一笔、用完为止、不按周期重置，没有对所有用户统一的活动截止日。早前按"因注册时间而异 → EVERGREEN"处理，2026-10-19 Joe 定为**一律砍**，302.AI（注册送 $1）与 Jiekou.AI（注册送额度）已下架。判定不被"是平台自有 key"改变：形态是一次性就是一次性。
  - 仍然收的形态：**周期性重置**的中转站额度（每月/每周/每日刷新）→ 常态免费；**官方公告了统一截止日**的赠送活动 → 限时活动。
  - 以下是历史记录，仅用于识别同类条目（不再作为收录依据）：收录门槛是官方页面写明赠送内容；不收邀请制/名额制/充值返利/用途受限的；正文需注明"额度来自平台自有 key，不是厂商直连额度"且"额度与规则随时可能变更"。
  - 不收：需邀请制或名额制的、必须充值才返的、用途受限的（如百川）。「绑定邀请码」这类人人可得的门槛视为可收，但要在正文写明。
  - 中转站条目一律注明两点：**额度来自平台自有 key，不是厂商直连额度**；**额度额度与规则随时可能清零/变更**。赠送金额官方未公布时，必须写明"官方未公布具体金额"，不得引用第三方数字。
  - 中转站官网多为 JS 壳（DMXAPI、云雾 API、硅基流动控制台实测 moli / obscura 都读不到），**公告面优先找 `docs.` 子域 / FAQ / 定价页**——302.AI 的赠送写在 `price.302.ai/faq/`，Jiekou 的写在 `docs.jiekou.ai/docs/announcement/`。读不到又无官方公告面的，标 `blocked` 待人工核实，不猜数字。
- **限时窗口内领取、领取后 N 天有效**（2026-10-19 裁定，AutoClaw 案例）：判定看**还能不能领**的那个截止日，不看领到之后的有效期。领取窗口对所有用户是同一个固定日历区间 → 归日期型限时；领取后的 7 天有效期写进正文，不改变分类，也不用 `window_days`。
- **同一产品中英文站两套口径**（2026-10-19 裁定，AutoClaw 案例）：同一 provider 同 `offer_type` 只能有一行（指纹去重），所以**合并成一条**，`expires_on` 取覆盖整体活动的最晚截止日，正文并列两站各自的活动内容与额度；清单语言对应的站点口径写在最前，另一站注明「中文站另有…」/「the CN site runs a separate campaign」。不要因为口径不同就拆成两条 provider。
- **每日重置型额度**（如"每日登录领 500 万，当日 24:00 清零"）：仍是一个日期型限时 offer，把"当日清零"写进 `limit_*` 和 `quota_*`（例：`每日 5M tokens，当日 24:00 清零`），不要为每天的额度单独建行。

## 发现面：来源清单与查询词族（2026-10-19 新增）

AutoClaw 漏抓复盘（Joe 2026-10-19 转发的「登录送 3000 万 token」）的结论：不是「限时线」判定失效，而是**这条 offer 的发布面不在监控清单里**。所以发现面按「发布面」组织，不按「厂商」组织。

### 一、`source_url` 规则（硬约束）

- `source_url` 只允许**公告面**：`/blog/news/`、`/blog/`、`/changelog/`、`/events/`、`/pricing`、免费模型文档页。**禁止** console / 登录页 / 产品站首页——这类页面要么 fetch 必失败，要么内容永不变，等于把核实环节变成摆设（2026-10-19 之前 18 个 provider 里有 4 个长期 fail）。
- 同一个 provider 可以、也应该挂**两个**页面：
  1. offer 自己的 `source_url`：本次事实的核实页；
  2. `providers.homepage`：**公告索引页**（`/blog/news/`、`/changelog/`、events 目录），负责发现**下一个**活动。
  `state.source_pages()` 会把两者都纳入 pagewatch。只挂一个页面时，本期能核实、下一期就没人盯。
- 同一厂商的**不同产品算两个 provider**（智谱开放平台 ≠ AutoClaw）。不要把产品活动塞进 API 平台的核实页。

### 二、必查来源清单（每日直接抓，不靠搜索发现）

| provider | 公告索引页（homepage） | 当前活动/核实页（source_url） |
|---|---|---|
| AutoClaw（智谱） | `autoclaw.z.ai/blog/news/`（中文站 `autoclaw.zhipuai.cn/blog/news/`） | `autoclaw.z.ai/blog/news/M10W3/` |
| Qoder | `docs.qoder.com/llms.txt`（全站文档索引，含 `/zh/events/*`） | `docs.qoder.com/zh/events/flashoffer` |
| OpenCode Zen / Go | Zen / Go 文档里的 Free models 专节 | 同左 |
| WorkBuddy（腾讯 / 国际版） | `workbuddy.ai/docs/workbuddy/Subscription` | 同左 |
| Ollama | `ollama.com/blog` | `ollama.com/blog/reflection-beam` |
| Vercel AI Gateway | `vercel.com/changelog` | `vercel.com/ai-gateway`（「Limited time」促销区，逐模型截止日看模型页） |
| OpenRouter | `openrouter.ai/announcements` | `openrouter.ai/collections/free-models` |

CN 厂商的活动位固定在**产品博客 / events 目录**，不在定价页：AutoClaw 是 `/blog/news/` 周更（M10W2 10/12、M10W3 10/14 中 / 10/16 英、free-token-event），Qoder 是 `docs.qoder.com/zh/events/*`（一个目录挂 6 条：flashoffer / sotafree / efficientunlimited / bogo / newqoderlaunch / qwen-max / 100credits）。定价页永远看不到这些。

### 三、查询词族（2026-10-20 起：周任务跑全套，每日只定向补 1~3 次）

- 日期型：`free through <月>` / `free until <月>` / `promotion period` / `免费延长到 <日期>` / `限时免费 大模型 API 截止`
- 措辞型：`free for a limited time` / `limited time free model` / `限时免费` / `限免` / `promotion terms`
- **CN 客户端活动型（新增）**：`登录送 token` / `每日登录 领 积分` / `积分加油站` / `限免 截止` / `限时免费 结束时间 公告` / `限免 延期`
**执行频率（2026-10-20 Joe 定）**：三组词族的全套 + 产品名笛卡尔积只在周任务里跑（job `ade61a61e8ff`，周日 18:00 UTC，同时做 `provider_index watchlist --sample 20` 与 AA 榜单刷新）。每日管线只保留定向补充：跟踪的公告索引页出现本期没见过的活动时，按「产品名 × 活动词」查 1 次，**每天最多 3 次**。理由：每日事实来源已经是 27 个跟踪页，泛词每天跑等于重复发现同一批；降频的代价是「当天发、次日截」的活动可能漏一天，补偿手段是把该 provider 的公告索引页加进跟踪，而不是恢复每日泛词。

- **产品名 × 活动词**定向查：把来源清单里的产品名与上面词族做笛卡尔积。实测（2026-10-19，yahoo / toutiao / sogou-weixin 三引擎）：泛词 `限时免费 大模型 API 截止` 对 AutoClaw **0 命中**；`智谱 AutoClaw 免费 3000万 token` 和 `AutoClaw 登录送 3000万 token 限时` **3/3 命中官方原文**。泛词只覆盖"模型限时免费"，覆盖不到"客户端发积分"。

### 四、线索层（Tier B，只作线索，截止日必须回官方）

用来兜住**清单外的新品**——新产品永远加不完，所以要有一条不依赖白名单的入口：

- `buguoshixc.github.io/ai-deals-aggregator/`：50 条优惠、标「每日更新」「即将截止」，带国内/国外/免费 API 分类和官方跳转
- `post.smzdm.com/p/ak8l35ze/`：全网 AI 产品免费权益清单，按日更新
- `allagent.wiki`：changelog + 每日速递，含精确活动窗口

聚合页自身写的"截止"一律重新回官方核实，不得直接当日期证据。

### 四之二、竞品目录导入（`import-competitors`，2026-10-19 新增）

两个公开目录按 provider 出表，填补的是**覆盖面**（"世界上哪些厂商有免费面"），不是事实。它们都是自家站点数据库的导出视图，没有更上游的源：

| 目录 | 上游 | 生成方式 |
|---|---|---|
| `nejib1/Free-LLM`（free-llm.com） | 自家站点库 + 社区提交/投票 | README 由 `<!--STATS:START-->` / `<!--TABLE:*:START-->` 标记生成 |
| `open-free-llm-api/awesome-freellm-apis`（freellm.net） | 自家爬虫库（自称 453 模型、每日更新）+ `free-llm-models` Python 包 | `<!-- BEGIN_PERMANENT_FREE -->` / `<!-- AUTO_LAST_UPDATED -->` 标记生成 |

```bash
python3 -m tooling.provider_index import-competitors /tmp/tok/nejib.md --source nejib1/Free-LLM --ref <sha>
python3 -m tooling.provider_index import-competitors /tmp/tok/ofa.md   --source open-free-llm-api/awesome-freellm-apis --ref <sha>
```

落地口径（全部强制执行，不靠自觉）：

- 只进 `t_provider`，**永不产生 offer 行**；`coverage=candidate`，`announce_url`/`free_page_url` **一律留空**（他们给的是 console/注册页）。
- `category` 用我们自己的 `classify()`，不采信他们的分类。
- `notes` 前缀 `UNVERIFIED[<source>@<sha>]`，原样保存他们的限流/绑卡/模型数——那是线索，不是证据。
- 段落判定：`Trial Credits` → `out_of_scope`（R1）；`Local / Self-Hosted` → `out_of_scope`（R2）。
- **两家分类冲突时不裁决，取 candidate 等人工核实**（`coverage_guard` 保证 candidate 不会被任何一个目录降级为 out_of_scope，且与导入顺序无关）。
- 同名复用：显示名按 `name_key()` 匹配到唯一已有 provider 时复用它的 slug，不新起一行；匹配到 0 个或多个则保留新 slug（宁可留重复，不许合并错人）。

**这两家的分类可信度实测（2026-10-19）**：抽查 12 条，**错 3 条**——Cerebras 被标 permanent free tier，官方实为一次性 $5/30 天；HuggingFace 被标 permanent free tier，官方写明免费用户额度为 `None`；OpenCode Zen 被标 permanent free tier，官方 docs 明写数个模型 "for a limited time"。所以：**目录只用来回答"该去看谁"，任何一个事实都必须回官方页。**

### 五、人工通道（补充，不替代自动化）

`weixin.sogou.com` 实测返空壳（16KB，只有页脚），**微信公众号 / 微信群这一最上游的信息面机器不可达**，Joe 转发的消息多属这一类。处理规则：收到转发 → 当场核实官方页 → 直接 `sync` + 渲染发布，不等次日 cron。对"当日 24:00 清零"的活动，这是唯一能赶上当天的方式。

### 六、已核实但暂不收录

- **百川「海纳百川计划」**（2026-10-19 核实）：官方文档页横幅「申请加入海纳百川计划 · 免费使用 M3Plus API」，2026-01-22 起，限服务于中国医疗工作者的机构、仅限临床辅助决策与医学教育，无公告截止日。属**申请 / 资格制 + 用途受限**，不是自助额度，暂不收录；若开放自助注册再评估。

## provider 索引表 t_provider（2026-10-19 新增）

每天靠搜索找漏是治标。`t_provider` 是**覆盖地图**：先枚举「世界上有哪些 provider」，再给每家标出该盯哪个面。缺一个面就是表里一行空字段，而不是一次静默漏抓。

表在同一个仓库外库 `/opt/data/tokenation/tokenation.db`，由 `tooling/provider_index.py` 维护，**不发布**。

分类（`category`）：`foundation` 基础模型厂商 / `cloud` 云厂商 AI 平台 / `gateway` 中转聚合 / `inference` 推理服务商 / `harness` 客户端与编码代理 / `local` 本地推理栈 / `aggregator` 优惠信息源（非厂商，只作线索）/ `unknown` 待分类。

每家可填的观测面：`announce_url`（公告索引，新活动最先出现）、`free_page_url`（直接挂免费额度的页）、`pricing_url`、`docs_url`；`watch_mode` 记录该面属于哪一类（`announcement_index` / `event` / `pricing` / `docs_free` / `web_search`）。`coverage` ∈ `tracked`（已进 offers）/ `verified`（来源已核实）/ `candidate` / `blocked` / `merged`。

```bash
python3 -m tooling.provider_index seed                    # 载入 tooling/providers_seed.json（人工维护，带分类与 URL）
python3 -m tooling.provider_index import-modelsdev <api.json>    # models.dev 开源库，批量发现新厂商
python3 -m tooling.provider_index import-openrouter <providers.json>  # OpenRouter 路由伙伴
python3 -m tooling.provider_index import-competitors <readme.md> --source <slug> --ref <sha>  # 竞品目录 → 只产候选
python3 -m tooling.provider_index reclassify              # 只给 unknown 打标签，不覆盖人工分类
python3 -m tooling.provider_index dupes                   # 松散同名检测
python3 -m tooling.provider_index merge <from> <into>     # 合并重复行（源行保留为 alias，不删除）
python3 -m tooling.provider_index sync-offers             # 标记哪些已进 offers
python3 -m tooling.provider_index report                  # 分类统计 + 覆盖缺口
python3 -m tooling.provider_index watchlist               # 已在监控的观测面清单
python3 -m tooling.provider_index watchlist --sample 5    # 轮转 5 家「还没有观测面」的候选（按 models_count 降序）
python3 -m tooling.provider_index triage [--file F] [--dry-run]   # 把查到的观测面写回 t_provider
python3 -m tooling.provider_index watchcheck [--since D] [--expect N]  # 周任务自检：本周真的写回了吗
python3 -m tooling.provider_index dedupe-plan [--min-gain 1]      # 同一厂商重复导入的合并建议（只打印）
```

每周任务的发现流程（2026-10-20 Joe 定，job `ade61a61e8ff`）——**先缩小分母，再花抓取**：

1. `dedupe-plan` 出合并建议 → 逐对 `merge`。合并只补空字段、源行留作 alias（`coverage=merged`），不删数据。**只合明确同一厂商的行**：不同产品（DevPass vs LLM Gateway）与各区域独立套餐（`kimi-code-plan-cn` vs `-global`）不合；代码里已按 `REGION_SUFFIXES` 收窄到 `-cn/-china/-us/-eu/-ams/-sgp`，并跳过 slug 全含 `plan` 的组。
2. `watchlist --sample 20` 取样现在**按 `models_count` 降序**（此前是 `md5(slug|date)` 随机，抽样里大量是零模型的空壳）。查清后写 `/tmp/tok/provider_surfaces.json`，再 `triage` 写回。
   - `triage` 的护栏：未知 slug 报错而不建行；只写 payload 里出现的列（缺省不清空旧值）；`announce_url`/`free_page_url`/`pricing_url` 命中 `pagewatch.is_unverifiable`（console / 登录 / apikey）就拒收，但 `console.<host>/docs/` 这种文档面放行；`blocked`/`out_of_scope` 不许被抬回 `candidate`/`tracked`；有观测面但无显式 coverage 的 `candidate` 自动升 `verified`（否则 `report` 与自检永远看不到它）。
   - 写完必须跑 `watchcheck --since <今天> --expect 1`：回写 0 条即 exit 1，周任务回执写失败，不许把「已查 20 家」当成果。
3. `reco_score aa-gap --limit 20`：AA 榜单里**我们完全没有收录**的模型家族（按 AA 分数降序，按家族去重——AA 给同一模型 Max/High/Low 多档，slug 与括号里都带档位标记，所以 `_family_key` 要两边都剥）。这是最便宜的线索：AA 分数一到位，智能维度就是实测值，不用掉到 11.4 回退。

每日任务里怎么用：

1. `watchlist` 的输出就是「固定抓取」的目标，与 pagewatch 的 tracked 页互为补充；
2. `watchlist --sample 5` 每天换一批候选（按 `md5(slug|date)` 排序，不额外存状态），一次查清 5 家的公告面/免费页并写回 `announce_url`/`free_page_url`，逐步把 400+ 家收敛成可监控集合；
3. `report` 的「缺少观测面」列表按模型数排序，优先补大厂；
4. 新增/删除 provider 一律先改 `t_provider`，再从它推进 `offers`。

开源数据源（本表由它们批量导入，均为开源项目）：

- `https://models.dev/api.json`（sst/models.dev）：232 家 provider + 模型元数据，2026-10-19 导入
- `https://openrouter.ai/api/v1/providers`：112 家路由伙伴，用于发现真实在供模型的上游
- `https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json`：$0 定价可批量筛出「被标成免费的模型」
- `github.com/cheahjs/free-llm-api-resources`、`github.com/ClawLabsAI/free-ai-models`：每日更新的免费清单

## 每日搜集

1. 使用本次 UTC 日期作为更新日期。
2. 确认工作目录、远端、分支和工作区状态。提交身份固定为 `precisionz <62896761+precisionz@users.noreply.github.com>`，不得使用真实姓名（见“署名”节）。
3. **先跑 `python3 -m tooling.daily prep`，再决定要读哪些页面**（见「增量核实」节）。只有 stale 列表里的页面需要 LLM 重读；unchanged 的沿用状态库里已核实的事实。
4. 两条采集线分开跑，都用 Moli 并行搜索再抓官方页（来源清单与查询词族见「发现面」节）：
   - **固定页面线（每日必跑）**：`pagewatch fetch` + `report` 覆盖库里的 27 个跟踪页（每个 active offer 的 `source_url`，加各 provider 的公告索引页）。这是每日核实的主路径，不依赖搜索。
   - **搜索线（只做发现）**：词族见「发现面」节。辅助脚本两个：`tooling/run_batch.py`（`searches <queries.json> <outdir>` / `pages <urls.json> <outdir>`，并行 moli 搜索与抓页）与 `tooling/collect_limit_time.py sources`（抓固定来源清单）。聚合站（aipromonow / resourify / felloai / buguoshixc / smzdm / allagent.wiki 等）只作线索，截止日必须回官方页核实。
   - 传输兜底：`moli fetch`（主）→ `obscura fetch`（兜底）→ 两者都失败时用内置搜索工具，并在日志记明降级。
   - 两条线现在是**发现**用途：库里已有的 provider 不需要靠搜索重新发现，搜索只用于找库里没有的新 offer 与新 provider。搜索摘要只作线索，不能单独作为证据。
5. 对每个 stale provider 核对官方价格/免费额度、模型目录、限流、活动条款和注册链接，并把它写进 `source_url`（官方核实页，不是注册链接）。
6. 明确区分通用 API Key 和 harness 产品内额度。不能把产品内 credits 描述为通用 API Key。
7. 长期有效的免费服务（常态免费）可入选。限时活动的定义见「offer 分类」节：日期型（有官方公布的固定统一截止日）只要本次执行时**未过期**就收录，不设剩余天数下限；措辞型（官方只写「限时」、未公布截止日）也收录。已过公布截止日的一律排除。常态条目沿用原有 7 天缓冲（`MIN_REMAINING_DAYS = 8`，仅约束无 `window_days` 的非长期条目）。
8. 标明适用地区、账号资格、绑卡或身份验证要求，以及额度耗尽后的计费行为。
9. RPM、RPD、TPM、TPD 等数据以官方当前信息为准。没有官方统一数字时写明“官方未公布统一限额，按账户/模型动态调整”，不得猜测。推荐模型必须逐项确认当前免费，并写准确模型 ID。
10. 同一 Provider 只保留一条，多个活动合并进 `活动/类型` 字段。去重由 state 层的指纹 + Jaccard 与 `dedupe` 兜底。
11. **没有条数上限**：渲染器按「已评分模型」逐行发布（一个 offer 可占多行，当前 21 个 active offer → 62 行），不凑数也不截断。EVERGREEN 不足 10 条或任一关键事实无法核实，保留旧版五份文件，不提交不推送，并在本地任务记录原因。LIMIT-TIME 允许 0 条（渲染器输出"当前暂无…"提示），不得因限时为空而中止。**无推荐指数、无模型介绍的条目不会发布**（见「发布门槛」节）。

## 增量核实（2026-10-19 新增）

免费额度页是周级变化，日级全量重读是浪费。拆成两段：脚本负责抓取与比对，LLM 只读变化的页面。

日常只需要两条命令，顺序由脚本保证（2026-10-20 起）：

```bash
python3 -m tooling.daily prep --workers 5   # fetch + report + 写 /tmp/tok/prep.json（含每个待读页的 text_path 与库内现存字段）
#  （LLM 只读 prep.json 里的 stale 页面，把改动写进 /tmp/tok/offers.json）
python3 -m tooling.daily finish             # sync -> mark -> confirm -> 评分闸门 -> 渲染 -> 校验 -> 只暂存五份文件
python3 -m tooling.daily status             # 计数、last_verified、最后一次提交、频道状态、新鲜度闸门结论
```

`daily finish` 不 commit、不 push，提交身份与推送仍由 agent 显式执行。

### 两层抓取（2026-10-20 实现）

每页每天仍然抓一次，但只有「指纹变了」的页才起浏览器：实测 27 页从 74.6s 降到 7~13s。

- **第一层**：`requests` 直接取 HTML，bs4 去掉 script/style/svg 后取正文，算 sha1。并发 8。
- **第二层**：只有 HTTP 指纹变了、或可见正文 < `MIN_CHARS = 1500`（JS 壳）、或 HTTP 失败时才调 moli/obscura。
- 指纹来源记在 `page_state.basis`（`http` / `markdown`）。换基线不会静默通过：该页报 `changed`，并把 `page_state.status` 置为 `rebaseline`。`changed` 状态下 `mark` 不推进 `last_verified`，直到 `daily finish` 里的 `pagewatch confirm` 把它关掉。**没有 confirm，同一页会一直报 changed**，这条闸门防的就是「换了基线但没人读」被当成已核实。
- `pagewatch fetch --no-http` 退回全浏览器模式，用于对照与回滚。
- 待读页面正文会落盘到 `/tmp/tok/stale/<provider_id>-<slug>-<url哈希>.md`，`prep.json` 的 `text_path` 指向它。同一 provider 的两个页面不会互相覆盖。
- `unverifiable`：URL 命中 `console|dashboard|dash.|/sign-up|/login|/apikey|api-keys`（但 `/docs/` 路径例外，例如 `console.groq.com/docs/rate-limits`）时直接判不可核实，**永不标记已核实**，也不抓。这类页面是登录墙，抓到了也证明不了额度。

判定口径：

- `unchanged`：指纹与上次一致（页面规范化后 sha1 相同）。沿用库中事实，**不重读、不重写**，`mark` 会把 `last_verified` 推进到今天并写一行 `offer_evidence`。
- `changed` / `new`：必须用本次抓到的页面重新核实。
- `fail`：抓取失败或页面过短（登录墙、纯 JS 壳）。**不得**当作 unchanged，也不得标记为已核实，按降级规则人工回官方页核实。
- `unverifiable`：`source_url` 本身是 console / 登录 / apikey 面，永远证明不了额度。修法是换 `source_url`，不是重试。
- `rebaseline`：指纹基线变了（`basis` 从 markdown 换成 http 等）。报 `changed`，等 `confirm` 才回到正常。
- 指纹变化只是「值得一看」的信号，不是事实变化的证明：假阳性代价是读一页，假阴性代价是发布过期事实。所以规范化只做空白/零宽字符折叠，日期、数字、模型 ID、价格一律不剥离。
- 记录里存了 transport：moli 与 obscura 抓同一页可能得到不同文本，跨 transport 的比对会判 changed，属于可接受的假阳性。

`source_url` 必须是**公告面**（`/blog/news/`、`/changelog/`、`/events/`、定价页、免费模型文档页），不是注册链接：增量核对比的是这个页面。

`state.source_pages()` 每个 provider 最多产出**两个**被跟踪页面：每个 active offer 的 `source_url`，加上 `providers.homepage`（公告索引页）。两者都进 pagewatch：

- 只挂 `source_url`：本期能核实，下一期新活动没人盯——这就是 AutoClaw 漏抓的形态（库里只有 `open.bigmodel.cn`，活动却在 `autoclaw.z.ai/blog/news/`）。
- 只挂首页 / console：fetch 多半失败、长期 stale，核实环节等于摆设。2026-10-19 已把 4 个长期 fail 的改成公告面：Cerebras → `cerebras.ai/pricing`；GitHub Copilot → `docs.github.com/en/copilot/get-started/plans`；WorkBuddy 国际版 → `workbuddy.ai/docs/workbuddy/Subscription`；Zhipu → `docs.bigmodel.cn/cn/guide/models/free/glm-4.7-flash`。
- 一个 provider 可能同时出现在 `stale` 和 `unchanged`：它的两个页面独立判定，按**页面**粒度读，不要按 provider 粒度跳过。
- 已知遗留：Together AI 的 `together.ai/pricing` 三个 transport 都拿不到（moli 空、obscura 1 字节），仍需换页或走浏览器渲染，暂按 fail 处理。

## 发布流程（脚本化，禁止手写 Markdown 正文）

1. 采集产物放仓库外 `/tmp/tok/`，写成结构化 `offers.json`（字段见下）。`daily prep` 已经把每个待读 provider 的**现有完整记录**放进 `prep.json` 的 `current` 块，整条复制再改，不要从零手写。
2. 写入 SQLite 状态库（仓库外 `/opt/data/tokenation/tokenation.db`，唯一事实源，含精确指纹 + Jaccard 去重、过期判定、重复行合并）并渲染：一条 `python3 -m tooling.daily finish` 完成 sync → mark → confirm → 评分闸门 → 渲染 → 校验 → 暂存五份文件。分步等价命令：
   ```bash
   python3 -m tooling.state sync /tmp/tok/offers.json --today YYYY-MM-DD
   python3 -m tooling.pagewatch mark            # unchanged 的条目推进 last_verified + 写证据行
   python3 -m tooling.pagewatch confirm         # 关闭 rebaseline，下一轮才可能判 unchanged
   ```
3. `daily finish` 内部已按序完成了渲染与两道校验，说明如下（要单独重跑时才手敲）：
   ```bash
   python3 -m tooling.render_all --from-db . --today YYYY-MM-DD
   python3 -m tooling.render_check README.md cn/EVERGREEN.md cn/LIMIT-TIME.md en/EVERGREEN.md en/LIMIT-TIME.md --db /opt/data/tokenation/tokenation.db
   ```
   渲染器按 `kind` 分流（`promotion` → LIMIT-TIME，其余 → EVERGREEN），已过期的限时条目直接丢弃、LIMIT-TIME 允许 0 条。四份清单按**推荐指数从高到低**排列，同分依次比「截止日升序 → provider 规范名 → model_id」。无评分 offer 在计数前被剔除并在 stderr 点名 `not published (no recommendation score)`，`offers-N` 徽章只统计实际发布的内容。校验器解析表格：表头与本语言列集精确一致、每行列数正确、模型 ID 是行内代码、介绍非空、分数是 `**NN.NN**`、分数非递增。任一项失败整体中止，五份文件都不写。

README 的落地表（2026-10-20 改，AA 门槛 v6）：与清单同一套 model × provider 行，但**两类混排**并多一列「类型」（`限时`/`常态`，EN 为 `Limited-time`/`Evergreen`），共 **9 列**（含 AA），取全站推荐指数最高的 `README_TOP_N=15` 行；README 专表只接纳有实测 AA 且 **AA > 30** 的模型（AA 缺失或回退值不得入榜），另有每品牌最多 `README_PER_PROVIDER=3` 行。同一品牌同模型只出一行（Zen/Go 共享 free 目录；有模型级截止日时保留带日期的记录）。排序键是「分数降序 → model_id → offer 链接」。`render_check` 支持 `--db /opt/data/tokenation/tokenation.db`，用数据库独立重算 AA>30 的 Top15 并核对 AA 列；不传 `--db` 时校验 9 列格式、AA 数值与门槛、列表成员和分数顺序，但无法证明全量候选的精确 Top15。表上方一句说明榜单，表下方说明总行数并链接评分口径；评分节在榜单之后、四个清单链接之前，每语言各一节。首屏徽章区除 updated/offers/verified 外还有一枚静态 `every row scored 0-100` 徽章。

**模型级截止日（2026-10-20 Joe 定）**：一个 offer 内不同模型可以各有各的窗口，所以截止日是**模型级**事实，不是 offer 级。存放位置 `t_offer_model.model_end_time`（由 `reco_score.load_catalogue` 从 catalogue.json 每个 model 的 `end_time` 写入；payload 省略该字段时保留库内旧值，不会被目录重载抹掉）。渲染优先级：`model_end_time` > offer 的 `end_time` > 长期有效/未公布截止日；该模型自己的日期一过，只摘掉这一行，同 offer 的其它模型继续发布。生效面：LIMIT-TIME 清单的「截止」列与 README 落地表（9 列，恒有「截止」列）；EVERGREEN 清单没有截止列，所以常态 offer 的模型级日期只在 README 表上可见。首个案例：OpenCode Zen `minimax-m3.1-flash-free` 记 2026-10-22（官方 X 2026-10-19 12:17 UTC：Space Bunny 揭晓为 MiniMax M3.1 Flash，OpenCode 免费 3 天；Zen/Go 文档页只写 for a limited time）。
4. 发布前确认：`git diff --check`、`git diff` 与暂存清单（`git diff --cached --name-only`）只含五个 Markdown。渲染器不能判断事实真伪，Agent 必须自己逐条确认来源。
5. 提交并推送 `main`，然后读回远端五个文件，确认日期、条数、英中条目顺序一致。未读回验证，不得报告成功。
6. 认证、搜索、抓取或推送失败时，停止发布并保留旧版。禁止 force push，禁止输出 Token 或其他凭证。

## 渲染器不负责的三件事（每次都人工确认）

- `---` 前后是否各有一个空行：`render_check` 能发现被解析成标题的情况。
- 是否误把产品内 credits 写成通用 API Key。
- 限流数字是否有官方来源。渲染器只检查字段非空。

## 结构化数据格式（offers.json）

```json
{
  "offers": [
    {
      "name": "GroqCloud",
      "kind": "free_tier",
      "is_forever": true,
      "models": [{"model": "openai/gpt-oss-120b", "note_cn": "通用推理", "note_en": "general reasoning"}],
      "link_text": "Groq API Keys",
      "link_url": "https://console.groq.com/keys",
      "limit_cn": "30 RPM、1,000 RPD",
      "limit_en": "30 RPM, 1,000 RPD"
    }
  ]
}
```

- `kind`：只允许 `free_tier` / `promotion`。分流：`promotion` → LIMIT-TIME，其余 → EVERGREEN。**`trial` 已退役（R1），新记录不得再写**；库里历史 `trial` 行只作审计，渲染器不再输出。
- 限时活动（`promotion`）：**日期型**用 `expires_on`（ISO 日期，官方公布的统一截止日），不得同时填 `window_days`；**措辞型**（官方只写"限时"、未公布截止日）`expires_on` 留空。
- `window_days` 仅历史 `trial` 行会用，新记录不再使用。
- `models` 1~3 条，`model` 是准确模型 ID，**一律小写**（2026-10-20 Joe 定：厂商页面写 `Qwen3.8-Flash`、`GLM-5.3`、`Qwen/Qwen2-7B-Instruct` 也要转小写发布，这一列表示「你该输入什么」，不是厂商品牌写法）。写入由 `state._upsert_model()` 兜底转小写、`reco_score.load_intros` 的键也转小写，渲染器对含大写字母的 ID 直接判失败；`note_cn/en` 可省略，省略时括号不渲染。
- `limit_cn/en` 必填，渲染器对空值报错。
- `quota_cn/en`：给清单与 README 表共用的**短额度**，约 30 字以内（例：`每天 10,000 Neurons` / `30 RPM · 1,000 RPD`）。限时条目必填；缺失时渲染器退化成截断的 limit 首句并在 stderr 告警。增量同步时缺这个字段不会覆盖库里已有的值。
- `source_url`：**公告面**（`/blog/news/`、`/changelog/`、`/events/`、定价页、免费模型文档页），增量核对比对的就是它；不填会退回注册链接，那种页面通常 fetch 失败并长期 stale。
- `homepage`：**公告索引页**（产品 blog / changelog / events 目录 / `llms.txt` 之类全站索引），用来发现下一个活动。`state.source_pages()` 会把它和 `source_url` 一起交给 pagewatch，所以两个都该填。
- 另有 `region`、`requires_card`、`requires_kyc`。

## 状态库（SQLite）

仓库外 `/opt/data/tokenation/tokenation.db`，是渲染的唯一事实源。表按维护模块分：`state.py` → `providers` / `models` / `offers` / `offer_models` / `offer_evidence` / `snapshots`；`pagewatch.py` → `page_state` / `page_checks`；`provider_index.py` → `t_provider`；`reco_score.py` → `t_offer_model` / `t_score_input` / `t_aa_index` / `t_model_intro`。

- `offers.offer_type` ∈ {`evergreen`,`limit_time`,`trial`}（`trial` 只剩历史行）。实际约束只有两条：`limit_time` 的 `window_days` 必须为空、`trial` 的 `window_days` 必须非空。**`limit_time` 的 `end_time` 允许为空**——措辞型限时正是靠这个字段留空表示「未公布截止日」，不要试图加 NOT NULL。
- 去重两段：① 精确指纹 `sha1(provider|**排序后**的归一化 model_id 集合|offer_type)`，撞键即合并（model 顺序不同必须落在同一行——`export` 再 `sync` 的往返在 2026-10-19 之前会凭空多出一条重复行）；② **Jaccard** 对 (provider + 模型 ID + spec) 的 2-gram token 集计算，`>=0.85` 归并、`0.5~0.85` 记入 `duplicates` 日志供人工复核。同 provider 的 evergreen 与 limit_time 指纹不同，不互斥。
- 第三道兜底：`dedupe`（`sync` 每次自动跑，也可单独 `state dedupe`）。同一 provider + offer_type 出现多条 active 行时，保留最新一条，把旧行缺的字段补到保留行上，旧行置 `removed`（不删除，保留审计）。渲染器对重名会直接报错，所以这一步是发布不中断的保险。
- `migrate`（每个命令启动时自动跑）只做加法：补列、跑 dedupe、把库存指纹重算到当前方案（历史行指纹加 `#id` 后缀避免与活跃行撞 UNIQUE）。**永不删除行。**
- 过期：`end_time < 今天` 的 `limit_time` 置为 `expired`，不再渲染。
- 增量核实表：`page_state`（每个 provider 的核实页当前指纹）+ `page_checks`（逐次判定历史），由 `tooling/pagewatch.py` 维护。
- 评分表（仓库外，不发布）：`t_offer_model`（该 offer 下可枚举的全部免费模型）、`t_score_input`（每 provider×model 的 AA 指数/每日额度/口径 note/note_en）、`t_aa_index`（AA 榜单快照）、`t_model_intro`（每 model 的 `intro_cn`/`intro_en` 用途定位 + `intro_kind`（vendor/fallback）+ 核实源）。由 `tooling/reco_score.py` 维护，加载命令 `python3 -m tooling.reco_score load-intros <json>`。
- 排序范围表（仓库外，不发布）：`t_model_param`（`params_b` 总参数 / `active_b` 激活参数 / `source_kind` / `source_url` / `note`）、`t_model_kind`（`kind` ∈ chat/decision/router + 证据 URL）。种子文件 `tooling/model_scope_seed.json`，加载命令 `python3 -m tooling.reco_score load-scope <json>`；**重建数据库后必须重跑这一步**，否则范围规则失效（参数量全变 unknown，被判为可排序）。
- 证据表 `offer_evidence` 由 `pagewatch mark` 写入，字段是 `url` + `fetched_at` + `snippet`，判定值存在 `snippet` 列里（形如 `sha1=unchanged`）。2026-10-19 之前一直是 0 行。
- 常用命令分四组：`daily prep|finish|status`，`state init|sync|export|report|dedupe`，`pagewatch fetch|report|mark|confirm|urls`，`reco_score init|load-aa|refresh-aa|load-catalogue|set-input|load-intros|build|check`。
- `load-catalogue` 的 payload 形如 `{"offers":[{"provider":"…","models":[{"model_id":"…","end_time":"2026-10-22"}],"source_url":"…","measured_at":"…","catalogue_complete":true}]}`。`end_time` 可选，是**模型级截止日**（见上文）；省略时库里已有的日期保留，不会因重载目录被清空。带日期的模型过期后自动下架该行，其它模型不受影响。
- `reco_score load-aa` 只刷新快照缓存 `t_aa_index`，不改变任何分数；要把新 AA 数字用到评分上必须再跑 `reco_score refresh-aa`（按 `aa_slug` 回写 `t_score_input`，22 条 fallback 行不动）。

## 输出固定格式（渲染器生成，勿手改）

2026-10-20 起四个清单文件是 **model × provider 表格**，不再是五段式条目。一个文件 = 一句话说明 + 更新日期 + 一张表；行 = 一个 model 在该 provider 上的免费额度。

```text
各平台常态免费额度，按推荐指数从高到低排列

（更新至 YYYY-MM-DD）

| 平台 | 模型 ID | 介绍 | 免费额度 | 推荐指数 | 链接 |
| --- | --- | --- | --- | --- | --- |
| **Provider 名** | `model-id` | 一句话用途定位 | 短额度 | **90.07** | [→](https://...) |
```

- 首句：EVERGREEN 用 `各平台常态免费额度，按推荐指数从高到低排列`；LIMIT-TIME 用 `各平台限时免费活动，按推荐指数从高到低排列`（中文 ≤35 字，英文 ≤35 词，均为固定文案，写在 `LABELS` 里）。
- 第二行固定 `（更新至 YYYY-MM-DD）` / `Updated YYYY-MM-DD`，即本次数据核实日期。
- 列：EVERGREEN 6 列（平台 / 模型 ID / 介绍 / 免费额度 / 推荐指数 / 链接）；LIMIT-TIME 7 列，在「免费额度」后插入「截止」。列名中英各自固定，校验器精确比对表头。
- **行 = model**：每个已评分模型一行，同一 provider 多模型占多行；同一 provider 的行允许被其他 provider 隔开，因为整张表是单一排名。
- 排序：**推荐指数从高到低**（Joe 2026-10-20）。同分依次 `截止日升序`（限时）、`provider 规范名`、`model_id`。中英文两份必须逐行同序，tie-break 用规范名而不是显示名。
- 不参与清单排序的硬门槛：实测 AA ≤ 20 剔除，AA 缺失保留；因此可能有 AA 缺失的行仍在清单中，但 README Top15 另要求 AA 实测值 > 30。
- 推荐指数：`**NN.NN**`，**严格两位小数，不带 /100**（Joe 2026-10-20；`reco_score` 不再取整）。
- 介绍列：来自 `t_model_intro` 的 `intro_cn` / `intro_en`，一句用途定位（中文 ≤30 字、英文 ≤15 词）。缺介绍的模型**不发布**（`render_all` 剔除 + stderr 点名，`reco_score check` 也会报）。
- 免费额度列：取 `quota_*`；缺失时退化为 `limit_*` 的首段并**截断到 40 字**加省略号（Joe 2026-10-20：截断内容长度，不整条丢弃）。英文截断按词边界回退，不切半个单词。
- 单格不允许出现 `|`（渲染时替换为 `/`）与换行。
- 英文文件禁 CJK；`render_check` 会整文件扫一遍。
- 旧格式（编号条目、🏷️⏰⚡🤖🔗 五段、`---` 分隔线）已废弃，出现即校验失败。

## 发布门槛：无评分、无介绍不发布（2026-10-20 实现）

渲染前有两道硬闸，任一不满足就不发布：

- `python3 -m tooling.reco_score check` 必须输出 `ok`：每个 active offer 至少有一个可评分模型，且该模型在 `t_model_intro` 里的中英文介绍都存在。查不到官方说明时写「官方未公布…」并把 `intro_kind` 标成 `fallback`，不许编造定位。
- `render_all --from-db` 在计数前剔除没有任何已评分模型的 offer，并在 stderr 打印 `not published (no recommendation score): <names>`。`offers-N` 徽章与清单行数只统计实际发布的内容，所以徽章不会虚高。

## 评分口径：Q 取所有已公布上限里最紧的一条（2026-10-20 Joe 定，v5 规则）

`t_score_input` 里 `daily_reqs`（RPD）和 `daily_tokens`（TPD）是**并列的约束**，不是主次关系。`reco_score.effective_reqs()` 取 `min(daily_reqs, daily_tokens / 80000)` 作为实际可服务的请求数，再把 `reqs_used` / `token_cap_applied` 带进 build 输出，方便复查是哪条上限在生效。

- 起因：Groq 免费档对 `qwen/qwen3.8-27b` 与 `openai/gpt-oss-120b` 同时公布 30 RPM、1,000 RPD、8K TPM、200K TPD。库里只填了 `daily_reqs=1000`、`daily_tokens=NULL`，于是 Q 取到对数刻度的顶格 100，score 82.47 让它排在第二——而 200K/80K = 2.5 请求/天才真实可用。修正后 qwen3.8-27b 33.35、gpt-oss-120b 18.61。
- **TPM 不参与折算**：它是每分钟速率上限，在 8 万 tokens/请求的约定下，日 token 上限已经比它更紧，再折一次是把同一约束算两遍。8K TPM 的实际影响写进 `note`（"RPD 不是约束"），不进公式。
- 录入要求：只要官方页面同时给了 RPD 和 token 上限，两列**都必须填**。只填 RPD 会让该行拿到它交付不了的用量分。
- `fallback_25m` / `rpm_derived` / `tpm_derived` 的折半照旧，折半发生在取最紧之后，不是替代它。
- 权重（智能 40% / 额度 60%）与 AA 取数不动：这条规则只修输入层。Joe 2026-10-20 明确「改取数规则，不动权重」。

## 排序范围：谁参与排序（2026-10-20 Joe 定，v4 规则）

`reco_score.build()` 是唯一的闸门，渲染器和频道速递都只从它取分，所以范围规则只写在这一处。不参与排序的模型**不产生分数行**，因此不会出现在 README Top15、四份清单和频道「评分榜前三」里。

| 规则 | 判定 | 数据来源 |
|---|---|---|
| 决策模型不排序 | 只返回类型化结果、不产出自由文本（System One 类） | `t_model_kind.kind='decision'` |
| 路由端点不排序 | `auto (automatic model selection)` / `auto (automatic model routing)` 之类，本质是开关不是模型 | `t_model_kind.kind='router'` |
| 总参数 < 20B 不排序 | **严格小于**；20B 整仍参与。MoE 按**总参数**，不按激活参数 | `t_model_param.params_b` |
| 查不出参数量 | **照常参与排序**，绝不猜一个数往里填 | 无 `t_model_param` 行 |

登记表：`tooling/model_scope_seed.json` → `python3 -m tooling.reco_score load-scope <file>`（幂等，模型 ID 统一小写）。

参数量核实优先级（写进 `source_kind`）：

1. `id_token`：model_id 里明确的 `\d+b`，但 `a\d+b` 是激活参数位，不算总数。
2. `gateway_desc`：OpenRouter / Vercel 模型描述里的明文参数量，优先取「total」。
3. `hf_safetensors`：HF **基座 BF16** 仓库的 `safetensors.total`。**禁用** NVFP4/GGUF/int4 仓库（实测 Nemotron-3-Nano NVFP4 报 18.3B，实际 30B）。
4. `vendor_doc`：闭源旗舰看官方文档。

两条实测警告：模型名不能当参数量（`poolside/Laguna-XS-2.1` = 33.4B、`thinkingmachines/Inkling-Small` = 276B）；`gemma-4-26b-a4b` 的 `a4b` 是激活参数，26B 才是总数。

整家 offer 被规则清空时**整家下线**（Joe 2026-10-20）：`reco_score check` 会把这些 offer 列成 `not published (all models out of scope)` 但**不报错**（这是决策，不是数据缺陷）；`render_all` 的日志会带上剔除原因。缺 `t_score_input` 仍然是硬错误。

新增模型进目录时，当天必须写入 `t_model_param` 或保持 unknown（unknown 可排序），不允许"先排着以后再说"地编造尺寸。

## 频道速递与每日回执（2026-10-20 起）

管线除五份 Markdown 外还有两个出口：

- **Telegram 频道** `Tokenation Daily` / `@tokenationz`（chat_id `-1004335659711`）。由独立 job `77d6b856f1f0` 驱动：`no_agent=true`，`*/20 20-22 * * *`（UTC），脚本 `scripts/notify_channel.py --require-fresh --quiet`，不经过 LLM，不靠模型排版。
  - 新鲜度闸门：DB `max(last_verified)` 必须等于今日 UTC，且 `origin/main` 最后一次提交日期等于今日。两条都给不出结论时按 DB 放行。不满足就静默退出，不得用旧数据冒充今日。
  - 幂等：`/opt/data/tokenation/channel_state.json` 按 `last_post_date` 去重，同日只发一次。
  - 版式由脚本持有（标题 `YYYYMMDD 速递（UTC）`、`新增 N` / `即将到期 N` 两段、条目行 `  provider｜模型 — 一句描述` 两空格缩进）。改版式只改脚本，不在 prompt 里描述。
- **每日回执**（唯一进入聊天的内容）：成功 `[Tokenation] 管线执行成功，时间：{YYYY-MM-DD HH:mm:ss}`，失败把「成功」换成「失败」，其余一字不改。时间用 `date -u` 现取，不用模型推算。不加统计、不加 emoji、不加空行、不用 `[SILENT]`。

## 署名


提交身份必须是 `precisionz <62896761+precisionz@users.noreply.github.com>`。全局配置是 `Joe Z. <joe@hermes-agent.com>`，所以每条提交都要显式指定身份或先设仓库级配置，否则会把真实姓名再次写进公开历史：

```bash
git -c user.name=precisionz -c user.email=62896761+precisionz@users.noreply.github.com commit -m "docs: refresh free LLM offers"
```

已在远程公开的 4 个提交仍带 `Joe Z.`，只有改写历史加 force push 才能清除，需 Joe 单独授权。默认不改历史，但不得再新增带姓名的提交。

## 已知坑

- **批量导入会静默改写人工判定，`upsert` 必须带 `coverage_guard`。** 2026-10-19 首次跑 `import-competitors` 时，`upsert` 的保护条件只写了"tracked/verified 不许降为 candidate"，结果 `merged`、`blocked` 的行被目录重新贴成 `candidate`/`out_of_scope`：cerebras（tracked→candidate）、novita-ai 与 fireworks-ai（merged→out_of_scope）、siliconflow（blocked→candidate）。已按不变量修复（`in_offers=1 → tracked`、`notes 含 "merged into" → merged`、`notes 含 "待人工核实/JS 壳" → blocked`），并给 upsert 加了 `coverage_guard`。**任何新的批量导入都要先 `--dry-run` 并核对 coverage 分布变化。**
- **两个目录对同一 provider 的判定冲突时，重复导入会来回翻转。** 先跑 A 后跑 B 与先跑 B 后跑 A 得到不同 coverage。已改成与顺序无关：`candidate` 不得降为 `out_of_scope`，`out_of_scope` 可升为 `candidate` → candidate 永远胜出。**改这类规则时必须跑「两种顺序 → 同一快照」验证。**
- **竞品目录的分类不可信，只可信它的"名单"。** Cerebras / HuggingFace / OpenCode Zen 三条都被它们标错（见「发现面」节）。判断一条 offer 合不合我们的框架，只能回官方页。
- **免费额度页的抓取成功率要按页面形态预估。** 2026-10-19 实测 14 个候选页：`alibaba` 56K、`ovh` 84K、`vercel` 49K、`opencode-zen` 30K 可读；`llm7.io` 只回 Cloudflare 壳（0 字节）、`modelscope` 超时（0 字节）、`hetzner` 是 SPA loader（moli 0 / obscura 1.9K）。**这三类必须先判 blocked，不许拿竞品数字顶替。**
- **`grep` 大页面会被内嵌 JSON 淹没。** 阿里云 help 页把整站导航和 footer 序列化进页面里（56K 里大半是 JSON），宽泛的 `grep -i free` 会刷出几千字符无用内容。按具体行号或 `-m` 限量读，别做无界 grep。
- **发现面漏一个域名，整类 offer 就消失。** 2026-10-19 AutoClaw 案例：库里有「智谱」，但核实页是 `open.bigmodel.cn`（开放平台首页），活动发在 `autoclaw.z.ai/blog/news/`（英文站）/ `autoclaw.zhipuai.cn/blog/news/`（中文站）。pagewatch 天天老实抓开放平台首页，永远不会出现客户端活动。看到"某厂商明明有活动却没收录"时，先查它有几个产品面、核实页挂在哪个面，再谈判定规则。
- **`export` 丢字段 = 下一次 `sync` 悄悄抹掉它。** `export_records` 曾经不输出 `source_url` 与 `homepage`，于是"导出→回灌"的往返会把核实页重置成注册链接、把公告索引页清空，pagewatch 从此盯着 console 页并永久 stale。任何新增字段都要同时进 `export`，并用「export → 原样 sync → 零合并、零变化」验收。
- **"剩余超7天"在剩余 ≤7 天时是假话。** 剩余天数下限取消后，日期型条目可以只剩几天；渲染器已改成剩余 ≤7 天时输出 `截止日（剩余 N 天）` / `(in N days)`，校验器同步接受这种带数字的日期后缀。改这个 label 时两个地方都要动，否则 `render_check` 会把正常输出判成错误。
- **五段式 emoji 已随旧格式一起废弃**（2026-10-20 改表格）：`🏷️⏰⚡🤖🔗🎁` 出现在任何清单或 README 里都会被校验器判为错误。校验器同时整文件拦英文版里的 CJK 字符。
- 历史清除已用 `git filter-branch` + `--force-with-lease` 完成，全历史作者均为 precisionz。GitHub API 按旧 SHA 查仍会返回旧姓名，那是服务端孤儿对象，不在任何分支上。
- `cn/`、`en/` 目录里放的是 `EVERGREEN.md` / `LIMIT-TIME.md` 而不是 `README.md`，所以两个目录不会自动渲染说明页，只能用直链访问（Joe 定的文件名）。
- 状态库 `tokenation.db` 必须放仓库外（默认 `/opt/data/tokenation/`）。它是二进制文件，一旦进仓库就会同时违反"只发 Markdown"和"无结构化数据"两条禁令。
- 本地有 `.gitignore`（未跟踪，忽略 `AGENT.md`、`PLAN_*.md`、`tooling/`、`scripts/`、`tests/`、`*.db`、`.state/`、`__pycache__/`），远端根目录只有 `LICENSE`、`README.md`、`cn/`、`en/`。`gh` 未登录，推送走 HTTPS 凭据；`git push` 要求输入用户名/密码即缺少凭据，停止并报告，不要重试。
- **登录墙会被判成「已核实」，除非 URL 层就把它挡掉。** 2026-10-20 之前 `MIN_CHARS = 200`，6 个 console 页（Cloudflare 244、Cohere 335、Mistral 433、SiliconFlow 441、Groq 671、Google AI Studio 1610 字符）每天照常判 `unchanged`，`mark` 把 `last_verified` 推到今天，抓到的是登录墙而不是额度。已修：阈值提到 1500，console/登录页直接判 `unverifiable`，并把 6 个 `source_url` 换成定价页或文档页（Cloudflare → `developers.cloudflare.com/workers-ai/platform/pricing/`、Cohere → `docs.cohere.com/docs/rate-limits`、Google → `ai.google.dev/gemini-api/docs/rate-limits`、Groq → `console.groq.com/docs/rate-limits`、Mistral → `mistral.ai/pricing`、SiliconFlow → `siliconflow.com/pricing`）。判断一个页面能不能当证据，先问「它会不会因为没登录而永远是同一段 HTML」。
- 大文件分次写入：不要一次性构造超长字符串再写盘，改由渲染器从状态库生成。
