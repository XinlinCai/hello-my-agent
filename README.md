# 🤖 我的 Agent 系统

基于 **LangGraph** 和 **阿里云千问模型（Qwen）** 构建的多 Agent 智能对话系统。

## ✨ 特性亮点

- 🚀 **现代化架构** - 采用 LangGraph 框架，支持多参数工具调用
- 🇨🇳 **国产模型** - 使用阿里云 DashScope 千问大模型
- 🎯 **多 Agent 协同** - 通用问答 + 旅行规划双 Agent
- 🔧 **易于扩展** - 模块化设计，可快速添加新 Agent 和工具
- 💬 **自然交互** - 简洁的命令行界面，支持智能切换
- 📝 **提示词管理** - 统一的提示词模板管理系统

## 📋 功能特性

### 1️⃣ 通用问答 Agent
- 日常聊天对话
- 知识问答
- 数学计算（内置计算器工具）
- 逻辑推理与问题解决
- 创意写作协助
- 代码编程指导

### 2️⃣ 旅行规划 Agent
- 🗺️ 目的地信息查询
- 💰 旅行预算计算（经济型/舒适型/豪华型）
- 🌤️ 天气查询服务
- 📅 行程规划建议
- 🍜 当地文化和美食推荐
- 🎫 景点门票和活动安排

### 3️⃣ 预定义特色 Agent（可扩展）
- 🌸 **林黛玉 Agent** - 古典文学风格，诗词歌赋
- 💻 **编程专家 Agent** - 全栈开发，架构设计，代码优化

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
│   ├── core/                    # 核心模块
│   │   ├── prompts/             # 提示词管理
│   │   │   ├── __init__.py      # 提示词接口
│   │   │   └── templates.py     # 提示词模板定义
│   │   ├── llm.py               # 模型管理（预留）
│   │   └── memory..py           # 记忆模块（预留）
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
| **工具定义** | StructuredTool / @tool | 支持单参数和多参数工具 |
| **环境管理** | python-dotenv | 环境变量加载 |
| **核心库** | langchain, langchain_classic | LangChain 生态 |
| **消息处理** | langchain_core.messages | SystemMessage, HumanMessage |

## 📐 架构设计

### 核心模块

1. **Agent 层** (`src/agents/`)
   - 负责业务逻辑和工具调用
   - 使用 `create_react_agent()` 创建 ReAct 模式 Agent
   - 支持系统提示词定制

2. **工具层** (`src/tools/`)
   - 封装具体功能实现
   - 支持单参数（`@tool`）和多参数（`StructuredTool`）
   - 统一导出管理

3. **提示词层** (`src/core/prompts/`)
   - 统一管理所有 Agent 的系统提示词
   - 提供提示词模板和获取接口
   - 支持快速扩展新 Agent 类型

4. **配置层** (`config/`)
   - API Key 管理
   - 环境变量加载

### 工作流程

```
用户输入 → main.py → 选择 Agent → 加载提示词 → LangGraph Agent → 调用工具 → 返回结果
```

## 🛠️ 扩展开发

### 添加新工具

在 `src/tools/` 目录下创建新工具文件：

#### 单参数工具（使用 @tool 装饰器）

```python
# src/tools/my_single_param_tool.py
from langchain_classic.tools import tool

@tool
def my_single_param_tool(param: str) -> str:
    """工具描述，说明输入参数的作用"""
    # 实现逻辑
    return f"处理结果：{param}"
```

#### 多参数工具（使用 StructuredTool）

```python
# src/tools/my_multi_param_tool.py
from langchain_classic.tools import StructuredTool

def my_tool_func(param1: str, param2: int = 10, param3: bool = True) -> str:
    """工具描述，详细说明各参数作用"""
    # 实现逻辑
    return f"结果：{param1}, {param2}, {param3}"

my_multi_param_tool = StructuredTool.from_function(
    func=my_tool_func,
    name="my_multi_param_tool",
    description="详细描述：需要 param1（字符串），可选 param2（整数，默认 10），可选 param3（布尔值，默认 True）"
)
```

### 添加新 Agent

#### 步骤 1：创建 Agent 文件

在 `src/agents/` 目录创建新 Agent 文件：

```python
# src/agents/my_custom_agent.py
from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi
from config.settings import DASHSCOPE_API_KEY
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from src.core.prompts import get_system_prompt

load_dotenv()

# 初始化模型
llm = ChatTongyi(
    dashscope_api_key=DASHSCOPE_API_KEY,
    model_name="qwen-max",
    temperature=0.7,
    max_tokens=1500
)

# 导入工具
from src.tools import my_tool_1, my_tool_2
tools = [my_tool_1, my_tool_2]

# 获取系统提示词
system_prompt = get_system_prompt("my_custom_type")

# 创建 Agent
my_custom_agent_executor = create_react_agent(llm, tools)

def run_my_custom_agent(query: str):
    """运行自定义 Agent"""
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=query)
    ]
    response = my_custom_agent_executor.invoke({"messages": messages})
    if "messages" in response and len(response["messages"]) > 0:
        return response["messages"][-1].content
    return "抱歉，我无法回答这个问题。"
```

#### 步骤 2：添加提示词模板

在 `src/core/prompts/templates.py` 中添加新的提示词：

```python
MY_CUSTOM_AGENT_PROMPT = """你是一个专业的...

## 你的身份
- ...

## 你的能力
- ...

## 回答原则
✅ ...
"""
```

在 `src/core/prompts/__init__.py` 中注册：

```python
from .templates import MY_CUSTOM_AGENT_PROMPT

PREDEFINED_AGENTS = {
    "general": GENERAL_AGENT_SYSTEM_PROMPT,
    "travel": TRAVEL_AGENT_SYSTEM_PROMPT,
    "my_custom": MY_CUSTOM_AGENT_PROMPT,  # 新增
}
```

#### 步骤 3：在主程序中集成

修改 `src/main.py`，添加新的 Agent 选项：

```python
# 在菜单中添加选项
print("  3 - 自定义 Agent（功能描述）")

# 在切换逻辑中添加
elif user_input == '3':
    current_agent = "my_custom"
    print("✅ 已切换到自定义 Agent")
    continue

# 在调用逻辑中添加
if current_agent == "my_custom":
    from src.agents.my_custom_agent import run_my_custom_agent
    response = run_my_custom_agent(user_input)
```

## ⚙️ 配置说明

### 模型配置

可在 Agent 文件中调整模型参数：

```python
llm = ChatTongyi(
    dashscope_api_key=DASHSCOPE_API_KEY,
    model_name="qwen-max",      # 模型名称：qwen-turbo / qwen-max / qwen-plus
    temperature=0.7,            # 创造性 (0-1，越高越有创意)
    max_tokens=1500             # 最大输出长度
)
```

### 提示词定制

在 `src/core/prompts/templates.py` 中自定义各 Agent 的系统提示词，调整：
- Agent 的身份定位
- 能力和职责范围
- 回答风格和格式要求
- 工具使用规范

### 工具自定义

- **单参数工具**：使用 `@tool` 装饰器，适合简单场景
- **多参数工具**：使用 `StructuredTool.from_function()`，支持复杂参数

## 🎯 最佳实践

### 工具设计原则

1. **单一职责**：每个工具只做好一件事
2. **清晰描述**：工具描述要详细准确，帮助 LLM 理解何时调用
3. **参数明确**：多参数工具要说明每个参数的作用和默认值
4. **错误处理**：工具内部要处理异常情况，返回友好错误信息

### 提示词编写技巧

1. **角色定义**：清晰定义 Agent 的身份和专业领域
2. **能力边界**：明确说明能做什么，不能做什么
3. **格式规范**：指定输出的结构和格式要求
4. **风格指导**：定义语言风格和语气特点

### 性能优化建议

1. **合理设置 max_tokens**：根据任务复杂度调整
2. **temperature 调优**：事实性问题用低值，创意性内容用高值
3. **工具精简**：只添加必要的工具，减少 LLM 选择负担

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
