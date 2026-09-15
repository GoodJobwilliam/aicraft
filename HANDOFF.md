# HANDOFF CONTEXT (updated 2026-09-15 CST)

## 2026-09-15（收入主线 round 132）
- 向 AgentsKit code-review #137 发布 1 条纯技术评论，讨论确定性 evidence envelope、逐 hunk 覆盖状态、去重指纹和 unavailable 证据的选择性重试：[issue comment](https://github.com/AgentsKit-io/code-review/issues/137#issuecomment-5673266802)。目前无维护者直接回复，未分享试用链接或收费信息。
- 真实触达从 17 增至 18；qualified replies、team tests、paid signals、pre-commitments、one-time revenue 和 MRR 仍全部为 0。Docker MCP Registry #4699 的文案修正仍是分发审核，不计为 contact。

## 2026-09-15（收入主线 round 131）
- 修正 Docker MCP Registry PR [#4699](https://github.com/docker/mcp-registry/pull/4699) 的过时产品描述：移除未被当前版本证明的 OWASP 全覆盖、AI-powered、漏洞/N+1/性能 profiling 表述，改为本地确定性模式检查、结构化 finding、CI 退出码、PyPI 0.1.2 和版本化免费试用入口；PR 仍 open，等待 Registry 审核。
- 该 PR 元数据更新属于分发审核，不计为新的 contact；`OUTREACH_LOG.csv` 的真实漏斗仍为 17 contacts / 0 qualified replies / 0 team tests / 0 paid signals / 0 pre-commitments / $0 one-time revenue / $0 MRR。未新增付费支出。

## 2026-09-15（收入主线 round 130）
- 重新核验最近三条外部技术评论：agents-shipgate #623、NetworKit #1471 和 fullsend-ai/agents #1216；前两条线程虽有维护者背景评论，但均早于 AICraft 的评论，尚无针对 AICraft 的直接回复，第三条仍无维护者评论。未发送重复跟进、未分享试用链接、未新增联系人或商业漏斗记录。
- 公开 team-trial / trial-feedback issue 仍为 0；当前真实漏斗保持 17 contacts / 0 qualified replies / 0 team tests / 0 paid signals / 0 pre-commitments / $0 one-time revenue / $0 MRR。

## 2026-09-15（收入主线 round 129）
- 刷新 GitHub Release mcp-code-review-0.1.2 的公开资产：当前试用包为 5,771 bytes、源码包为 91,966 bytes；旧副本保留为 mcp-code-review-trial-legacy.zip 与 mcp-code-review-legacy.zip，避免破坏历史下载引用。
- 公开下载 URL 已复核：两个 canonical ZIP 均 HTTP 成功，unzip -tq 通过，下载后 SHA-256 与本地一致：试用包 9908060e9bb53ffa1c80d3e0bf65b120cd77ed6c6e4fdaeacd0bd0534089d858，源码包 01c2f404f680dcf40109cb9cf923520697a75f323959810377eaa4dcd32f46b4。
- Release 说明已同步当前哈希并明确下载量不计入联系人、试用、客户或收入；本轮未新增付费支出，真实漏斗仍为 17 contacts / 0 qualified replies / 0 team tests / 0 paid signals / 0 pre-commitments / $0 one-time revenue / $0 MRR。

## 2026-09-15（收入主线 round 128）
- 收尾核验：`PYTHONPATH=. pytest -q` 55 passed，`git diff --check` 通过；官网首页与试用页均 HTTP 200，公开 PyPI 版本仍为 `0.1.2`。
- 当前真实漏斗：17 contacts / 0 qualified replies / 0 team tests / 0 paid signals / 0 pre-commitments / $0 one-time revenue / $0 MRR。下载量、评论和公开 issue 互动均不计入收入。
- 本轮向 `ThreeMoonsLab/agents-shipgate#623`、`networkit/networkit#1471` 与 `fullsend-ai/agents#1216` 发布纯技术评论；三处均等待维护者回复，不发送重复跟进，不分享付费报价。
- 本地审计记录已提交为 `5cc5ae2`，并通过 Git Data API 同步到远端 `main`，远端 commit 为 `8797a8e3dd0b8cd22f6dc6b1dbdf9355e9c4a592`。未跟踪的 `.github/workflows/ci.yml` 与 `assets/*` 用户文件保持不动。
- 官方 MCP Registry 条目仍为 `active`、版本 `0.1.2`；本地准确 `server.json` 的官方发布接口拒绝重复版本，编辑接口返回 `403`（当前 token 没有 edit permission），因此远端旧描述未被伪称为已更新。
- 降低反馈门槛：英文/中文 `trial-feedback` 表单现在只要求三项核心技术观察，团队规模、语言、发现来源和商业资格字段均可留空；团队试用申请仍保留完整资格字段。回归测试 `56 passed`，提交 `b50dbdb` 已通过 Git Data API 同步到远端 `4af2a076cd1dc36c42faaa771744e80eb3dc894d`。
- 进一步降低反馈门槛：`trial-feedback` 的“下一步”选择也改为可选，技术反馈不再要求用户先做商业决策；英文/中文 YAML 均通过解析，回归测试仍为 `56 passed`。
- 产品可靠性修正：`review-diff` 现在解析 unified diff hunk 的新文件起始行，将 finding 映射到 Pull Request 中的真实行号；英文/中文 README、CHANGELOG、回归测试和 `products/mcp-code-review.zip` 已同步。根测试 `56 passed`、MCP 产品测试 `50 passed`、Ruff 通过；该改动尚未进入公开 PyPI `0.1.2`。

## 2026-09-14（收入主线 round 123）
- 收尾核验：`PYTHONPATH=. pytest -q` 54 passed，`git diff --check` 通过；首页、中文首页、试用页和 Team Updates 页均 HTTP 200。
- 当前公开分发快照：PyPI 最近 1/7/30 天为 2/33/352，GitHub Release 两个资产下载量均为 0；这些数字仍只作分发信号，不进入收入漏斗。
- 真实漏斗仍为 1 contact / 0 qualified replies / 0 team tests / 0 paid signals / $0 MRR；A9 无维护者回复，A2 未获发送确认；未发送外部评论、未新增付费支出。

## 2026-09-14（收入主线 round 122）
- 根 README 新增只读分发审计命令 `python3 scripts/distribution_report.py` 及“下载量不等于联系人、客户或收入”的说明；新增回归断言。
- `PYTHONPATH=. pytest -q`：54 passed，`git diff --check` 通过；未发送外部评论、未新增付费支出，真实漏斗仍为 1 contact / 0 qualified replies / 0 team tests / 0 paid signals / $0 MRR。

## 2026-09-14（收入主线 round 121）
- GitHub Release `mcp-code-review-0.1.2` 说明已补充两个资产的直接下载链接和 SHA-256：试用包 `6e33ea89dbdd8cc9742c461678ab180aebaa2cfc75d539bb2dde8e8a4b51a052`，源码包 `7f5bebd7b9d428e0796002a600766c63427744f81c8133934b025aaa0778fa1e`。
- A9 仍只有 GoodJobwilliam 的一条评论，维护者没有回复；A2 仍未获用户明确发送确认，因此没有发布任何新的外部评论。
- 未新增付费支出；公开分发与产品测试状态不改变，真实漏斗仍为 1 contact / 0 qualified replies / 0 team tests / 0 paid signals / $0 MRR。

## 2026-09-14（收入主线 round 120）
- 首页生产核验完成：`https://aicraft.vip/` 与 `/zh.html` 均 HTTP 200，英文出现 `Release downloads`，中文出现 `版本下载`；远端 `main` 为 `61261d8...`。
- `PYTHONPATH=. pytest -q`：54 passed。GitHub Release 资产下载量仍为 0；PyPI Stats 最近一次成功快照仍是 2 / 33 / 352（1 日 / 7 日 / 30 日），随后请求被 API 429 限流，未把限流当作数据变化。
- 当前真实漏斗仍为 1 contact / 0 qualified replies / 0 team tests / 0 paid signals / $0 MRR；未发送外部评论、未新增付费支出。A2 仍需用户明确确认后才能发布。

## 2026-09-14（收入主线 round 119）
- 中英文首页 MCP 产品卡新增版本化 GitHub Release 下载入口，连接免费试用包和源码包；新增回归断言，`PYTHONPATH=. pytest -q`：54 passed，`git diff --check` 通过。
- 本地改动尚未同步到 Pages，当前线上首页仍 HTTP 200 但还未出现该新按钮；待 Git Data API 同步后再复核，不把本地结果当作生产结果。
- 未发送外部评论、未新增付费支出；漏斗仍为 1 contact / 0 qualified replies / 0 team tests / 0 paid signals / $0 MRR。

## 2026-09-14（收入主线 round 118）
- 新增只读 `scripts/distribution_report.py`：汇总 PyPI 最近 1/7/30 天下载量和 GitHub Release 资产下载量，并明确声明下载量不是联系人、试用、客户或收入；新增 2 条回归测试。
- 测试结果：`PYTHONPATH=. pytest -q` 54 passed，`git diff --check` 通过。PyPI Stats curl 当前返回 `last_day=2`、`last_week=33`、`last_month=352`；GitHub Release 两个资产当前下载量均为 0。脚本直连 PyPI Stats 遇到临时 429，已改为清晰错误而非 traceback。
- 未发送外部评论、未新增付费支出；真实漏斗仍为 1 contact / 0 qualified replies / 0 team tests / 0 paid signals / $0 MRR。

## 2026-09-14（收入主线 round 117）
- 将根 README 与产品中英文 README 接入版本化 GitHub Release 下载入口；归档回归发现 `products/mcp-code-review.zip` 旧于 README，已按精确清单重建并替换 Release 同名资产。当前产品 ZIP SHA-256：`7f5bebd7b9d428e0796002a600766c63427744f81c8133934b025aaa0778fa1e`，Release 资产大小 89,374 bytes。
- `PYTHONPATH=. pytest -q`：52 passed，归档校验与 `git diff --check` 通过。GitHub Release API 显示试用包和源码包均存在；直接下载仍受当前 github.com 网络超时影响，未把下载超时误记为成功。
- 未发送外部评论、未新增付费支出；漏斗仍为 1 contact / 0 qualified replies / 0 team tests / 0 paid signals / $0 MRR。

## 2026-09-14（收入主线 round 116）
- 创建了公开 GitHub Release `mcp-code-review-0.1.2`（无付费、非预售）：上传 `mcp-code-review-trial.zip`（5,374 bytes）和 `mcp-code-review.zip`（89,169 bytes），两个 ZIP 均已通过 `unzip -tq`，可作为版本化免费分发入口。
- 中英文试用页新增 GitHub Release 链接，并通过回归测试；`PYTHONPATH=. pytest -q`：52 passed，`git diff --check` 通过。
- 未发送外部评论、未新增付费支出；漏斗仍为 1 contact / 0 qualified replies / 0 team tests / 0 paid signals / $0 MRR。

## 2026-09-14（收入主线 round 115）
- 生产验证完成：`https://aicraft.vip/trial.html` 与 `/trial.zh.html` 均 HTTP 200，线上页面已包含试用反馈邮件中的 offer tier、决策角色和目标开始月份字段；远端 `main` 为 `33faa989153fe0c21e724a810df00651ca2c8c22`。
- 当前真实漏斗仍为 1 contact / 0 qualified replies / 0 team tests / 0 paid signals / $0 MRR；未发送外部消息、未新增付费支出。

## 2026-09-14（收入主线 round 114）
- 将中英文试用页的反馈/团队邮件模板与 Issue Form 对齐：试用结果邮件现在也收集 offer tier、决策角色、决策时间、目标开始月份和有条件承诺，避免最接近转化的反馈无法进入资格化流程。
- 新增回归测试，`PYTHONPATH=. pytest -q`：52 passed；`git diff --check` 通过。仅修改网站入口，不涉及试用 ZIP。
- 未发送外部消息、未新增付费支出；公开 trial/feedback issues 仍为 0，漏斗仍为 1 contact / 0 tests / 0 paid signals / $0 MRR。

## 2026-09-14（收入主线 round 113）
- 通过 GitHub 公共 API 重新核验候选外联：A2 `sdempsay/agentic-review-tool#5` 仍 open、0 comments；A13 `trailhq/Graft#368` 仍 open、0 comments；A14 `microsoft/finops-toolkit#2274` 仍 open、1 条微软机器人确认。
- A2 与产品的 MCP stdio / 稳定结果契约最贴合，保留为下一条候选；A13/A14 继续排队。未发送任何评论，未新增联系人或收入，等待用户对具体草稿明确确认。

## 2026-09-14（收入主线 round 112）
- 将首页、中文首页和中英文 Team Updates 页的邮件申请模板与团队试用表单对齐：新增痛点、offer tier、决策角色、决策时间、目标开始月份和有条件承诺字段，降低私下邮件线索无法资格化的风险。
- 新增页面回归测试，`PYTHONPATH=. pytest -q`：51 passed；`git diff --check` 和 `sh -n products/mcp-code-review/trial/run-trial.sh` 通过。
- 未发送外部消息、未新增付费支出；公开 trial/feedback issues 仍为 0，漏斗仍为 1 contact / 0 tests / $0 MRR。

## 2026-09-14（收入主线 round 111）
- 重新通过 GitHub 公共 API 核验 A9（picatz/flowstate#1584）：issue 仍 open，评论仍只有 GoodJobwilliam 于 2026-09-13 发布的技术评论，维护者尚未回复；保持等待，不发送重复跟进。
- 独立试用包解压后实跑成功：输出 High command injection 与 Medium team-convention，预期退出码为 1；`products/mcp-code-review-trial.zip` 与源码脚本 SHA-256 一致，产品 ZIP 归档校验通过。
- 线上 `https://aicraft.vip/`、`/trial.html`、`/team-updates.html` 和试用 ZIP 均 HTTP 200；`PYTHONPATH=. pytest -q`：50 passed。
- 当前真实漏斗仍为 1 contact / 0 tests / $0 MRR；未发送外部消息、未新增付费支出。Team Updates recurring checkout 尚未自动化，继续只通过范围确认后的人工流程推进。

## 2026-09-14（收入主线 round 110）
- 只读试用报告现在校验 target-start-month：只接受真实日历月份的 YYYY-MM，缺失或非法值会分别标记 missing/invalid，不会被误当作合格的开始承诺。
- 跟进手册同步要求有效 YYYY-MM；新增回归测试，PYTHONPATH=. pytest -q：50 passed。公开 trial/feedback issues 仍为 0，漏斗仍为 1 contact / 0 tests / $0 MRR；未发送外部消息、未新增付费支出。

## 2026-09-14（收入主线 round 109）
- 中英文 team-trial 与 trial-feedback 表单新增必填 target-start-month（YYYY-MM），补齐“有条件承诺”所需的明确目标开始月份；只读报告现在显示该字段。
- 新增回归测试，PYTHONPATH=. pytest -q：49 passed；公开 trial/feedback issues 仍为 0，漏斗仍为 1 contact / 0 tests / $0 MRR。未发送外部消息、未新增付费支出。

## 2026-09-14（收入主线 round 108）
- 中英文 trial-feedback Issue Form 新增必填 decision-role 字段，区分购买决策者、推荐者、实际测试工程师和纯调研者；只读报告现在会输出该字段，便于优先跟进可决策线索。
- 新增回归测试，PYTHONPATH=. pytest -q：48 passed；未发送外部消息、未新增付费支出，当前公开 trial/feedback issues 仍为 0，漏斗仍为 1 contact / 0 tests / $0 MRR。

## 2026-09-14（收入主线 round 107）
- 审计官方 MCP Registry：现有 0.1.2 条目仍为 active，但公开描述仍是历史性的 “OWASP security scanning”；当前环境无法安装 mcp-publisher，因此未冒险修改或伪称已更新 Registry。
- 修正首页和社交文案，把 MCP 主产品能力统一为 deterministic security-pattern checks；新增回归断言，避免重新出现 OWASP Top 10 扫描承诺。
- 由于中文产品 README 更新，重建并同步免费 mcp-code-review.zip；线上 ZIP HTTP 200 且归档内容与源码一致。
- PYTHONPATH=. pytest -q：47 passed；未发送外部消息、未新增付费支出，漏斗仍为 1 contact / 0 tests / $0 MRR。

## 2026-09-14（收入主线 round 106）
- 将英文和中文试用页首屏主按钮改为直接下载独立试用包，保留团队方案按钮；新增回归测试，确保首屏 CTA 与可下载 ZIP 一致。
- GitHub main 已同步提交 4b704568c4a88f87bf5997464dc6cc1d83d70876；生产环境两种语言页面均呈现新 CTA，试用 ZIP 返回 HTTP 200 且 unzip 校验通过。
- PYTHONPATH=. pytest -q：45 passed；未发送外部消息、未新增付费支出，漏斗仍为 1 contact / 0 tests / $0 MRR。

## 2026-09-14（收入主线 round 105）
- 将中英文自助试用页的三步顺序调整为“下载试用文件 → 运行示例审查 → 试试自己的规则”，修复首次访问者先运行 \`sample.py\` 但尚未取得示例文件的转化摩擦；新增回归断言确保顺序不会回退。
- 生产环境 \`https://aicraft.vip/trial.html\` 与 \`/trial.zh.html\` 均返回 HTTP 200；远端页面当前仍是旧顺序，待本地提交通过 GitHub API 同步后再复核。
- \`PYTHONPATH=. pytest -q\`：44 passed；试用/安装定向测试：21 passed；\`git diff --check\` 通过。未发送外部消息、未新增付费支出，漏斗仍为 1 contact / 0 tests / \`$0 MRR\`。

## CURRENT STATE
- **目标**: aicraft 达到 $2,000 MRR；预算 $0；工作区 `/Users/william/work/AIcompany/aicraft`
- **策略更新（2026-08-30）**: 聚焦 `mcp-code-review` 主线；免费开源 server + $49 Team Rules Pack + Team Updates 早期体验（$19/月或 $190/年）。不新增任何付费工具、广告或基础设施。
- **本轮已完成**: 英文/中文首页首屏收敛到 MCP Code Review；新增 `team-updates.html` / `team-updates.zh.html`；新增预售说明、价格、邮件收集入口和中英文 GitHub team-trial Issue Forms（使用仓库已有 `question` 标签和标题前缀，避免依赖额外权限）；仓库禁用空白 issue 并提供文档/早期体验联系入口；中英文产品 README 也接入对应试用表单和 10 分钟自助试用包；README、发布指南、市场提交信息和社交草稿同步 Team Updates 口径；新增 `OUTREACH_LOG.md`；新增同域名中英文自助试用页 `trial.html` / `trial.zh.html`，首页与 Team Updates CTA 已切换，sitemap 已收录。漏斗报告现在还会输出 `$2,000 MRR` 剩余缺口和按 Starter/Team Pilot 价格计算的新增客户数；本轮还修复了试用页首条命令未直接执行审查的断链，并重建两个 MCP ZIP。
- **本轮已完成**: 英文/中文首页首屏收敛到 MCP Code Review；新增 `team-updates.html` / `team-updates.zh.html`；新增预售说明、价格、邮件收集入口和中英文 GitHub team-trial Issue Forms（使用仓库已有 `question` 标签和标题前缀，避免依赖额外权限）；仓库禁用空白 issue 并提供文档/早期体验联系入口；中英文产品 README 也接入对应试用表单和 10 分钟自助试用包；README、发布指南、市场提交信息和社交草稿同步 Team Updates 口径；新增 `OUTREACH_LOG.md`；新增同域名中英文自助试用页 `trial.html` / `trial.zh.html`，首页与 Team Updates CTA 已切换，sitemap 已收录。漏斗报告现在还会输出 `$2,000 MRR` 剩余缺口和按 Starter/Team Pilot 价格计算的新增客户数；本轮还修复了试用页首条命令未直接执行审查的断链、补充了下载顺序提示，并重建两个 MCP ZIP。
- **本轮已完成**: 英文/中文首页首屏收敛到 MCP Code Review；新增 `team-updates.html` / `team-updates.zh.html`；新增预售说明、价格、邮件收集入口和中英文 GitHub team-trial Issue Forms（使用仓库已有 `question` 标签和标题前缀，避免依赖额外权限）；仓库禁用空白 issue 并提供文档/早期体验联系入口；中英文产品 README 也接入对应试用表单和 10 分钟自助试用包；README、发布指南、市场提交信息和社交草稿同步 Team Updates 口径；新增 `OUTREACH_LOG.md`；新增同域名中英文自助试用页 `trial.html` / `trial.zh.html`，首页与 Team Updates CTA 已切换，sitemap 已收录。漏斗报告现在还会输出 `$2,000 MRR` 剩余缺口、按 Starter/Team Pilot 价格计算的新增客户数和按日期标记的跟进队列；本轮还修复了试用页首条命令未直接执行审查的断链、补充了下载顺序提示，并重建两个 MCP ZIP。
- **本轮已完成**: 英文/中文首页首屏收敛到 MCP Code Review；新增 `team-updates.html` / `team-updates.zh.html`；新增预售说明、价格、邮件收集入口和中英文 GitHub team-trial Issue Forms（使用仓库已有 `question` 标签和标题前缀，避免依赖额外权限）；仓库禁用空白 issue 并提供文档/早期体验联系入口；中英文产品 README 也接入对应试用表单和 10 分钟自助试用包；README、发布指南、市场提交信息和社交草稿同步 Team Updates 口径；新增 `OUTREACH_LOG.md`；新增同域名中英文自助试用页 `trial.html` / `trial.zh.html`，首页与 Team Updates CTA 已切换，sitemap 已收录。漏斗报告现在还会输出 `$2,000 MRR` 剩余缺口、按 Starter/Team Pilot 价格计算的新增客户数和按日期标记的跟进队列；本轮还修复了试用页首条命令未直接执行审查的断链、补充了下载顺序提示和一键下载/运行命令，并重建两个 MCP ZIP。
- **新增分发资产**: `OUTREACH_PACK.md`（中英文短帖、私信模板、资格问题和以付费承诺为准的验证标准）、`OUTREACH_TARGETS.md`（20 个公开 GitHub 候选项目和技术切入点）、`TRIAL_FOLLOWUP_PLAYBOOK.md`（人工跟进、证据阈值和收入统计口径）以及 `OUTREACH_LOG.csv` + `scripts/funnel_report.py`（可重复的漏斗统计）。
- **Website**: https://aicraft.vip (EN) + /zh.html (CN) — live；新增 `/trial.html` 与 `/trial.zh.html` 自助试用页，生产环境已返回 200。首页示例报告区展示 Team Rules Pack 真实输出（`MCP_CODE_REVIEW_CONFIG=rules/python.yaml mcp-code-review review-file main.py`，3 Critical / 5 High / Block，exit 2）并直链 Creem $49 结算页（本轮 commit `b5ae2b7`）
- **Creem**: 9 产品 live，**0 销售 / 0 订阅 / 0 客户**（漏斗复查：2026-09-13）。账号 731685147@qq.com。增值产品 Team Rules Pack `prod_6Z3S3jGNPsCyRSqNi397ZY`（63 条规则 + CI playbook + LLM prompts，$49）
- **GitHub**: GoodJobwilliam/aicraft，2 stars / 0 forks。⚠️ github.com 直连被墙（api.github.com 可达）→ **推送必须走 API**（recipe 见 TOOLING NOTES）。OAuth token 无 `workflow` scope → `.github/workflows/ci.yml` 和 MCP Trusted Publishing workflow 无法推送；后者已在本地验证，但远端 workflow API 当前只显示 Pages 部署。
- **登录状态（in-app browser, CDP 9229）**: Google ✅ / GitHub ✅ / Smithery ✅ / Glama ✅ / Creem ✅（QQ 账号）/ IH ✅（Firebase，但 Firestore 被墙不可用）。⚠️ Product Hunt 会话已过期（需重新登录）；PyPI / V2EX / 掘金 未登录——**登录页标签已开好**（PyPI=E60305F8、V2EX=76D6EA55、掘金=BC42B4FB）
- **网络**: github.com、googleapis.com（Firestore/identitytoolkit）不通——**用户 VPN（MotionPro 同济 vpn.tongji.cn）当前断开**。其余（PyPI/PH/Glama/Dev.to/Smithery/Creem/mcpservers）均可达
- **PyPI 0.1.2 live**: package metadata now pins `mcp>=1.6,<2`; public install path and docs are aligned. A local 0.1.2 release-candidate build passes the full product suite (49 tests), lint, and wheel/sdist schema-content checks; publishing 0.1.3 still requires PyPI credentials or the remote Trusted Publishing workflow.

## LAUNCH STATUS (2026-08-17)

| Platform | Status | Notes |
|----------|--------|-------|
| **Smithery.ai** | ✅ Live | [yaohuixue1/mcp-code-review](https://smithery.ai/servers/yaohuixue1/mcp-code-review) 52/100。Arcade 迁移后 redeploy 通道坏（UI Publish 无反应，API POST /releases 404）。验证需付费计划 |
| **mcpservers.org** | ✅ Live | APPROVED: [goodjobwilliam/aicraft](https://mcpservers.org/servers/goodjobwilliam/aicraft)，已用于 backlinks |
| **cursor.directory** | ✅ Live | [mcp-code-review-server](https://cursor.directory/plugins/mcp-code-review-server) 公开（1 Rule + 1 MCP Server） |
| **PyPI** | ✅ 0.1.2 live | Public package metadata pins `mcp<2`; install path verified against the live release. |
| **Product Hunt** | ✅ Launched | 3 upvotes / 12 followers / 7 comments（外部 5 条全部回复 + 2 条 maker 回复）。论坛帖 approved。⚠️ 浏览器会话已过期，需重新登录才能继续互动 |
| **Dev.to** | ✅ 5 篇文章 | [主页](https://dev.to/goodjobwilliam)。文章 5（id 4408698, 63 规则）0 反应。发布 API 凭据不记录在仓库；如历史凭据仍有效，必须在 Dev.to 侧轮换。总 30 views（历史复查） |
| **PitchHut** | ✅ Claimed | 47 page views, 0 pitch clicks。账号 cheap_copper_rodie |
| **Glama** | ⏳ 审核队列中 | 提交确认在队列（"A submission for this repository is already pending review"）。工单 **#125096481**（Fin bot 回复过）。GitHub OAuth 连接 bug（授权成功但设置页 Not connected，48h 重试）。仍未收录（2026-08-17 复查）→ 收录后 claim + badge + 更新 PR #10918 |
| **awesome-mcp-servers** | ⏳ PR open | [#10918](https://github.com/punkpeye/awesome-mcp-servers/pull/10918) open/clean/4 comments，无维护者新回复。只差 Glama 收录+徽章 |
| **MCPFind** | ⏳ PR open | [#139](https://github.com/MCPFind/mcp-find/pull/139) open/unstable/1 comment |
| **Cline MCP Marketplace** | ❌ Issue closed | #2106 已被维护者关闭（2025-12-30），不再追 |
| **Official MCP Registry** | ✅ Active | `io.github.GoodJobwilliam/aicraft-code-review` version `0.1.2` is active in the public API; no republish needed. |
| **Hacker News** | ✅ 1 point | Item #49058442，0 comments，dormant |
| **Reddit r/mcp** | ⚠️ 限流中 | 两帖被 spam 过滤（1v76tt5/1v9xgip）。账号级 blocked，punkpeye 未回复 mod queue 请求。已在攒 karma：4 条技术评论（r/mcp×3 + r/ClaudeAI×1）。等待账号成熟后 clean repost |
| **mcp.so** | ❌ $39 付费 | $0 预算跳过 |
| **Indie Hackers** | ✅ Live | [mcp-code-review](https://www.indiehackers.com/product/mcp-code-review) approved（4 gates 绿），1 like。⚠️ Firestore 帖文库被墙（VPN 断开），本周无法发新帖/清理 UNPUBLISHED DRAFT |
| **Docker MCP Registry** | ⏳ PR open | [#4699](https://github.com/docker/mcp-registry/pull/4699) open，无 CI/评论。root Dockerfile + LICENSE + SECURITY.md 已就位 |
| **PulseMCP** | ⏳ Paused | 仍暂停，等官方 Registry 收录后自动 pickup |
| **ai-bot.cn** | 🕐 待审 | 飞书问卷已提交（2026-08-16）。2026-08-17 搜索无收录，等待通知邮件 |
| **V2EX / 掘金** | 🕐 草稿就绪 | 草稿 `/tmp/v2ex_post.md`、`/tmp/juejin_article.md`（已指向 zh.html），登录页已开好等用户登录 |

## RECENT CODE CHANGES
- **Landing demo report**（remote 1fb9ff7）: index.html + zh.html 示例报告区换成 Team Rules Pack 真实输出（3 Critical/5 High/Block, exit 2），直链 Creem $49 结算页。已验证上线
- **Custom Rules & Team Profiles**（f0c0b40）: `config.py` ReviewConfig/CustomRule/load_config（向上自动发现 `.mcp-code-review.yaml|yml|json` + `MCP_CODE_REVIEW_CONFIG` 环境变量）；16 个 check id；33 测试全过
- **CLI 直跑模式**（fff7cda）: `mcp-code-review review-file PATH` / `review-diff [--git]` / `review-code CODE`；退出码 0 clean/1 high-medium/2 critical
- **Team Rules Pack**（1fbfda2）: products/mcp-code-review-rules-pack/（63 规则：Python 21/JS·TS 16/Go 13/Java 13；ci/github-actions.yml + ci/gitlab-ci.yml；llm-prompts.md 20 条）全部经 ReviewConfig.from_dict + 正则编译 + 真实 CLI 验证
- **mcp pin fix**（2940d6e）: pyproject `mcp>=1.6,<2`；root Dockerfile/LICENSE/SECURITY.md
- **SEO/中文站**（16604f5/933d319）: OG/Twitter/JSON-LD/sitemap/robots；zh.html 中文落地页
- **YAML 示例修复**（2abd0e2）: README regex pattern 单引号
- **Glama Dockerfile**（8dca404）: pinned git commit 安装（防 mcp 2.x）
- **mcp pin fix**（2940d6e，已上线）: package metadata and all install guides use `mcp<2`; the live PyPI 0.1.2 release no longer needs a manual compatibility workaround.
- **待推送（本地）**: `.github/workflows/ci.yml` 与 `.github/workflows/mcp-code-review-release.yml`（需 PAT `workflow` scope，Git Data API 也会 404）

## TOOLING NOTES
- **GitHub 推送（github.com 被墙时的标准流程）**: 走 api.github.com Git Data API——① GET `/git/refs/heads/main` 取 BASE；② POST `/git/blobs`（base64 文件内容）；③ GET `/git/commits/BASE` 取 parent tree，POST `/git/trees`（`base_tree` + 变更文件）；④ POST `/git/commits`（注意：GitHub 会把 date 的时区归一化成 UTC 存盘，本地重建 commit 无法字节对齐——接受 SHA 分歧，本地分支与远端树内容保持一致即可，**不要** git pull/push 覆盖远端）；⑤ PATCH `/git/refs/heads/main`。token 取法: `printf "protocol=https\nhost=github.com\n\n" | git credential fill`（password 行）。⚠️ token 无 workflow scope → `.github/workflows/*` 的 tree POST 返回 404
- **IH (Indie Hackers)**: 账号 aicraftbuilder / yaohuixue1@gmail.com。产品元数据在 **RTDB** `/products/mcp-code-review.json`（REST + idToken，token 缓存在 /tmp/ih_idtoken.json；identitytoolkit 被墙时改用浏览器 IndexedDB 里的 stsTokenManager 直接查）。**帖文（new-post）在 Firestore** `posts` 集合（productId 过滤），REST 需 `firestore.googleapis.com`——当前被墙，**必须 VPN 在线**。RTDB 旧 `posts/` 路径是 legacy，帖文不在那。浏览器 IH 标签经常是 stuck renderer（卡在 loading quote），需关掉重开
- **PH 评论**: GraphQL `CommentUpdate` mutation（需 X-CSRF-Token + csrf_token cookie）；回帖用 action-bar-reply-button + ProseMirror execCommand insertText。PH 会话过期快，用前先检查登录态
- **CDP**: ws://127.0.0.1:9229（/tmp/cdp.py 第一参数 = 完整 ws URL）；新 tab `PUT /json/new?URL` 共享浏览器会话
- **Creem**: dashboard 标签 56042DEA 常驻；产品编辑走 UI
- **Smithery**: API key smry_EtMB... 在 CLI config

## USER ACTIONS NEEDED（按优先级）
1. **官方 MCP Registry 登录/发布**: `mcp-publisher publish` can now use the live 0.1.2 package; this is the highest-leverage free distribution step still pending.
2. **打开 VPN**（MotionPro 同济）: 解锁 github.com 直连、IH Firestore（发帖/清理草稿）、identitytoolkit
3. **V2EX + 掘金登录**: 标签已开好，草稿就绪，登录后立即可发
4. **Product Hunt 重新登录**: 会话已过期，重新登录后可继续评论互动
5. **GitHub PAT（含 workflow scope）**: 解锁 CI workflow 推送

## NEXT STEPS
1. Keep the Official MCP Registry entry current on future releases → Glama 收录后 claim + badge → 更新 awesome PR #10918
2. VPN 恢复后: IH 发新 timeline 更新 + 清理 UNPUBLISHED DRAFT（Firestore 查询法已就绪）
3. V2EX/掘金登录后: 发中文引流帖 → zh.html
4. Glama 工单 #125096481 持续跟进；GitHub OAuth 连接 bug 48h 重试
5. PulseMCP 每周查（等官方 Registry）；MCPFind #139 / Docker #4699 每周查
6. Reddit karma 攒够后 clean repost；PH 重新登录后回复新评论
7. Creem 销售每周复查（当前 $0）；Dev.to 文章 6 选题: Glama badge + registry 收录 roundup

## PATROL LOG

- **2026-09-14（收入主线 round 98）**：通过 GitHub 公共 API 核验新候选 `techie2000/template-docs#61`（Copilot PR review 的 repo-owned skill / MCP context 设计，open、0 comments、2026-09-03 更新），加入 `OUTREACH_QUEUE.md` 和 `OUTREACH_DRAFTS.md` 的 A10；仅准备技术问题，不发送评论、不计联系人或收入，发送前仍需用户明确确认。随后将独立试用包的 `run-trial.sh` 改为优先使用 `uvx`，缺少 `uvx` 时把公开 PyPI `0.1.2` 安装到临时目录并在退出时清理；中英文说明同步，重建两个分发 ZIP，归档/安装测试 `21 passed`。中英文试用页已直接展示 `./run-trial.sh` 和 fallback 说明；live 页面与 live ZIP 核验为当前内容。未发送外部消息、未新增付费支出，漏斗仍为 1 contact / 0 tests / $0 MRR。
- **2026-09-14（收入主线 round 99）**：通过 GitHub 公共 API 核验维护者 `clstaudt` 发起的 NetworKit #1471（open，1 条非维护者评论，记录本地 Qwen 代码审查实验及低 tokens/s 延迟），加入 A12 队列和草稿；建议讨论快速确定性预检如何减少慢模型的搜索范围，保持模型复现/修复验证为权威步骤。未发送评论、未写入联系人漏斗、未新增付费支出。
- **2026-09-14（收入主线 round 101）**：通过 GitHub 公共 API 核验 `trailhq/Graft#368`（active MIT coding-agent 项目，维护者讨论免费 AI PR 首轮审查，open、0 comments，仓库 2026-09-13 有更新），加入 A13 队列和纯技术草稿；未发送公开消息、未计入联系人或收入，等待用户明确确认。
- **2026-09-14（收入主线 round 100）**：中英文试用页新增预填团队资格邮件入口，覆盖 GitHub 表单同等的团队规模、语言、流程、痛点、试用时间、档位和决策字段，并加回归测试；根测试 `39 passed`。未发送外部消息、未新增付费支出，漏斗仍为 1 contact / 0 tests / $0 MRR。

- **2026-09-14（收入主线 round 97）**：将中英文 Team Trial Issue Form 增加必填 `offer-tier` 字段（免费服务器 / Team Rules Pack / Starter / Team Pilot / 范围未清晰），并让只读报告解析新字段；新增回归测试，根测试 `39 passed`。该改动已通过 Git Data API 同步到远端 commit `741f0d7`，使团队试用线索能直接归因到具体 offer；当前仍无真实试用、预承诺或付款。

- **2026-09-14（收入主线 round 96）**：将本地已验证的 MCP Schema、CLI、产品 README、测试、试用包和交接/触达审计文件通过 Git Data API 同步到远端 `main`（commit `2f20164628cb7af8d15b1e612f92c411664078a7`）；未触碰因 token scope 限制而无法写入的 `.github/workflows/*`。复查官网 `mcp-code-review.zip` 和 `mcp-code-review-trial.zip` 均返回 200，产品 ZIP 已包含 `schema/review-result.schema.json`。

- **2026-09-14（收入主线 round 95）**：在干净的临时 Python 3.12 环境中从公开 PyPI 安装 `aicraft-code-review==0.1.2` + `mcp<2`，从官网下载试用样例和 JSON 配置，完成端到端试用：输出 1 High（command injection）+ 1 Medium（team-convention），退出码 `1`。同时确认公开 PyPI `0.1.2` 仍不含 `schema` 子命令（返回 argparse exit `2`），与当前文档口径一致；本地构建包才包含该能力。

- **2026-09-14（收入主线 round 94）**：完成发布候选验证：`uv sync --locked --extra dev --extra yaml`、Ruff、MCP 产品测试 `49 passed`，并确认 wheel/sdist 均包含 `mcp_code_review/schema/review-result.schema.json`。同时修复 Trusted Publishing workflow 的两个真实缺陷：测试未安装 YAML extra，以及将输出目录 .gitignore 误算为第三个 artifact；根测试 `37 passed`。本地修复尚未能同步到 GitHub，因为当前 token 缺少 `workflow` scope；远端 Actions 仍只有 Pages。PyPI 公开版本仍为 0.1.2，未声称 0.1.3 已发布。

- **2026-09-13（收入主线 round 93）**：用户明确确认后，向 `picatz/flowstate#1584` 发布 1 条不带销售链接的技术评论（[issue comment](https://github.com/picatz/flowstate/issues/1584#issuecomment-5654286581)）；真实联系已记录到 `OUTREACH_LOG.csv` 并通过 Git Data API 同步到远端 commit `466855d`。维护者尚未回复，不能计入 qualified reply、试用、意向或收入；当前漏斗为 1 contact / 0 tests / $0 MRR。核验公开 PyPI `0.1.2` wheel 仍不含 bundled schema，因此保留“下一版发布后可用”的文档表述；本地 Trusted Publishing workflow 尚未进入远端 Actions（token 缺少 `workflow` scope）。
- **2026-08-30（收入主线 round 2）**: 统一公开发布指南、市场提交信息、社交草稿与产品 README 到 PyPI 0.1.2；明确免费 MIT server、$49 Team Rules Pack 与尚未自动收费的 Team Updates；新增 `OUTREACH_LOG.md` 记录 20 个零预算定向触达目标；通过官方 Registry API 核实 0.1.2 已为 `active`，并在临时干净环境安装成功。
- **2026-08-30（收入主线 round 3）**: 基于公开 GitHub 搜索整理 `OUTREACH_TARGETS.md`，为 20 个相关项目添加公开信号、技术切入点和合规触达顺序；未发送外部消息。
- **2026-08-30（收入主线 round 4）**: 在临时干净环境安装 PyPI `aicraft-code-review==0.1.2` 并完成 CLI review smoke test；官方 Registry 查询、官网四个页面和两个 Creem 结算链接均返回 200。当前仍无已验证销售或付费预承诺。
- **2026-08-30（收入主线 round 5）**: 新增公开 GitHub Issue Form（团队规模、语言、审查流程、试用时间、持续更新意向），并将中英文 Team Updates 页面 CTA 接入；不收集代码、密钥或私人联系方式。
- **2026-08-30（收入主线 round 6）**: 新增 `.github/ISSUE_TEMPLATE/config.yml` 禁用空白 issue、补充文档/Team Updates 联系入口，并将中英文产品 README 接入结构化试用表单。
- **2026-08-30（收入主线 round 7）**: 新增中文团队试用表单 `team-trial-zh.yml`，中文页面、中文 README 和中文推广文案均已切换到本地化入口。
- **2026-08-30（收入主线 round 8）**: 新增 `products/mcp-code-review/trial/` 自助试用包（示例代码、共享 JSON 规则、10 分钟运行说明和升级路径），并从中英文产品 README 与 Team Updates 页面接入。
- **2026-08-30（收入主线 round 9）**: 运行自助试用包完成冒烟验证：自动发现 JSON 配置，报告 1 个 High + 1 个 Medium，退出码 `1`（预期的 CI 阻断行为）；产品测试继续 `33 passed`。
- **2026-08-30（收入主线 round 10）**: 尝试加入 `.github/workflows/team-trial-intake.yml` 自动回执，但当前 GitHub OAuth token 缺少 `workflow` scope，远端拒绝写入；已删除未推送草稿，不把自动回执算作已上线功能。
- **2026-08-30（收入主线 round 11）**: 将 10 分钟自助试用和中英文 GitHub 团队申请入口直接接入首页 Team Updates 区，减少从访问到验证的跳转。
- **2026-08-30（收入主线 round 12）**: 修正英文首页团队 CTA 的页面级按钮样式，确保自助试用和团队申请入口在首屏之外仍清晰可见。
- **2026-08-30（收入主线 round 13）**: 在中英文团队试用表单加入决策角色与付费决策时间字段，并同步更新 `OUTREACH_LOG.md` / `GTM_NEXT_STEPS.md`；开始按可验证购买时点筛选线索。
- **2026-08-30（收入主线 round 14）**: 修正 GitHub Issue Template 配置中“自动回复”的过时描述，明确当前由维护者在公开 issue 线程人工跟进；未新增任何外部服务。
- **2026-08-30（收入主线 round 15）**: 新增 `TRIAL_FOLLOWUP_PLAYBOOK.md`，定义 24 小时内人工回复、试用复盘、$49/Team Updates 提议时机、付费承诺证据阈值和 $2,000 MRR 统计口径。
- **2026-08-30（收入主线 round 16）**: 修正跟进手册收入数学，仅按当前 Team Updates `$19/月` 和 `$190/年` 月均等价统计 MRR；$49 Team Rules Pack 明确只计一次性收入。
- **2026-08-30（收入主线 round 17）**: 新增标准 CSV 漏斗日志和无依赖报告脚本，空日志明确输出 0；仅确认付款计入收入，付费信号和预承诺单独统计。
- **2026-08-30（收入主线 round 18）**: 因 PyPI 下载统计接口限流，移除首页无法重新核实的下载量、市场数量、文章数量和产品数量，改为展示可直接验证的 PyPI 0.1.2、官方 Registry active、本地运行和 MIT 开源事实；中文页同步更新。
- **2026-08-30（收入主线 round 19）**: 修正根 README 的 Creem/MCP Registry 过时状态；英文/中文首页收录列表补上官方 Registry 链接；历史分发博客显式标注为 2026-08-16 数据快照。
- **2026-08-30（收入主线 round 22）**: 修正 Team Rules Pack Python 规则数（实际 21 条）；从当前交接文档移除 Dev.to API key。该 key 曾出现在历史提交，需在 Dev.to 侧轮换，不能视为已撤销。
- **2026-08-30（收入主线 round 23）**: 全局统一首页、博客、LLM 安装指南和规则包 CI 示例到 PyPI 0.1.2 + `mcp<2`；修正 CI 示例使用当前 CLI 的 stdin diff 形式，避免新装兼容性错误。
- **2026-08-30（收入主线 round 24）**: 将中英文产品 README 的 pip 安装命令也固定到 `aicraft-code-review==0.1.2`，完成所有主要公开安装入口的一致性收口。
- **2026-08-30（收入主线 round 25）**: 为 `scripts/funnel_report.py` 新增 5 个回归测试，覆盖空日志、一次性收入与 MRR 分离、中文状态值、缺列和负数收入校验。
- **2026-08-30（收入主线 round 26）**: 将 Team Rules Pack 的 Creem `$49` 结算链接补入自助试用包、规则包 README 和跟进手册，打通“试用结果 → 购买”最后一步；Team Updates 仍保持人工确认后收费。
- **2026-08-30（收入主线 round 27）**: 新增中文自助试用说明 `trial/README.zh.md`，中文首页、Team Updates 页面和产品 README 均直连本地化文档。
- **2026-08-30（收入主线 round 28）**: 新增同域名中英文自助试用页 `trial.html` / `trial.zh.html`，包含安装、克隆、示例审查、预期 High/Medium 与退出码、共享规则、自定义规则、团队试用和 `$49` 规则包入口；首页、Team Updates CTA 切换到本地页面，sitemap 更新；HTML/sitemap 解析、HTTP 200、漏斗 5 测试与 MCP 33 测试全部通过；提交并推送 `b5ae2b7`。生产页最初短暂返回 404，随后 GitHub Pages 同步完成并复查为 200。
- **2026-08-30（收入主线 round 20）**: 在 `TRIAL_FOLLOWUP_PLAYBOOK.md` 增加中英文首回复/试用复盘/报价模板和跟进时点；`OUTREACH_LOG.csv` 增加 GitHub issue 编号与下次跟进日期，漏斗脚本同步新 schema。
- **2026-08-30（收入主线 round 21）**: 将 Team Updates 收敛为可验收的 founding pilot：首 30 天包含共享规则档案、CI 接入复核、规则/误报复盘和邮件支持；明确不含托管扫描、全天候支持或无限定制，并同步双语页面、推广包、GTM 和跟进手册。
- **2026-08-17（round 13）**: 官网示例报告区上线验证 ✅；github.com 被墙 → 建立 API 推送流程并推送成功（remote 1fb9ff7→7342e40→cbe82eb）；CI workflow 推送被 workflow scope 拦截（404，等 PAT）；IH 交叉发帖根因定位——帖文在 Firestore `posts` 集合（非 RTDB），firestore.googleapis.com 被墙，浏览器内 fetch 也 Failed to fetch → **需 VPN**；**实测确认 0.1.0 新装即崩**（mcp 2.0.0 移除 list_tools）→ 全部安装指引改 pin `mcp<2` 止损（cbe82eb，zh.html 已生效）；Creem 复查 0 销售；Glama 仍 0 收录（72k servers 无 aicraft）；awesome #10918 open/clean、Docker #4699 open、MCPFind #139 open、Cline #2106 已被关；HN 1 point；ai-bot.cn 未收录；PH 会话过期需重登；已为 PyPI/V2EX/掘金 开好登录标签
- **2026-08-16（round 12）**: Glama 提交确认在审核队列（弹窗 "already pending review"）；官网示例报告区用真实 CLI 输出重做（3 Critical/5 High/Block）；PyPI/V2EX/掘金仍待登录；IH cross-post 受阻（UNPUBLISHED DRAFT 残留，编辑器未出现）
- **2026-08-16（round 10，转化专项）**: Team Rules Pack 上线（63 规则 + CI + prompts，全部验证）；Creem 产品更新为 $49 规则包；官网双层文案；PH 论坛发规则包公告；Dev.to 文章 5（id 4408698）
- **2026-08-16（round 9）**: 用户确认 Creem 账号 + PH 登录；Glama OAuth bug 实锤（4 次重试）；GitHub 公开邮箱设为 yaohuixue1@gmail.com；IH 误发草稿修复 + CLI 更新帖发布；Reddit 第 4 条 karma 评论；ai-bot.cn 问卷提交
- **2026-08-16（round 8）**: CLI 直跑模式上线（33 测试全过）；PH 论坛配置示例评论修正；0.1.1 dist 重建
- **2026-08-16（round 7）**: zh.html 中文落地页上线；V2EX/掘金草稿写好；Bing 收录 22 处
- **2026-08-16（round 6）**: Reddit karma 第 3 条（r/ClaudeAI）；awesome bot 要求逐条核对（仅剩 Glama）
- **2026-08-16（round 5）**: 中文博客 distribution-playbook.html 上线（eb2cb1d）
- **2026-08-16（round 4）**: Frank 邮件催办 + Glama GitHub OAuth bug 复现步骤；官网示例报告区初版（40243df）
- **更早**: round 1-3 = PH 评论回复、Dev.to 文章 1-3、Docker PR、README 修复、PH 论坛帖等（见 git log）

## CONSTRAINTS
- $0 budget；Creem (Alipay → 中国银行) 收款；用户在中国大陆（部分平台需 VPN）
- 中文回复用户；每轮结束更新本文件并推送（github.com 不通时走 API 流程）
- 不虚构数据；所有公开数字来自真实平台复查

## LATEST ROUND
- 2026-09-14（收入主线 round 104）：中英文试用页新增单行路径 `mkdir -p ... && curl ... trial.zip && unzip ... && ./run-trial.sh`，减少从看到试用页到第一次真实结果的步骤；新增页面回归断言，根测试 `43 passed`，未发送外部消息、未新增付费支出，漏斗仍为 1 contact / 0 tests / `$0 MRR`。
- 2026-09-14（收入主线 round 103）：增强 `scripts/funnel_report.py`，新增 `--as-of YYYY-MM-DD` 和 `next_follow_up` 的 due/upcoming 队列；新增日期校验与回归测试，当前输出会把 A9 的 2026-09-20 标为 upcoming。根测试 `43 passed`（本轮相关测试 16 passed），未发送外部消息、未新增付费支出，漏斗仍为 1 contact / 0 tests / `$0 MRR`。
- 2026-09-14（收入主线 round 102）：官网中英文试用页补充克隆/直链下载顺序提示，减少用户在示例文件尚未取得时直接执行命令造成的失败；新增回归断言，根测试 `41 passed`，未发送外部消息、未新增付费支出，漏斗仍为 1 contact / 0 tests / `$0 MRR`。
- 2026-09-14（收入主线 round 100）：审计自助试用路径，发现官网首步仅运行服务器、下一步却调用未安装到 PATH 的 `mcp-code-review`，会让正确安装的试用者失败。已将中英文试用页、独立试用 README 的首条命令改为直接执行 `review-file sample.py`，保留 `./run-trial.sh` 作为统一 fallback；删除页面重复的自定义规则步骤，重建 `products/mcp-code-review-trial.zip` 与 `products/mcp-code-review.zip`。页面、安装文档、归档回归共 `21 passed`，未发送外部消息、未新增付费支出，漏斗仍为 1 contact / 0 tests / `$0 MRR`。
- 2026-09-14（收入主线 round 99）：重新核验 A9 `picatz/flowstate#1584` 和候选 A12 `networkit/networkit#1471` 的公开状态；A9 只有 GoodJobwilliam 于 2026-09-13 发布的 1 条评论且维护者未回复，A12 仍为维护者发起的 open 实验且只有 1 条社区评论，因此没有重复触达或未经确认发帖。增强 `scripts/funnel_report.py` 输出目标缺口：当前日志为 1 contact / 0 tests / 0 paid signals / 0 pre-commitments / `$0 MRR`，距离 `$2,000 MRR` 还需 21 个 Team Pilot 或 106 个 Starter；新增回归测试，根测试 `40 passed`，并通过 shell、compileall、diff 检查。远端同步提交 `c85e86b` 与 `0ffdb8d`，未触碰受 workflow scope 限制的发布 workflow，未新增付费支出。
- 2026-09-14（收入主线 round 98）：降低独立试用包的安装摩擦：`run-trial.sh` 继续优先使用 `uvx`，缺少 `uvx` 时自动创建临时 Python 环境安装公开 PyPI `0.1.2`，并在退出时清理；中英文试用说明同步，重建 `products/mcp-code-review-trial.zip` 和 `products/mcp-code-review.zip`，归档/安装测试 `21 passed`，shell 语法检查和 `git diff --check` 通过。未发送外部消息、未新增付费支出，漏斗仍为 1 contact / 0 tests / $0 MRR。
- 2026-09-03（收入主线 round 97）：为下一版发布候选增加 mcp-code-review schema 命令，直接输出随 Python 包携带的 JSON 结果契约，降低 CI 集成门槛；双语 README、试用说明和 CHANGELOG 已同步，并明确当前公开 PyPI 0.1.2 尚未包含该命令。尚未发布新的 PyPI 版本，未发送外部消息、未新增付费支出，漏斗仍为 0。
- 2026-09-03（收入主线 round 96）：核验新的高相关公开 prospect picatz/flowstate#1584：议题同时要求 CLI explanation、JSON/MCP 结构化结果和 CI widening gate，且标记为 security/cli；加入 A9 队列与架构回复草稿。未自动发帖、未写入联系人漏斗、未新增付费支出。
- 2026-09-03（收入主线 round 95）：核验新的高相关公开 prospect SociableSteve/caroline#79：议题明确要求提交前与 CI 的同一 secret 检查，维护者已选择 secretlint 并讨论非 provider 模式和可审计 suppression。加入 A8 队列与技术回复草稿；未自动发帖、未写入联系人漏斗、未新增付费支出。
- 2026-09-03（收入主线 round 94）：常规 git push 被 GitHub OAuth 的缺少 workflow scope 拒绝后，使用 Git Data API 将文档、schema、测试和更新后的免费 Server zip 同步到远端 main；远端提交为 f689160ef9a23a043ee66adbb28ab679f5a76c58，远端 zip 与本地 SHA-256 一致。发布 workflow 未强行绕过权限，仍只在本地等待具备 workflow scope 后同步；PyPI 仍为 0.1.2，未发布新版本、未发送外部消息、未新增付费支出，漏斗仍为 0。
- 2026-09-03（收入主线 round 93）：发布候选变更触发归档字节同步测试，发现免费分发包仍是旧版 pyproject.toml；按精确文件清单重建 products/mcp-code-review.zip，排除缓存文件并通过归档校验。根测试 36 passed，MCP 产品测试 48 passed，Ruff 通过；PyPI 仍为 0.1.2，未发布新版本、未发送外部消息、未新增付费支出，漏斗仍为 0。
- 2026-09-03（收入主线 round 92）：新增 products/mcp-code-review/RELEASING.md 与仅在维护者显式创建 aicraft-code-review-v* 标签时运行的 PyPI Trusted Publishing workflow；发布前自动执行 Ruff、48 项产品测试、wheel/sdist 构建和包内容检查。发现并修复原构建物遗漏 JSON schema 的真实断层，将 schema 纳入 Python package data 并加回归测试。当前 PyPI 仍为 0.1.2，未发布新版本、未发送外部消息、未新增付费支出；漏斗仍为 0。
- 2026-09-03（收入主线 round 78）：收敛中英文首页的主转化路径，在首屏后增加“安装 → 10 分钟验证 → 团队上线”三步入口，降低从免费 MCP server 到 Team Pilot 的理解成本；试用页增加结构化 GitHub 反馈之外的预填邮件反馈入口，覆盖 GitHub 访问受限或不愿公开发帖的试用者；新增回归测试，根测试 27 passed。未发送外部消息、未新增付费支出，公开试用与收入漏斗仍为 0。
- 2026-09-03（收入主线 round 79）：修复 AI agent 安装指南仍使用旧 uvx --with ... aicraft-code-review 命令的问题，统一到已实测的 uvx --from aicraft-code-review --with "mcp<2" mcp-code-review；新增安装文案回归覆盖该指南。未发送外部消息、未新增付费支出，公开试用与收入漏斗仍为 0。
- 2026-09-03（收入主线 round 80）：审计公开分发元数据，修正 LAUNCHGUIDE、Glama 配置、MCP marketplace 提交模板和安装规则中的旧 OWASP/Top 10 承诺，统一为可验证的 deterministic local security-pattern checks；新增元数据回归测试。未发送外部消息、未新增付费支出，公开试用与收入漏斗仍为 0。
- 2026-09-03（收入主线 round 81）：为独立试用包增加透明的 run-trial.sh 启动脚本，自动检查 uvx 并执行已验证的 PyPI review 命令，缺少依赖时返回 exit 2、示例发现时保留真实 exit 1；双语试用说明与归档同步测试已更新。未发送外部消息、未新增付费支出，公开试用与收入漏斗仍为 0。
- 2026-09-03（收入主线 round 82）：审计 `CREEM_PRODUCTS.md` 的商业状态，移除“全部正式开售”导致的收入歧义，明确一次性结账页已配置、Team Updates 尚未自动订阅、确认付款和 MRR 仍为 0；新增状态文档回归测试。未进入 Creem 后台修改账户、未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 83）：为 MCP CLI 增加可选 `--format json` 机器可读输出，包含 schema_version、稳定 check id、严重度计数、verdict 和一致的 CI exit code；默认 Markdown 行为保持不变，双语 README 明确该能力在新 PyPI 发布前仅保证于源码，避免把未发布代码冒充 `0.1.2`。新增 CLI JSON 回归测试。未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 84）：重新核验 issue-backed signals A4-A6 仍为开放且相关，新增三条技术回复草稿到 `OUTREACH_DRAFTS.md`；草稿不代表已发帖，未写入联系人漏斗，也未新增付费支出。
- 2026-09-03（收入主线 round 85）：为源码中的 `--format json` 增加独立 `schema/review-result.schema.json` 输出契约，并接入中英文 README 与归档/文档回归测试，方便团队验证 CI 消费格式；仍未发布新的 PyPI 版本，未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 86）：通过 GitHub 公共 API 重新核验 A1-A6 issue 均仍开放；根据最新线程上下文重写 A1-A3 技术回复草稿并标注人工发送顺序，A1 改为只讨论网站 Add-to-Cursor payload，A3 纳入最新静态凭据失败背景；未自动发帖、未写入联系人漏斗、未新增付费支出。
- 2026-09-03（收入主线 round 87）：为免费 MCP Server 增加可复制的 secretless GitHub Actions PR 检查模板，使用当前 PyPI 版本和稳定退出码；中英文 README、归档清单与测试同步，明确共享规则和持续维护仍属于 Team Rules Pack / Team Updates；未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 88）：将免费 GitHub Actions 起步模板接入中英文自助试用页，试用者可从一次本地运行直接进入真实 Pull Request 验证；新增页面回归测试，根测试 34 passed；未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 89）：将免费 GitHub Actions 模板固定到已验证的 PyPI `0.1.2`，避免未发布源码变化影响首次试用；同步中英文文档和回归测试，未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 90）：在根 README 增加免费 Pull Request 检查模板入口，并在 `PROGRESS.md` 增加当前可验证状态快照（Pypistats 最近 30 天下载 307，销售漏斗和收入仍为 0）；下载量仅作分发信号，不计作客户或收入。未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 91）：核对公开分发元数据，修正 MCPFind 提交草稿中残留的 OWASP 夸大描述，并移除仓库内跟踪的旧 0.1.0 `mcp-code-review` egg-info，避免与实际 `aicraft-code-review` 0.1.2 构建元数据冲突；根测试 34 passed，MCP 测试 48 passed，Ruff 通过。未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 92）：通过 GitHub 公共 API 发现并核验新的高相关候选 `lwgerhardt/agent-co-op-mcp#40`（MCP DX、结构化返回、版本单一来源和 CI 校验）；加入公开触达队列与技术回复草稿。issue 仍是 prospect，未自动发帖、未写入联系人漏斗、未新增付费支出。
- 2026-09-03（收入主线 round 77）：新增独立 `products/mcp-code-review-trial.zip` 试用包（示例、隐藏 JSON 配置、中英文说明），中英文试用页加入直接下载入口和归档同步测试；减少首次试用的文件复制摩擦，未新增付费支出。
- 2026-09-03（收入主线 round 76）：在根 README 的 MCP 产品段增加免费 10 分钟试用、结构化反馈、团队试用和 Team Pilot 范围入口，并新增回归测试；缩短 GitHub 访问者从安装到反馈/团队转化的路径。未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 75）：新增根目录 `pytest.ini`，将默认 `python3 -m pytest` 限定到仓库级漏斗、归档和文案测试，避免递归收集其他产品的独立依赖；MCP 产品仍通过其 `uv run --locked pytest` 单独验证。
- 2026-09-03（收入主线 round 74）：继续用 GitHub 公共 issue API 筛选 3 条具体需求（aster-code-review 领域知识 MCP、Claude AI PR 工作流、Sourcery CLI 审查），加入 `OUTREACH_QUEUE.md` 的 issue-backed signals；只记录公开证据和技术开场，不自动发帖、不计入联系人、试用或收入。
- 2026-09-03（收入主线 round 73）：核验 Team Rules Pack 的 63 条规则和 CI 交付，新增精确规则数量回归测试（Python 21、JS/TS 16、Go 13、Java 13）；规则包测试 4 passed，未修改付费内容或收入数据。
- 2026-09-03（收入主线 round 72）：收紧中文首页、PyPI 描述、官方 Registry 和 server card 的 MCP 能力表述，移除完整 OWASP/Top 10 暗示，统一为可验证的 deterministic local security-pattern checks；新增元数据回归测试，重建下载 ZIP。
- 2026-09-03（收入主线 round 71）：将上述能力边界和 `uvx` 修复写入产品 `CHANGELOG.md`，让 PyPI 用户看到与当前版本一致的变更记录；重建下载 ZIP，文案/归档测试 21 passed。
- 2026-09-03（收入主线 round 70）：对照免费服务器实际规则收紧公开承诺：移除未实现的竞态检测和完整 OWASP Top 10 扫描表述，改为可验证的本地安全模式、性能、质量和风格检查；新增文案回归测试防止重新出现该类夸大承诺。
- 2026-09-03（收入主线 round 69）：进一步修正产品 Dockerfile，改为构建时安装本地 `.`，避免镜像安装 PyPI 后与当前源码漂移；`pyproject.toml` 继续锁定 `mcp<2`，归档元数据测试同步更新。
- 2026-09-03（收入主线 round 68）：审计 Docker 与 MCPB 分发入口，修复产品 Dockerfile 覆盖旧提交的问题，改为安装 PyPI `0.1.2` + `mcp<2`；将 `mcp-code-review.mcpb` 从 `0.1.0` 更新到 `0.1.2`，并修正内部 `uvx` 参数；新增归档元数据回归测试，相关测试 20 passed。未新增付费支出、未发送外部消息。
- 2026-09-03（收入主线 round 67）：新增 OUTREACH_DRAFTS.md，为三条有具体公开痛点的 issue 准备技术回复草稿和人工发送检查清单；未自动发帖、不计入联系人或收入，后续只有真实发布和真实回复才能进入漏斗。
- 2026-09-03（收入主线 round 66）：新增安装文案回归测试，覆盖中英文产品 README、自助试用页与首页，锁定已实测可用的 uvx --from aicraft-code-review --with ... mcp-code-review 入口并拒绝旧命令，防止免费试用再因 package/executable 名称不一致而中断。
- 2026-09-03（收入主线 round 65）：实测发现 PyPI 包的 `uvx` 入口必须使用 `--from aicraft-code-review ... mcp-code-review`，原有 `uvx ... aicraft-code-review` 会因找不到 executable 失败；已统一修正首页、中英文试用页、README、MCP 配置、发布/市场文案和博客社交草稿，并验证正确命令在临时环境输出 High + Medium、退出码 1。同步重建下载 ZIP，测试通过；未新增付费支出、未发送外部消息。
- 2026-09-03（收入主线 round 64）：修正中文首页 MCP 卡片将 `$49` 写成“终身授权”的歧义，明确付费项是 Team Rules Pack、服务器仍免费；中英文产品 README 接入 Team Pilot 范围与验收清单链接。未新增付费支出，未发送外部消息。
- 2026-09-03（收入主线 round 63）：将 Team Pilot 范围说明和验收清单接入根 README 与中文首页，打通 GitHub/自然流量入口到免费试用和团队转化路径；未发送外部消息、未新增付费支出，漏斗仍以真实 issue 和 Creem 证据为准。
- 2026-09-03（收入主线 round 62）：基于 GitHub 公共 issue API 核验三条具体痛点信号（Cursor 安装失败、MCP stdio code-review 任务、代理审查失败导致 PR 误红），加入 `OUTREACH_QUEUE.md` 的 issue-backed signals 区；只记录公开证据和技术开场，不发送外部消息，不计入联系人、试用或收入。
- 2026-09-03（收入主线 round 61）：新增 `TEAM_PILOT_BRIEF.md`，把 Team Pilot 首 30 天交付物、验收清单、边界和收费触发条件整理成可直接分享的范围说明；中英文 Team Updates 页面、GTM 下一步和触达包均接入该说明。未新增付费工具、未发送外部消息，公开试用与收入漏斗仍需真实用户进入后再更新。
- 2026-09-03（收入主线 round 60）：修正根 README 路线图中初始产品数量（8 -> 9），与当前 Creem 产品清单一致；没有把产品数量当作收入证据。
- 2026-09-03（收入主线 round 59）：更新 `OUTREACH_LOG.md` 的复核日期和证据字段说明，明确来源归因、报价档位、意向信号与 Creem 付款引用的边界，避免后续人工录入时把推断或意向当成收入。
- 2026-09-03（收入主线 round 58）：在 AI agent 安装指南与发布指南增加 Team Rules Pack `$49` 的直接 Creem checkout CTA，并再次明确免费 MIT Server 边界，减少从自动发现/安装文档到购买的路径损失。
- 2026-09-03（收入主线 round 57）：漏斗报告在保留原有计数的基础上，按 `offer_tier` 和 `discovery_source` 增加试用率、付费信号率、预承诺率；收入记录现在同时强制要求 `offer_tier` 与 `payment_reference`，每笔真实收入都能追溯到具体报价和 Creem 证据。根测试 18 passed，MCP 测试 45 passed，Ruff 与 `git diff --check` 通过。
- 2026-09-03（收入主线 round 56）：漏斗报告新增按 `discovery_source` 分组的真实转化统计，展示各免费分发渠道的联系人、试用、付费信号、预承诺、订阅数与确认 MRR；空日志不显示虚假渠道，新增回归测试。根测试 16 passed，MCP 测试 45 passed，Ruff 与 `git diff --check` 通过。
- 2026-09-03（收入主线 round 55）：中英文团队试用与试用反馈表单新增必填 `discovery-source` 渠道归因字段，GitHub 只读报告会展示来源；`OUTREACH_LOG.csv` 同步加入 `discovery_source`，为后续比较 Registry、Smithery、目录、Product Hunt、搜索和推荐的真实转化率做准备。当前没有线索，收入仍为 0。
- 2026-09-03（收入主线 round 54）：在中英文 MCP 产品 README 增加直接的 Team Rules Pack `$49` Creem checkout CTA，明确免费 MIT Server 与付费规则包的边界，缩短 GitHub 产品页到购买的路径；同步重建 `products/mcp-code-review.zip`。没有新增付费服务。
- 2026-09-03（收入主线 round 54）：在中英文 MCP 产品 README 增加直接的 Team Rules Pack `$49` Creem checkout CTA，明确免费 MIT Server 与付费规则包的边界，缩短 GitHub 产品页到购买的路径；没有新增付费服务。
- 2026-09-03（收入主线 round 53）：修正中英文首页 MCP 产品卡的视觉报价歧义：服务器价格区现在明确显示免费 MIT Server，$49 只出现在 Team Rules Pack 购买按钮中，避免用户把免费主产品误解为付费。
- 2026-09-03（收入主线 round 52）：为 `OUTREACH_LOG.csv` 和 `scripts/funnel_report.py` 增加 `payment_reference` 证据字段；任何正的一次性收入或 MRR 若没有可核验的 Creem 订单/订阅引用都会被拒绝，避免误把表单意向或手工数字当成收入。空漏斗仍为 0，漏斗测试 8 passed。
- 2026-09-03（收入主线 round 51）：将 `scripts/github_trial_report.py` 改为分页读取 GitHub 公共 Issues，并排除 Pull Request；新增分页回归测试，避免公开线索超过 100 条后静默漏读。工具仍只读、不写 issue、不更新收入。相关测试 14 passed，Ruff 与 `git diff --check` 通过；当前 API 仍为 0 条试用/反馈 issue。
- 2026-09-03（收入主线 round 50）：重建仓库内的 `products/mcp-code-review.zip` 免费 Server 分发包，使其与当前 27 个跟踪源码文件字节同步；移除旧版 7 月代码、build/cache/egg-info 等污染内容，新增 `tests/test_mcp_archive.py` 防止下载包再次落后。归档测试 1 passed，漏斗/issue 测试 13 passed，MCP 严格测试 45 passed，Ruff 与 `git diff --check` 通过。未发布 PyPI 0.1.3，也未修改 Creem。
- 2026-09-03（收入主线 round 49）：修正 `PROGRESS.md` 中将整个 MCP Code Review Server 写成 `$49` 的历史性价目表述，明确免费 MIT Server 与 `$49` Team Rules Pack 的边界；没有修改收入数据或 Creem 已有文件。
- 2026-09-03（收入主线 round 48）：重新核验 GitHub 公共 API 的候选仓库状态，刷新 `OUTREACH_QUEUE.md` 的日期、开放 issue 数和最近更新时间，并新增 `kopfrechner/gitlab-mr-mcp` 与 `mattzcarey/shippie` 两个技术问题候选。没有发送任何外部消息；候选仍不计入联系人、试用或收入。
- 2026-09-03（收入主线 round 47）：修正 `products/mcp-code-review/uv.lock` 与 `pyproject.toml` 的本地包版本漂移（0.1.0 -> 0.1.2），使 `uv run --locked` 可复现安装；严格产品测试 45 passed，漏斗/issue 报告测试 12 passed，Ruff 与 `git diff --check` 通过。
- 2026-09-03（收入主线 round 46）：新增只读 scripts/github_trial_report.py，从公开 GitHub Issues 提取中英文团队试用/试用反馈表单的团队规模、语言、报价档位、决策时间和有条件承诺，输出人工复核队列；不会发帖、修改 issue、写入 OUTREACH_LOG.csv，也不会把表单意向当作收入。中英文 trial-feedback Issue Forms 新增必填 offer-tier 与 precommitment 字段，避免反馈进入漏斗后缺少报价档位和条件开始承诺。脚本测试 12 passed（含漏斗回归），所有 Issue Form YAML 可解析且字段 ID 唯一；公开 GitHub API 当前仍为 0 条试用/反馈 issue，真实收入与 MRR 仍为 0。
- 2026-09-03（收入主线 round 45）：修正根 README 将免费的 MCP Code Review Server 误标为 `$49` 的转化问题，明确 MIT 免费 server 与 `$49` Team Rules Pack 的边界；同步定价哲学，避免新用户在免费试用入口被错误价格拦截。
- 2026-08-30（收入主线 round 44）：中英文团队试用表单新增明确的 conditional-start 预承诺字段（确认范围和开始时间后是否按所选档位开始），并同步跟进手册证据标准；提交表单仍不会收费，只有人工核对“档位、开始月份、范围/价格”三项后才记录 `precommitment=yes`。
- 2026-08-30（收入主线 round 43）：漏斗报告新增按 `offer_tier` 的联系人、试用、付费信号、预承诺、订阅数与确认 MRR 分段；空日志不显示该分段，避免制造不存在的信号。新增回归测试验证 Team Pilot 的确认订阅可记入 MRR，而 Starter 预承诺仍为 `$0 MRR`。
- 2026-08-30（收入主线 round 42）：将双层 Team Updates offer 统一到首页、中文页、产品 README、发布指南、试用包、Issue Form、GTM、推广包、跟进手册和市场提交说明；漏斗 `offer_tier` 已纳入必填字段并新增缺列回归测试。Starter 为最多 3 人 `$19/月`，Team Pilot 为最多 10 人 `$99/月`；当前仍无真实付款或预承诺。
- 2026-08-30（收入主线 round 41）：将 Team Updates 从单一 `$19/月` 早期体验调整为可验证双层 offer：Starter（最多 3 人，$19/月或 $190/年）与 Team Pilot（最多 10 人，$99/月或 $990/年，含 CI/调优支持）；同步首页、中英文产品文档、试用包、GTM、推广包、跟进手册和四个 Issue Form；漏斗 CSV 新增 `offer_tier` 字段，后续可区分不同价格意向。目标数学为 21 个 Team Pilot 约 $2,079 MRR；当前真实收入仍为 0。
- 2026-08-30（收入主线 round 40）：收紧免费 server 的 `hardcoded_secret` 内置规则：只有凭据字段被赋值为字符串字面量时才触发，不再把函数名、注释或 `os.environ` 查找误报为硬编码密钥；新增回归测试。尚未发布新 PyPI 版本，线上仍为 `0.1.2`；收入证据仍为 0。
- 2026-08-30（收入主线 round 39）：将 Team Rules Pack GitHub Actions 拆为只读 `review` job 与独立 `comment` job：执行 PR 内容的 job 不再持有写权限；评论 job 只下载 artifact、使用 `issues: write`，并仅对同仓库 PR 运行；fork PR 仍保留报告 artifact；Critical 门禁通过 review job 输出保持生效。README、测试与 ZIP 已同步更新。
- 2026-08-30（收入主线 round 38）：继续修正 Team Rules Pack GitHub Actions 交付：`issues.createComment` 改用正确的 `issues: write` 权限；来自 fork 的 PR 跳过写评论以适配 GitHub 只读 token；新增 `actions/upload-artifact@v4` 始终上传 `review-report.txt`。README、回归测试与 ZIP 已同步更新。
- 2026-08-30（收入主线 round 37）：修复 Team Rules Pack GitHub Actions 模板的真实运行权限：PR 评论步骤从 `pull-requests: read` 改为 `pull-requests: write`；README 明确最小权限范围；归档同步测试增加权限回归；ZIP 已同步更新。尚未发布新 PyPI 版本，收入证据仍为 0。
- 2026-08-30（收入主线 round 36）：基于 GitHub 公共 API 二次搜索并核验 README/仓库元数据，向 `OUTREACH_QUEUE.md` 增加 5 个新候选（MCP Audit Scanner、PR Review Assistant、Lintro、agent-bom、Rebar），每个候选附公开 issue 链接和技术问题开场；明确这些只是审计快照，未发送任何外部消息，也不计入联系人、试用或收入。漏斗仍为 `$0 MRR`。
- 2026-08-30（收入主线 round 35）：修复 Team Rules Pack 的 GitLab CI 交付缺陷：模板现在将报告写入 `review-report.txt`、始终作为 artifact 保留，并传递真实退出码（Critical=`2` 阻断，High/Medium=`1` 按现有策略允许失败）；同步更新规则包 README，重建 8 文件 ZIP；新增归档同步测试。规则包测试 `2 passed`，MCP 产品测试 `44 passed`，漏斗测试 `5 passed`，Ruff 和 `git diff --check` 通过。未发布新 PyPI 版本，线上仍为 `0.1.2`；收入证据仍为 0。
- 2026-08-30（收入主线 round 34）：修复团队共享配置损坏时的体验问题：JSON/YAML 解析错误现在带文件路径及行列信息；CLI 统一返回 exit `2`，MCP 工具返回可读 `Error:`，不再把 parser traceback 暴露给客户端；新增 CLI/MCP 回归测试。产品测试 `44 passed`、漏斗测试 `5 passed`、Ruff 和 `git diff --check` 全部通过。未发布新 PyPI 版本，线上仍为 `0.1.2`；收入证据仍为 0。
- 2026-08-30（收入主线 round 29）：首页中英文首屏增加免费试用 CTA；试用页增加无 Git 直接下载命令和公开 trial-config.json（下载后保存为 .mcp-code-review.json 以触发自动发现）；试用结果增加邮件回复入口；英文/中文产品 README 与跟进手册统一到官网试用页。
- 本地 CLI 实测得到 1 High + 1 Medium、退出码 1；生产页面 trial.html、trial.zh.html、sample.py、trial-config.json 均返回 200。
- 漏斗统计仍为 0 contacts / 0 paid signals / 0 pre-commitments / $0 one-time revenue / $0 MRR；提交 8fb171e 已推送到 main。
- 2026-08-30（收入主线 round 30）：基于 GitHub 公共 API 核验候选仓库的 issue 开放状态与最近提交，新增 `OUTREACH_QUEUE.md` 固化 8 个优先候选和技术开场问题；新增中英文 `trial-feedback` Issue Forms，记录试用发现、共享规则、误报/遗漏、下一步意向与决策时间；试用页和 issue 配置已接入反馈入口。未发送外部消息，未把候选项目或表单提交计入收入。
- 2026-08-30（收入主线 round 31）：修复 CLI `review-diff --git` 文案与实现不一致问题，新增 `--staged` 使用 `git diff --cached` 检查 index；对文件/Git 错误返回简洁的 CI exit 2；补充帮助、staged 调用和缺失文件回归测试；同步 README、中文 README、AI 安装指南与 CHANGELOG。源码 lint 通过，MCP 测试 36 passed，漏斗测试 5 passed。该修复尚未发布新的 PyPI 版本，线上仍为 0.1.2。收入证据仍为 0。
- 2026-08-30（收入主线 round 33）：MCP server 增加参数对象、必填字符串、路径类型和 UTF-8 读取校验，避免编辑器调用时抛 `KeyError` 或原始文件异常；新增 5 个 server 输入/文件错误测试。源码 lint 通过，MCP 测试 42 passed，漏斗测试 5 passed。修复仍只在 GitHub `main`，PyPI 线上仍为 0.1.2。
- 2026-08-30（收入主线 round 32）：补充真实 Git 仓库 staged/unstaged 对照回归测试，MCP 测试达到 37 passed；修复测试文件 import lint 提示。GitHub `main` 源码已包含 CLI 修复，但 PyPI 仍为 0.1.2，未把未发布代码当作线上版本。
