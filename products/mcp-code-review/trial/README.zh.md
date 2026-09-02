# MCP Code Review：10 分钟团队试用

这个免费的本地试用包可以让小团队在讨论付费 Team Rules Pack 或 Team Updates 前，先验证共享审查规则。源代码不会离开本机，运行命令也不会产生收费。

## 1. 安装

```bash
uvx --from aicraft-code-review --with "mcp<2" mcp-code-review
```

或者在已有 Python 环境中安装当前 PyPI 版本：

```bash
pip install "aicraft-code-review==0.1.2" "mcp<2"
```

## 2. 运行示例

在这个目录执行：

```bash
mcp-code-review review-file sample.py
```

也可以使用试用包自带的启动脚本；它会先检查 uvx，再执行同一条审查命令：

```bash
./run-trial.sh
```

相邻的 `.mcp-code-review.json` 会自动发现。你应该看到一个 High 级别的命令注入问题和一个 Medium 级别的团队规范问题；非零退出码可以直接用于合并门禁。

## 3. 试用自己的文件

把 `.mcp-code-review.json` 复制到测试仓库，按团队规范修改 `custom_rules` 的正则、严重度和提示，然后运行：

```bash
mcp-code-review review-file path/to/file.py
```

如果所有同事都需要使用同一份配置，可以把 `MCP_CODE_REVIEW_CONFIG` 指向共享 JSON 文件。这个配置同时适用于 Claude Code、Cursor、Cline 和 CLI。

## 4. 判断是否存在团队问题

完成一次审查后，讨论：

- 是否在合并前发现了真实问题？
- 哪条规则应该在所有仓库共享？
- 哪些结果属于误报或遗漏？
- 每月规则更新、CI 工作流刷新或上线支持是否能节省审查时间？

如果答案指向持续的团队需求，可以提交[中文结构化试用反馈](https://github.com/GoodJobwilliam/aicraft/issues/new?template=trial-feedback-zh.yml&title=%5B%E8%AF%95%E7%94%A8%E5%8F%8D%E9%A6%88%5D)，或使用[中文团队试用申请表](https://github.com/GoodJobwilliam/aicraft/issues/new?template=team-trial-zh.yml&title=%5B%E5%9B%A2%E9%98%9F%E8%AF%95%E7%94%A8%5D)开始一次引导式团队测试。填写团队规模、语言、流程和痛点即可。请勿提交源代码或密钥。

可选的 **Team Rules Pack** 为一次性 `$49`，可[通过 Creem 安全结算](https://creem.io/checkout/prod_6Z3S3jGNPsCyRSqNi397ZY/ch_6wLlsvodjjvKq73eBpZCP0)。**Team Updates Starter** 是最多 3 人的 `$19/月` 或 `$190/年`；**Team Pilot** 是最多 10 人的 `$99/月` 或 `$990/年`，包含 CI 和调优支持。收费前会先确认范围和开始时间。

English: [README.md](./README.md)
