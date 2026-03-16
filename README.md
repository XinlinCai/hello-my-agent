# 🤖 我的 Agent 系统

基于 **LangGraph** 和 **阿里云千问模型（Qwen）** 构建的多 Agent 智能对话系统。

## ✨ 特性亮点

- 🚀 **现代化架构** - 采用 LangGraph 框架，支持多参数工具调用
- 🇨🇳 **国产模型** - 使用阿里云 DashScope 千问大模型
- 🎯 **多 Agent 协同** - 通用问答 + 旅行规划双 Agent
- 🔧 **易于扩展** - 模块化设计，可快速添加新 Agent 和工具
- 💬 **自然交互** - 简洁的命令行界面，支持智能切换

## 📋 功能特性

### 1️⃣ 通用问答 Agent
- 日常聊天对话
- 知识问答
- 数学计算（内置计算器工具）

### 2️⃣ 旅行规划 Agent
- 🗺️ 目的地信息查询
- 💰 旅行预算计算（经济型/舒适型/豪华型）
- 🌤️ 天气查询服务
- 📅 行程规划建议

## 🏗️ 项目结构

```
hello-my-agent/
├── config/                      # 配置模块
│   └── settings.py              # 环境变量加载
├── src/
│   ├── agents/                  # Agent 模块
│   │   ├── general_agent.py     # 通用问答 Agent
│   │   └── travel_agent.py      # 旅行规划 Agent
│   ├── tools/                   # 工具模块
│   │   ├── __init__.py          # 工具导出
│   │   ├── calculator_tool.py   # 计算器工具
│   │   └── travel_tools.py      # 旅行工具集
│   └── main.py                  # 主程序入口
├── .env                         # 环境变量配置
├── requirements.txt             # Python 依赖
└── README.md                    # 项目说明
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- 阿里云 DashScope API Key

### 安装步骤

1. **克隆或下载项目**
```bash
cd hello-my-agent
```

2. **创建虚拟环境（推荐）**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

4. **配置 API 密钥**

在 `.env` 文件中配置阿里云 DashScope API Key：
```env
DASHSCOPE_API_KEY=your_api_key_here
```

5. **运行程序**
```bash
python -m src.main
```

## 💡 使用指南

### 基本操作

启动程序后，你会看到以下菜单：

```
============================================================
欢迎使用我的 Agent 系统 (基于千问模型)
============================================================

📋 可用的 Agent:
  1 - 通用问答 Agent（聊天、知识问答、计算等）
  2 - 旅行规划 Agent（行程规划、预算计算、天气查询等）

💡 使用提示:
  • 输入数字 '1' 或 '2' 切换 Agent
  • 输入 'q' 退出程序
============================================================
```

### 命令说明

| 命令 | 功能 |
|------|------|
| `1` | 切换到通用问答 Agent |
| `2` | 切换到旅行规划 Agent |
| `h` | 显示帮助信息 |
| `q` | 退出程序 |

### 使用示例

#### 通用问答 Agent

```
[通用问答] 请输入你的问题：计算 123 + 456 * 789

💬 通用问答 Agent 回答：计算结果：359784
```

#### 旅行规划 Agent

```
[旅行规划] 请输入你的问题：帮我规划去北京 5 天的行程，预算中等

💬 旅行规划 Agent 回答：
北京是中国的首都，有故宫、长城、天坛等著名景点...

【北京 5 天旅行预算】(舒适型)
💰 总预算：¥3700.00

详细分解:
  🏨 住宿：¥1200.00
  🍜 餐饮：¥900.00
  🎫 门票：¥600.00
  🛍️  购物：¥300.00
  ✈️  交通：¥800.00
```

## 🔧 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| **LLM** | Qwen-Max (ChatTongyi) | 阿里云千问大模型 |
| **Agent 框架** | LangGraph | 新一代 Agent 编排框架 |
| **工具定义** | StructuredTool | 支持多参数工具 |
| **环境管理** | python-dotenv | 环境变量加载 |
| **核心库** | langchain, langchain_classic | LangChain 生态 |

## 🛠️ 扩展开发

### 添加新工具

在 `src/tools/` 目录下创建新工具文件：

```python
# src/tools/my_new_tool.py
from langchain_classic.tools import StructuredTool


def my_tool_func(param1: str, param2: int = 10) -> str:
    """工具描述"""
    # 实现逻辑
    return f"结果：{param1}, {param2}"


my_new_tool = StructuredTool.from_function(
    func=my_tool_func,
    name="my_new_tool",
    description="工具描述..."
)
```

### 添加新 Agent

1. 在 `src/agents/` 目录创建新 Agent 文件
2. 导入所需工具
3. 使用 `create_react_agent()` 创建 Agent

```python
from langgraph.prebuilt import create_react_agent
from src.tools import my_new_tool

llm = ChatTongyi(...)
tools = [my_new_tool]
agent_executor = create_react_agent(llm, tools)
```

## ⚙️ 配置说明

### 模型参数

可在 Agent 文件中调整模型参数：

```python
llm = ChatTongyi(
    dashscope_api_key=DASHSCOPE_API_KEY,
    model_name="qwen-max",      # 模型名称
    temperature=0.7,            # 创造性 (0-1)
    max_tokens=1500             # 最大输出长度
)
```

### 工具自定义

- **单参数工具**：使用 `@tool` 装饰器
- **多参数工具**：使用 `StructuredTool.from_function()`

## 📝 常见问题

### Q: 如何获取 API Key？

A: 访问 [阿里云 DashScope 控制台](https://dashscope.console.aliyun.com/) 注册并获取 API Key。

### Q: 支持哪些模型？

A: 目前支持阿里云千问系列模型（qwen-turbo, qwen-max, qwen-plus 等）。

### Q: 可以添加自己的工具吗？

A: 当然可以！参考「扩展开发」部分，轻松添加自定义工具。

### Q: LangGraph 有什么优势？

A: 
- ✅ 支持多参数工具调用
- ✅ 现代化的消息传递架构
- ✅ 更好的状态管理
- ✅ 官方长期支持

## 📄 许可证

本项目仅供学习参考使用。

## 🤝 贡献

欢迎提出建议和改进意见！

## 📮 联系方式

如有问题，请通过 Issue 反馈。

---

**🎉 享受你的 AI Agent 之旅！**
