# Python CLI 项目模板（中文版）

一个生产级的 Python CLI 项目脚手架，中文文档和注释，专为中国开发者设计。

## 特点

- **Typer** 框架 — 基于 Click 的现代 CLI 框架，自动生成帮助信息
- **Rich** 终端输出 — 表格、进度条、面板、Markdown 渲染
- **Pydantic v2** 配置管理 — 类型安全的环境变量/配置文件读取
- **structlog** 结构化日志 — 开发环境彩色输出，生产环境 JSON 格式
- **httpx** 异步 HTTP — 支持重试、超时、连接池
- **pytest** 测试套件 — 含覆盖率报告、模拟对象、夹具
- **Ruff** 代码检查 — 极速 Python linter 和 formatter

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 或使用 Poetry
poetry install

# 运行 CLI
python -m cli hello --name 世界

# 查看帮助
python -m cli --help
```

## 项目结构

```
src/
├── cli/
│   ├── __init__.py
│   ├── main.py              # CLI 入口
│   └── commands/
│       ├── hello.py          # 示例命令
│       └── config.py         # 配置管理
├── core/
│   ├── __init__.py
│   ├── config.py             # Pydantic 配置
│   └── logger.py             # 日志配置
tests/
├── conftest.py               # 测试夹具
└── test_hello.py             # 示例测试
docs/
└── guide.md                  # 使用指南
```

## 使用示例

```bash
# 打招呼
python -m cli hello 张三

# 正式模式
python -m cli hello 张三 --formal

# 重复 3 次
python -m cli hello 张三 --count 3

# 显示配置
python -m cli show-config

# 查看版本
python -m cli --version
```

## 开发命令

```bash
make install    # 安装依赖
make test       # 运行测试
make lint       # 代码检查
make format     # 代码格式化
```

## 技术栈

- Python 3.11+
- [Typer](https://typer.tiangolo.com/)
- [Rich](https://rich.readthedocs.io/)
- [Pydantic v2](https://docs.pydantic.dev/)
- [structlog](https://www.structlog.org/)
- [httpx](https://www.python-httpx.org/)
- [pytest](https://docs.pytest.org/)
- [Ruff](https://docs.astral.sh/ruff/)

## 许可证

MIT License
