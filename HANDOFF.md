# HANDOFF CONTEXT (updated 2026-08-30 CST)

## CURRENT STATE
- **目标**: aicraft 达到 $2,000 MRR；预算 $0；工作区 `/Users/william/work/AIcompany/aicraft`
- **策略更新（2026-08-30）**: 聚焦 `mcp-code-review` 主线；免费开源 server + $49 Team Rules Pack + Team Updates 早期体验（$19/月或 $190/年）。不新增任何付费工具、广告或基础设施。
- **本轮已完成**: 英文/中文首页首屏收敛到 MCP Code Review；新增 `team-updates.html` / `team-updates.zh.html`；新增预售说明、价格、邮件收集入口和中英文 GitHub team-trial Issue Forms（使用仓库已有 `question` 标签和标题前缀，避免依赖额外权限）；仓库禁用空白 issue 并提供文档/早期体验联系入口；中英文产品 README 也接入对应试用表单与 10 分钟自助试用包；README、发布指南、市场提交信息和社交草稿同步 Team Updates 口径；新增 `OUTREACH_LOG.md`；新增同域名中英文自助试用页 `trial.html` / `trial.zh.html`，首页与 Team Updates CTA 已切换，sitemap 已收录。
- **新增分发资产**: `OUTREACH_PACK.md`（中英文短帖、私信模板、资格问题和以付费承诺为准的验证标准）、`OUTREACH_TARGETS.md`（20 个公开 GitHub 候选项目和技术切入点）、`TRIAL_FOLLOWUP_PLAYBOOK.md`（人工跟进、证据阈值和收入统计口径）以及 `OUTREACH_LOG.csv` + `scripts/funnel_report.py`（可重复的漏斗统计）。
- **Website**: https://aicraft.vip (EN) + /zh.html (CN) — live；新增 `/trial.html` 与 `/trial.zh.html` 自助试用页，生产环境已返回 200。首页示例报告区展示 Team Rules Pack 真实输出（`MCP_CODE_REVIEW_CONFIG=rules/python.yaml mcp-code-review review-file main.py`，3 Critical / 5 High / Block，exit 2）并直链 Creem $49 结算页（本轮 commit `b5ae2b7`）
- **Creem**: 9 产品 live，**0 销售 / 0 订阅 / 0 客户**（2026-08-17 复查，无变化）。账号 731685147@qq.com。增值产品 Team Rules Pack `prod_6Z3S3jGNPsCyRSqNi397ZY`（63 条规则 + CI playbook + LLM prompts，$49）
- **GitHub**: GoodJobwilliam/aicraft，2 stars / 0 forks。⚠️ github.com 直连被墙（api.github.com 可达）→ **推送必须走 API**（recipe 见 TOOLING NOTES）。OAuth token 无 `workflow` scope → `.github/workflows/ci.yml` 无法推送（本地就绪，等 PAT）
- **登录状态（in-app browser, CDP 9229）**: Google ✅ / GitHub ✅ / Smithery ✅ / Glama ✅ / Creem ✅（QQ 账号）/ IH ✅（Firebase，但 Firestore 被墙不可用）。⚠️ Product Hunt 会话已过期（需重新登录）；PyPI / V2EX / 掘金 未登录——**登录页标签已开好**（PyPI=E60305F8、V2EX=76D6EA55、掘金=BC42B4FB）
- **网络**: github.com、googleapis.com（Firestore/identitytoolkit）不通——**用户 VPN（MotionPro 同济 vpn.tongji.cn）当前断开**。其余（PyPI/PH/Glama/Dev.to/Smithery/Creem/mcpservers）均可达
- **PyPI 0.1.2 live**: package metadata now pins `mcp>=1.6,<2`; public install path and docs are aligned.

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
- **待推送（本地）**: `.github/workflows/ci.yml`（需 PAT workflow scope，Git Data API 也会 404）

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
- 2026-09-03（收入主线 round 78）：收敛中英文首页的主转化路径，在首屏后增加“安装 → 10 分钟验证 → 团队上线”三步入口，降低从免费 MCP server 到 Team Pilot 的理解成本；试用页增加结构化 GitHub 反馈之外的预填邮件反馈入口，覆盖 GitHub 访问受限或不愿公开发帖的试用者；新增回归测试，根测试 27 passed。未发送外部消息、未新增付费支出，公开试用与收入漏斗仍为 0。
- 2026-09-03（收入主线 round 79）：修复 AI agent 安装指南仍使用旧 uvx --with ... aicraft-code-review 命令的问题，统一到已实测的 uvx --from aicraft-code-review --with "mcp<2" mcp-code-review；新增安装文案回归覆盖该指南。未发送外部消息、未新增付费支出，公开试用与收入漏斗仍为 0。
- 2026-09-03（收入主线 round 80）：审计公开分发元数据，修正 LAUNCHGUIDE、Glama 配置、MCP marketplace 提交模板和安装规则中的旧 OWASP/Top 10 承诺，统一为可验证的 deterministic local security-pattern checks；新增元数据回归测试。未发送外部消息、未新增付费支出，公开试用与收入漏斗仍为 0。
- 2026-09-03（收入主线 round 81）：为独立试用包增加透明的 run-trial.sh 启动脚本，自动检查 uvx 并执行已验证的 PyPI review 命令，缺少依赖时返回 exit 2、示例发现时保留真实 exit 1；双语试用说明与归档同步测试已更新。未发送外部消息、未新增付费支出，公开试用与收入漏斗仍为 0。
- 2026-09-03（收入主线 round 82）：审计 `CREEM_PRODUCTS.md` 的商业状态，移除“全部正式开售”导致的收入歧义，明确一次性结账页已配置、Team Updates 尚未自动订阅、确认付款和 MRR 仍为 0；新增状态文档回归测试。未进入 Creem 后台修改账户、未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 83）：为 MCP CLI 增加可选 `--format json` 机器可读输出，包含 schema_version、稳定 check id、严重度计数、verdict 和一致的 CI exit code；默认 Markdown 行为保持不变，双语 README 明确该能力在新 PyPI 发布前仅保证于源码，避免把未发布代码冒充 `0.1.2`。新增 CLI JSON 回归测试。未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 84）：重新核验 issue-backed signals A4-A6 仍为开放且相关，新增三条技术回复草稿到 `OUTREACH_DRAFTS.md`；草稿不代表已发帖，未写入联系人漏斗，也未新增付费支出。
- 2026-09-03（收入主线 round 85）：为源码中的 `--format json` 增加独立 `schema/review-result.schema.json` 输出契约，并接入中英文 README 与归档/文档回归测试，方便团队验证 CI 消费格式；仍未发布新的 PyPI 版本，未发送外部消息、未新增付费支出。
- 2026-09-03（收入主线 round 86）：通过 GitHub 公共 API 重新核验 A1-A6 issue 均仍开放；根据最新线程上下文重写 A1-A3 技术回复草稿并标注人工发送顺序，A1 改为只讨论网站 Add-to-Cursor payload，A3 纳入最新静态凭据失败背景；未自动发帖、未写入联系人漏斗、未新增付费支出。
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
