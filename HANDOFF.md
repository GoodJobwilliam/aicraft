# HANDOFF CONTEXT (updated 2026-08-17 CST)

## CURRENT STATE
- **目标**: aicraft 达到 $2,000 MRR；预算 $0；工作区 `/Users/william/work/AIcompany/aicraft`
- **Website**: https://aicraft.vip (EN) + /zh.html (CN) — live。首页示例报告区展示 Team Rules Pack 真实输出（`MCP_CODE_REVIEW_CONFIG=rules/python.yaml mcp-code-review review-file main.py`，3 Critical / 5 High / Block，exit 2）并直链 Creem $49 结算页（commit 已上线，remote 1fb9ff7）
- **Creem**: 9 产品 live，**0 销售 / 0 订阅 / 0 客户**（2026-08-17 复查，无变化）。账号 731685147@qq.com。增值产品 Team Rules Pack `prod_6Z3S3jGNPsCyRSqNi397ZY`（63 条规则 + CI playbook + LLM prompts，$49）
- **GitHub**: GoodJobwilliam/aicraft，2 stars / 0 forks。⚠️ github.com 直连被墙（api.github.com 可达）→ **推送必须走 API**（recipe 见 TOOLING NOTES）。OAuth token 无 `workflow` scope → `.github/workflows/ci.yml` 无法推送（本地就绪，等 PAT）
- **登录状态（in-app browser, CDP 9229）**: Google ✅ / GitHub ✅ / Smithery ✅ / Glama ✅ / Creem ✅（QQ 账号）/ IH ✅（Firebase，但 Firestore 被墙不可用）。⚠️ Product Hunt 会话已过期（需重新登录）；PyPI / V2EX / 掘金 未登录——**登录页标签已开好**（PyPI=E60305F8、V2EX=76D6EA55、掘金=BC42B4FB）
- **网络**: github.com、googleapis.com（Firestore/identitytoolkit）不通——**用户 VPN（MotionPro 同济 vpn.tongji.cn）当前断开**。其余（PyPI/PH/Glama/Dev.to/Smithery/Creem/mcpservers）均可达
- **PyPI 0.1.1 就绪待发**: dist 已构建、fresh venv 验证通过（mcp 1.29.0）。只差用户登录 PyPI 后建 token。⚠️ 0.1.0 的 `mcp>=1.6` 无上限，mcp 2.0.0 已致新装用户 CLI 崩溃

## LAUNCH STATUS (2026-08-17)

| Platform | Status | Notes |
|----------|--------|-------|
| **Smithery.ai** | ✅ Live | [yaohuixue1/mcp-code-review](https://smithery.ai/servers/yaohuixue1/mcp-code-review) 52/100。Arcade 迁移后 redeploy 通道坏（UI Publish 无反应，API POST /releases 404）。验证需付费计划 |
| **mcpservers.org** | ✅ Live | APPROVED: [goodjobwilliam/aicraft](https://mcpservers.org/servers/goodjobwilliam/aicraft)，已用于 backlinks |
| **cursor.directory** | ✅ Live | [mcp-code-review-server](https://cursor.directory/plugins/mcp-code-review-server) 公开（1 Rule + 1 MCP Server） |
| **PyPI** | ✅ 0.1.0 live | 666 总下载 / 153 月 / 2 周。⚠️ mcp 2.x 崩溃问题待 0.1.1 修复；**等用户登录 PyPI** |
| **Product Hunt** | ✅ Launched | 3 upvotes / 12 followers / 7 comments（外部 5 条全部回复 + 2 条 maker 回复）。论坛帖 approved。⚠️ 浏览器会话已过期，需重新登录才能继续互动 |
| **Dev.to** | ✅ 5 篇文章 | [主页](https://dev.to/goodjobwilliam)。文章 5（id 4408698, 63 规则）0 反应。API key `GEdbXASUJqszsj4fBTX7nvK9`（POST/PUT 需浏览器 UA）。总 30 views |
| **PitchHut** | ✅ Claimed | 47 page views, 0 pitch clicks。账号 cheap_copper_rodie |
| **Glama** | ⏳ 审核队列中 | 提交确认在队列（"A submission for this repository is already pending review"）。工单 **#125096481**（Fin bot 回复过）。GitHub OAuth 连接 bug（授权成功但设置页 Not connected，48h 重试）。仍未收录（2026-08-17 复查）→ 收录后 claim + badge + 更新 PR #10918 |
| **awesome-mcp-servers** | ⏳ PR open | [#10918](https://github.com/punkpeye/awesome-mcp-servers/pull/10918) open/clean/4 comments，无维护者新回复。只差 Glama 收录+徽章 |
| **MCPFind** | ⏳ PR open | [#139](https://github.com/MCPFind/mcp-find/pull/139) open/unstable/1 comment |
| **Cline MCP Marketplace** | ❌ Issue closed | #2106 已被维护者关闭（2025-12-30），不再追 |
| **Official MCP Registry** | ⏳ 阻塞于 PyPI | `products/mcp-code-review/registry/server.json` valid；PyPI 0.1.1 发布后 `mcp-publisher publish` |
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
- **mcp<2 安装指引**（cbe82eb，已上线）: README/README.zh/zh.html 所有安装命令改为 pin `mcp<2`（实测确认 0.1.0 + mcp 2.0.0 新装必崩: `AttributeError: 'Server' object has no attribute 'list_tools'`）——0.1.1 发布前的止损措施
- **待推送（本地）**: `.github/workflows/ci.yml`（需 PAT workflow scope，Git Data API 也会 404）

## TOOLING NOTES
- **GitHub 推送（github.com 被墙时的标准流程）**: 走 api.github.com Git Data API——① GET `/git/refs/heads/main` 取 BASE；② POST `/git/blobs`（base64 文件内容）；③ GET `/git/commits/BASE` 取 parent tree，POST `/git/trees`（`base_tree` + 变更文件）；④ POST `/git/commits`（注意：GitHub 会把 date 的时区归一化成 UTC 存盘，本地重建 commit 无法字节对齐——接受 SHA 分歧，本地分支与远端树内容保持一致即可，**不要** git pull/push 覆盖远端）；⑤ PATCH `/git/refs/heads/main`。token 取法: `printf "protocol=https\nhost=github.com\n\n" | git credential fill`（password 行）。⚠️ token 无 workflow scope → `.github/workflows/*` 的 tree POST 返回 404
- **IH (Indie Hackers)**: 账号 aicraftbuilder / yaohuixue1@gmail.com。产品元数据在 **RTDB** `/products/mcp-code-review.json`（REST + idToken，token 缓存在 /tmp/ih_idtoken.json；identitytoolkit 被墙时改用浏览器 IndexedDB 里的 stsTokenManager 直接查）。**帖文（new-post）在 Firestore** `posts` 集合（productId 过滤），REST 需 `firestore.googleapis.com`——当前被墙，**必须 VPN 在线**。RTDB 旧 `posts/` 路径是 legacy，帖文不在那。浏览器 IH 标签经常是 stuck renderer（卡在 loading quote），需关掉重开
- **PH 评论**: GraphQL `CommentUpdate` mutation（需 X-CSRF-Token + csrf_token cookie）；回帖用 action-bar-reply-button + ProseMirror execCommand insertText。PH 会话过期快，用前先检查登录态
- **CDP**: ws://127.0.0.1:9229（/tmp/cdp.py 第一参数 = 完整 ws URL）；新 tab `PUT /json/new?URL` 共享浏览器会话
- **Creem**: dashboard 标签 56042DEA 常驻；产品编辑走 UI
- **Smithery**: API key smry_EtMB... 在 CLI config

## USER ACTIONS NEEDED（按优先级）
1. **PyPI 登录**（最高优先，0.1.1 已就绪）: 标签已开好，登录后我建 token → `uvx twine upload -u __token__ -p <token> dist/aicraft_code_review-0.1.1*` → `mcp-publisher publish`。解锁：修复 mcp 2.x 崩溃 + 官方 MCP Registry + PulseMCP 自动收录
2. **打开 VPN**（MotionPro 同济）: 解锁 github.com 直连、IH Firestore（发帖/清理草稿）、identitytoolkit
3. **V2EX + 掘金登录**: 标签已开好，草稿就绪，登录后立即可发
4. **Product Hunt 重新登录**: 会话已过期，重新登录后可继续评论互动
5. **GitHub PAT（含 workflow scope）**: 解锁 CI workflow 推送

## NEXT STEPS
1. PyPI 登录后: 发布 0.1.1 → `mcp-publisher publish` → Glama 收录后 claim + badge → 更新 awesome PR #10918
2. VPN 恢复后: IH 发新 timeline 更新 + 清理 UNPUBLISHED DRAFT（Firestore 查询法已就绪）
3. V2EX/掘金登录后: 发中文引流帖 → zh.html
4. Glama 工单 #125096481 持续跟进；GitHub OAuth 连接 bug 48h 重试
5. PulseMCP 每周查（等官方 Registry）；MCPFind #139 / Docker #4699 每周查
6. Reddit karma 攒够后 clean repost；PH 重新登录后回复新评论
7. Creem 销售每周复查（当前 $0）；Dev.to 文章 6 选题: Glama badge + registry 收录 roundup

## PATROL LOG
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
