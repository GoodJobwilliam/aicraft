# AICraft - 项目进度

## 当前可验证状态（2026-09-14）

- MCP Code Review Server：免费 MIT，本地运行；PyPI 稳定版本 `0.1.2`，官方 MCP Registry 状态为 active。
- Team Rules Pack：一次性 `$49`，包含共享规则、CI 模板和提示词；Team Updates 仍处于早期验证，收费前确认范围和开始时间。
- 免费试用：自助试用包、结构化 GitHub 表单、邮件反馈入口和 secretless GitHub Actions 起步模板均已上线。
- 公共分发信号：PyPI 最近 30 天下载量为 `307`（Pypistats，2026-09-03 核验）；下载量不等于联系人、试用或收入。
- 销售漏斗：contacts `1`、qualified replies `0`、team tests `0`、pre-commitments `0`、确认收入 `$0`、MRR `$0`。
- 已验证联系：2026-09-13 经用户确认向 Flowstate #1584 发布 1 条技术评论；A7/A9 均暂无维护者回复，不能计入试用或收入。
- 发布准备：本地 MCP 产品测试 `49 passed`、根测试 `39 passed`、Ruff 通过；wheel/sdist 均包含 JSON Schema。公开 PyPI 仍为 `0.1.2`，未将本地未发布能力计入线上承诺。
- 试用路径修复（2026-09-14）：独立试用包的 `run-trial.sh` 现在优先使用 `uvx`，没有 `uvx` 时把公开 PyPI `0.1.2` 安装到临时目录，退出时清理；中英文说明和两个分发 ZIP 已同步，归档/安装相关测试 `21 passed`。
- 试用页同步：中英文试用页已直接说明独立包可运行 `./run-trial.sh`，并标注无 `uvx` 时的隔离 Python fallback；live 页面和 live ZIP 均已核验为 `200` / 当前内容。
- 私密转化入口：中英文试用页新增预填团队资格邮件，覆盖团队规模、语言、流程、痛点、试用时间、档位、决策角色、决策时间和有条件开始承诺；不要求源代码或密钥。
- 下一步：等待 A7/A9 回复；A2/A10 仅在用户明确确认后发送。远端 Trusted Publishing workflow 仍受 GitHub token 缺少 `workflow` scope 限制。
- 漏斗报告增强（2026-09-14）：`scripts/funnel_report.py` 现在显示 `$2,000 MRR` 目标、剩余缺口、Starter/Team Pilot 所需新增客户数和下一动作；当前真实日志仍为 `$0 MRR`，对应 106 个 Starter 或 21 个 Team Pilot。
- 试用路径修复（2026-09-14）：中英文官网试用页和独立 README 的首条命令现在直接执行 `review-file sample.py`，不再出现“只安装后就调用未安装命令”的断链；重建两个 MCP ZIP，并新增页面/归档回归覆盖。
- 试用顺序说明（2026-09-14）：中英文官网页面补充提示，使用克隆或直链下载时先取得示例文件再运行命令；独立 ZIP 仍可解压后直接运行 `./run-trial.sh`。

## 2026-07-20 第一期进度报告

### 已完成
| 时间 | 事件 | 状态 |
|------|------|------|
| 下午 | GitHub Pages 网站部署 (goodjobwilliam.github.io/aicraft) | ✅ |
| 下午 | Creem 注册 + KYC 通过 + 支付宝提现绑定 | ✅ |
| 下午 | Code Review Agent skill 创建 | ✅ |
| 下午 | Git Commit Assistant skill 创建 | ✅ |
| 下午 | Python CLI Generator 代码模板创建 | ✅ |

### 当前产品清单

| 产品 | 类型 | 定价 | 目标平台 | 状态 |
|------|------|------|----------|------|
| 100 Developer AI Prompts | Prompt 合集 | $19 | Creem | ✅ 已打包 |
| AI + Trading Prompt Pack | Prompt 合集 | $29 | Creem | ✅ 已打包 |
| Code Review Agent | Agent Skill | 免费 | AgentPowers | ✅ 已上架 |
| Git Commit Assistant | Agent Skill | 免费 | AgentPowers | ✅ 已上架 |
| Python CLI Generator | 代码模板 | $49 | Creem | ✅ 已打包 |
| Python CLI 中文模板 | 代码模板 | $19 | Creem | ✅ 已打包 |
| MCP Code Review Server | MCP 工具 | 免费 MIT；Team Rules Pack $49 | GitHub / PyPI + Creem add-on | ✅ 已打包 |
| FastAPI Starter Kit | 代码模板 | $59 | Creem | ✅ 已打包 |
| AI Agent Prompts Pack | Prompt 合集 | $29 | Creem | ✅ 已打包 |
| API Development Prompts | Prompt 合集 | $19 | Creem | ✅ 已打包 |
| Next.js SaaS Starter Kit | 代码模板 | $99 | Creem | ✅ 已打包 |

### AgentPowers 已上架
| 技能 | 定价 | 状态 |
|------|------|------|
| Code Review Agent | 免费 | ✅ 已上架 |
| Git Commit Assistant | 免费 | ✅ 已上架 |
| PR Description Generator | 免费 | ✅ 已上架（安全扫描中）|

### 已生成的文件
- `products/100-ai-prompts.zip` — 100个开发者 AI Prompt（$19）
- `products/ai-trading-prompts.zip` — AI+交易 Prompt 包（$29）
- `products/ai-agent-prompts.zip` — AI Agent 构建 Prompt 包（$29）
- `products/python-cli-zh.zip` — 中文 Python CLI 模板（$19）
- `products/mcp-code-review.zip` — MCP Code Review Server（免费 MIT）；配套 Team Rules Pack 为 $49
- `products/python-cli-generator.zip` — CLI 项目模板（$49）
- `products/fastapi-starter.zip` — FastAPI Starter Kit（$59）
- `products/api-dev-prompts.zip` — API Development Prompts（$19）
- `products/nextjs-saas-starter.zip` — Next.js SaaS Starter Kit（$99）
- `CREEM_PRODUCTS.md` — Creem 上架数据

### 待用户操作
### 当前状态（全部完成 ✅）

| 项目 | 状态 | 链接 |
|------|------|------|
| Code Review Agent | ✅ 已上架 AgentPowers | https://agentpowers.ai/skills/code-review-agent |
| Git Commit Assistant | ✅ 已上架 AgentPowers | https://agentpowers.ai/skills/git-commit-assistant |
| Python CLI Generator | ⏳ 等 Creem 审核 | 待上架 Creem 商店 |

### ✅ CLI 打通
- AgentPowers API token 获取成功 ✅
- CLI 已认证（`ap whoami` 返回 `731685147@qq.com`）
- 以后发布更新可自动完成，无需手动上传

### 待办
- [ ] **SSL**: 等待 GitHub Pages SSL 证书签发
- [ ] **Creem**: SSL 就绪后去 Payout Accounts 点 Request re-review
- [ ] **MCP Marketplace**: 注册 mcp-marketplace.io 后上架 MCP Code Review Server
- [ ] **上架**: Creem 审核通过后上架全部 7 个产品

### 下次启动后我自动做的事
- SSL 就绪 → 通知你去 Creem 点重新审核
- Creem 审核通过 → 上架全部 7 个产品
- MCP Marketplace 账号注册 → 上架 MCP Code Review Server
- 持续制作更多产品扩大收入源
