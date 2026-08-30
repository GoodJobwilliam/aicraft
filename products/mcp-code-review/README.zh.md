# MCP Code Review Server（中文文档）

mcp-name: io.github.GoodJobwilliam/aicraft-code-review

[![smithery badge](https://smithery.ai/badge/yaohuixue1/mcp-code-review)](https://smithery.ai/servers/yaohuixue1/mcp-code-review)
[![Product Hunt](https://img.shields.io/badge/Launch-July%2029%2C%202026-orange?style=flat-square&logo=product-hunt)](https://www.producthunt.com/products/mcp-code-review-server?launch=mcp-code-review-server)

已收录：[官方 MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.GoodJobwilliam%2Faicraft-code-review) · [Smithery](https://smithery.ai/servers/yaohuixue1/mcp-code-review) · [mcpservers.org](https://mcpservers.org/servers/goodjobwilliam/aicraft) · [cursor.directory](https://cursor.directory/plugins/mcp-code-review-server)

把代码审查做成 MCP 服务器，接进 Claude Code、Cursor、Cline 或任何支持 MCP 的 AI 助手。**完全本地运行，代码零上传。**

English docs: [README.md](./README.md)

## 功能

- **`review_code`** — 审查任意代码片段（bug、安全、性能、风格）
- **`review_diff`** — 合并前审查 git diff
- **`review_file`** — 按路径审查本地文件

内置 OWASP Top 10 模式扫描、N+1 查询检测、竞态分析，输出带严重度分级的结构化报告。

## 快速开始

### 通过 `uvx`（免安装）

```bash
# 添加到 Claude Code 的 MCP 配置：
claude mcp add code-review -- uvx --with "mcp<2" aicraft-code-review
```

或写进 `~/.cursor/mcp.json` / `claude_desktop_config.json`：

```json
{
  "mcpServers": {
    "code-review": {
      "command": "uvx",
      "args": ["--with", "mcp<2", "aicraft-code-review"]
    }
  }
}
```

### 通过 pip

```bash
pip install "aicraft-code-review==0.1.2" "mcp<2"
python -m mcp_code_review
```

> 兼容性说明：PyPI `0.1.2` 已自动锁定 `mcp<2`。如果安装旧版 `0.1.0`，必须手动添加 `mcp<2`，因为 MCP 2.0 移除了 `Server.list_tools`。

### Team Updates（早期体验）

需要持续规则更新、CI 工作流刷新和上线支持的团队，可以加入 **Team Updates** 早期名单：Starter 为[$19/月或 $190/年](https://aicraft.vip/team-updates.zh.html)（最多 3 人），Team Pilot 为 $99/月或 $990/年（最多 10 人）。目前只和少量团队验证，收费前会先确认交付范围和上线时间。

如需结构化、免费的团队试用，可以[打开 GitHub 中文试用申请表](https://github.com/GoodJobwilliam/aicraft/issues/new?template=team-trial-zh.yml&title=%5B%E5%9B%A2%E9%98%9F%E8%AF%95%E7%94%A8%5D)。请勿提交源代码、凭据或其他机密信息。

### CLI 直跑模式（不需要 MCP 客户端）

```bash
# 审查本地文件（自动从文件所在目录向上发现 .mcp-code-review.yaml）
mcp-code-review review-file path/to/file.py

# 审查未暂存的 git diff
git diff | mcp-code-review review-diff
mcp-code-review review-diff --git

# 提交前审查已暂存的改动
mcp-code-review review-diff --staged

# 审查代码片段
mcp-code-review review-code "import os; os.system('ls')"
```

退出码适配 CI：`0` 干净 / `1` 存在 High 或 Medium / `2` 存在 Critical。

## 使用示例

## 10 分钟团队试用

运行[中文自助试用包](https://aicraft.vip/trial.zh.html)，用一个故意包含风险的示例测试共享 JSON 规则。它使用免费的本地服务器，不会产生收费，并帮助团队判断是否需要 Team Rules Pack 或 Team Updates。

接好后直接问你的 AI 助手：

> "帮我审查这段 Python 代码的安全问题：[粘贴代码]"
> "提交前审查一下这个 diff：[粘贴 diff]"
> "审查这个文件：/path/to/file.py"

AI 会调用 MCP 服务器并返回结构化结果。

### 示例输出

```
## Review Results

### 🟠 High (2)
| Line | Issue | Category | Fix |
|------|-------|----------|-----|
| 4 | Command injection risk | security | Use subprocess.run with args list |
| 9 | N+1 query in loop | performance | Batch query or eager loading |

### Summary
- **Critical**: 0
- **High**: 2
- **Medium**: 0
- **Info**: 0
```

## 自定义规则 & 团队共享配置

把团队的代码规范写成配置文件——不用改任何代码。

- **`.mcp-code-review.yaml` / `.yml` / `.json`** — 从被审查文件所在目录向上自动发现；片段和 diff 则从服务器工作目录查找
- **`MCP_CODE_REVIEW_CONFIG` 环境变量** — 让每个同事都指向同一份共享配置（团队规则档案）
- **自定义正则规则** — 可设置严重度、说明和修复建议
- **`disabled_checks`** — 关掉吵闹的检查
- **`severity_overrides`** — 调高或调低任意检查（例如把硬编码密钥设为阻断级）
- **`min_severity`** — 只报告达到阈值的发现（按仓库降噪）

### `.mcp-code-review.yaml` 示例

```yaml
disabled_checks:
  - todo_comment

severity_overrides:
  hardcoded_secret: critical

min_severity: medium

custom_rules:
  - name: no-console-log
    pattern: 'console\.log\('
    severity: high
    category: quality
    issue: Console logging left in production code
    fix: Use a structured logger instead
```

注意：正则建议用单引号包裹；严重度可选 `critical` / `high` / `medium` / `info`。

### 团队配置

把文件提交到共享仓库，然后让每个同事的 MCP 客户端指向它：

```json
{
  "mcpServers": {
    "code-review": {
      "command": "uvx",
      "args": ["--with", "mcp<2", "aicraft-code-review"],
      "env": {
        "MCP_CODE_REVIEW_CONFIG": "/path/to/team-repo/.mcp-code-review.yaml"
      }
    }
  }
}
```

## 开源与授权

- 仓库：<https://github.com/GoodJobwilliam/aicraft/tree/main/products/mcp-code-review>
- 协议：MIT，免费安装使用
- 可选支持：$49 终身授权用于资助开发，并解锁终身更新与邮件支持（[aicraft.vip/zh.html](https://aicraft.vip/zh.html)）
- 中文分发复盘：《0 预算把 MCP 工具铺到 12 个分发渠道》见 <https://aicraft.vip/blog/distribution-playbook.html>
