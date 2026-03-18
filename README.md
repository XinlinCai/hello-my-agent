# 🤖 我的 Agent 系统

基于 **LangGraph** 和 **阿里云千问模型（Qwen）** 构建的多 Agent 智能对话系统，支持 RAG 知识库检索、多工具调用和模块化扩展。

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ 特性亮点

- 🚀 **现代化架构** - 采用 LangGraph 框架，支持多参数工具调用和 ReAct 模式
- 🇨🇳 **国产模型** - 使用阿里云 DashScope 千问大模型（Qwen-Max）
- 🎯 **多 Agent 协同** - 通用问答 + 旅行规划 + 编程专家三 Agent
- 🔧 **易于扩展** - 模块化设计，支持自动发现工具和快速添加新 Agent
- 💬 **自然交互** - 简洁的命令行界面，支持智能切换和思考过程显示
- 📝 **提示词管理** - 统一的提示词模板管理系统
- 🧠 **RAG 增强** - 本地知识库检索，支持 PDF/TXT/MD 文档
- ⚡ **性能优化** - 知识库预加载、向量库缓存、全局单例管理

## 📋 功能特性

### 1️⃣ 通用问答 Agent
- 日常聊天对话
- 知识问答（支持 RAG 知识库检索）
- 数学计算（内置计算器工具）
- 逻辑推理与问题解决
- 创意写作协助
- 代码编程指导
- 执行 Python 代码、验证语法、格式化代码

### 2️⃣ 旅行规划 Agent
- 🗺️ 目的地信息查询
- 💰 旅行预算计算（经济型/舒适型/豪华型）
- 🌤️ 天气查询服务
- 📅 行程规划建议
- 🍜 当地文化和美食推荐
- 🎫 景点门票和活动安排

### 3️⃣ 编程专家 Agent
- 💻 代码编写和调试
- 🐛 Bug 定位和修复
- 🏗️ 架构设计咨询
- 🔍 代码质量分析
- 📊 性能优化建议
- 📚 技术文档查询（RAG）

### 4️⃣ 预定义特色 Agent（可扩展）
- 🌸 **林黛玉 Agent** - 古典文学风格，诗词歌赋
- 🤖 **自定义 Agent** - 根据需求快速定制

## 🏗️ 项目结构

```
hello-my-agent/
├── config/                      # 配置模块
│   └── settings.py              # 环境变量和路径配置
├── src/
│   ├── agents/                  # Agent 模块
│   │   ├── general_agent.py     # 通用问答 Agent（支持 RAG）
│   │   ├── travel_agent.py      # 旅行规划 Agent
│   │   └── coding_assistant_agent.py  # 编程专家 Agent
│   ├── tools/                   # 工具模块
│   │   ├── __init__.py          # 工具管理和自动发现
│   │   ├── calculator_tool.py   # 计算器工具
│   │   ├── travel_tools.py      # 旅行工具集
│   │   └── code_tools.py        # 编程辅助工具集
│   ├── core/                    # 核心模块
│   │   ├── prompts/             # 提示词管理
│   │   │   ├── __init__.py      # 提示词接口
│   │   │   └── templates.py     # 提示词模板定义
│   │   ├── llm.py               # 模型管理（预留）
│   │   └── memory..py           # 记忆模块（预留）
│   ├── rag/                     # RAG 知识库模块
│   │   ├── __init__.py          # RAG 接口
│   │   ├── knowledge_base.py    # 知识库核心（文档加载、向量化）
│   │   └── retriever.py         # 检索工具（Agent 调用）
│   └── main.py                  # 主程序入口
├── knowledge/                   # 知识库文档目录
│   ├── agent_basics.md          # Agent 基础知识
│   └── rag_technology.md        # RAG 技术文档
├── tests/                       # 测试用例
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

6. **验证安装**

启动后会自动初始化 RAG 知识库，并显示可用 Agent 列表。

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

| 命令 | 功能 | 说明 |
|------|------|------|
| `1` / `1️⃣` | 切换到通用问答 Agent | 聊天、知识问答、计算 |
| `2` / `2️⃣` | 切换到旅行规划 Agent | 行程规划、预算、天气 |
| `3` / `3️⃣` | 切换到编程专家 Agent | 代码编写、调试、优化 |
| `h` / `help` / `帮助` | 显示帮助信息 | 查看使用指南 |
| `v` | 切换思考过程显示 | 开启/关闭 AI 推理过程展示 |
| `refresh` | 刷新知识库 | 更新本地文档后重新加载 |
| `q` / `quit` / `exit` | 退出程序 | 安全退出系统 |

### 使用示例

#### 通用问答 Agent（带思考过程）

```
[通用问答] 请输入你的问题：什么是 RAG 技术？

⏳ 通用 Agent 正在思考中...

======================================================================
🧠 通用 Agent 思考链路
======================================================================

👤 用户问题:
   什么是 RAG 技术？

💭 思考决策:
   🔹 使用方法：knowledge_retrieval
   🔹 调用参数：{'query': 'RAG 技术'}

✅ 方法执行结果:
   RAG（Retrieval-Augmented Generation）是一种检索增强生成技术...
   (结果长度：1250 字符)

📊 方法调用统计:
   • knowledge_retrieval: 1 次

======================================================================

💬 通用问答 Agent 回答:
RAG（Retrieval-Augmented Generation）即检索增强生成，是一种结合...
```

#### 编程专家 Agent

```
[编程专家] 请输入你的问题：如何用 Python 实现快速排序？

⏳ 编程专家 Agent 正在思考中...

💬 编程专家 Agent 的回答:
### 问题分析
快速排序是一种高效的分治算法...

### 解决方案
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

### 代码说明
- 基准值选择：取中间元素
- 分区操作：小于、等于、大于基准值
- 递归排序：对左右子数组递归调用

### 运行示例
```python
arr = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(arr))  # 输出：[1, 1, 2, 3, 6, 8, 10]
```
```

## 🔧 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| **LLM** | Qwen-Max (ChatTongyi) | 阿里云千问大模型 |
| **Agent 框架** | LangGraph | 新一代 Agent 编排框架，支持 ReAct 模式 |
| **工具定义** | StructuredTool / @tool / BaseTool | 支持单参数和多参数工具 |
| **RAG 引擎** | FAISS + LangChain | 向量数据库和文档处理 |
| **嵌入模型** | text-embedding-v2 | DashScope 嵌入模型 |
| **环境管理** | python-dotenv | 环境变量加载 |
| **核心库** | langchain, langchain_classic | LangChain 生态 |
| **消息处理** | langchain_core.messages | SystemMessage, HumanMessage |
| **文档加载** | PyPDFLoader, TextLoader | 支持 PDF/TXT/MD 格式 |

## 📐 架构设计

### 核心模块

1. **Agent 层** (`src/agents/`)
   - 负责业务逻辑和工具调用
   - 使用 `create_react_agent()` 创建 ReAct 模式 Agent
   - 支持系统提示词定制
   - 三个专用 Agent：通用、旅行、编程

2. **工具层** (`src/tools/`)
   - 封装具体功能实现
   - 支持单参数（`@tool`）和多参数（`StructuredTool`）
   - 统一导出管理
   - 支持自动发现和去重机制

3. **提示词层** (`src/core/prompts/`)
   - 统一管理所有 Agent 的系统提示词
   - 提供提示词模板和获取接口
   - 支持快速扩展新 Agent 类型

4. **RAG 层** (`src/rag/`)
   - **KnowledgeBase**: 文档加载、切分、向量化
   - **Retriever**: 知识检索工具（供 Agent 调用）
   - **全局单例**: 启动预加载，避免重复初始化
   - **支持格式**: PDF, TXT, Markdown

5. **配置层** (`config/`)
   - API Key 管理
   - 环境变量加载
   - 路径配置管理

### 工作流程

```
用户输入 → main.py → 选择 Agent → 加载提示词 → LangGraph Agent 
         → 调用工具（计算器/旅行/编程/RAG） → 返回结果
```

### RAG 工作流程

```
知识库文档 → 文档加载 → 文本切分 → 向量化 → FAISS 索引
                                    ↓
用户查询 ← 相似度搜索 ← 向量查询 ← Agent 调用 ← 触发检索
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

#### 工具自动发现机制

工具模块支持自动发现，无需手动注册：
- 默认排除 `example_*`, `test_*`, `_*.py` 文件
- 通过工具名称去重，避免重复加载
- 可在 `general_agent.py` 中配置发现策略

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
from src.tools import discover_tools

load_dotenv()

# 初始化模型
llm = ChatTongyi(
    dashscope_api_key=DASHSCOPE_API_KEY,
    model_name="qwen-max",
    temperature=0.7,
    max_tokens=1500
)

# 导入工具（可使用自动发现或手动指定）
tools = discover_tools(auto_discover=True, verbose=False)

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
    "programming_expert": PROGRAMMING_EXPERT_AGENT_PROMPT,
    "my_custom": MY_CUSTOM_AGENT_PROMPT,  # 新增
}
```

#### 步骤 3：在主程序中集成

修改 `src/main.py`，添加新的 Agent 选项：

```python
# 在菜单中添加选项
print("   🎨  [4] 自定义 Agent（功能描述）")

# 在切换逻辑中添加
elif user_input in ['4', '4️⃣']:
    current_agent = "my_custom"
    print_agent_switch("自定义", "🎨")
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

### RAG 配置

在 `src/rag/knowledge_base.py` 中调整：

```python
class KnowledgeBase:
    def __init__(
        self, 
        knowledge_dir: str = None,
        chunk_size: int = 500,     # 文本块大小
        chunk_overlap: int = 50    # 文本块重叠量
    ):
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
- **自动发现**：默认启用，可配置排除规则

## 🎯 最佳实践

### 工具设计原则

1. **单一职责**：每个工具只做好一件事
2. **清晰描述**：工具描述要详细准确，帮助 LLM 理解何时调用
3. **参数明确**：多参数工具要说明每个参数的作用和默认值
4. **错误处理**：工具内部要处理异常情况，返回友好错误信息
5. **命名规范**：工具名称应简洁明了，体现功能用途

### 提示词编写技巧

1. **角色定义**：清晰定义 Agent 的身份和专业领域
2. **能力边界**：明确说明能做什么，不能做什么
3. **格式规范**：指定输出的结构和格式要求
4. **风格指导**：定义语言风格和语气特点
5. **工具说明**：详细列出可用工具及其使用场景

### 性能优化建议

1. **合理设置 max_tokens**：根据任务复杂度调整
2. **temperature 调优**：事实性问题用低值，创意性内容用高值
3. **工具精简**：只添加必要的工具，减少 LLM 选择负担
4. **RAG 预加载**：启动时完成向量库构建，避免首次查询延迟
5. **全局单例**：知识库使用全局实例，避免重复加载

### RAG 最佳实践

1. **文档质量**：确保文档内容清晰、结构化
2. **切分策略**：根据文档类型调整 chunk_size 和 overlap
3. **来源标注**：为检索结果添加来源，便于追溯
4. **定期更新**：及时刷新知识库保持信息最新

## 📝 常见问题

### Q: 如何获取 API Key？

A: 访问 [阿里云 DashScope 控制台](https://dashscope.console.aliyun.com/) 注册并获取 API Key。

### Q: 支持哪些模型？

A: 目前支持阿里云千问系列模型（qwen-turbo, qwen-max, qwen-plus 等），可在 Agent 配置文件中切换。

### Q: 可以添加自己的工具吗？

A: 当然可以！参考「扩展开发」部分，轻松添加自定义工具。工具支持自动发现机制，无需手动注册。

### Q: LangGraph 有什么优势？

A: 
- ✅ 支持多参数工具调用
- ✅ 现代化的消息传递架构
- ✅ 更好的状态管理
- ✅ 官方长期支持
- ✅ 支持 ReAct 模式（推理 + 行动）

### Q: RAG 知识库如何使用？

A: 
1. 将文档（PDF/TXT/MD）放入 `knowledge/` 目录
2. 启动程序会自动加载
3. Agent 会自动调用 `knowledge_retrieval` 工具检索相关信息

### Q: 如何更新知识库？

A: 
- 方式 1：重启程序
- 方式 2：在命令行输入 `refresh` 命令
- 方式 3：代码中调用 `kb.clear_cache()` 后重新加载

### Q: 思考过程显示有什么用？

A: 
- 🔍 了解 AI 的推理过程
- 🛠️ 查看工具调用情况
- 📊 统计方法使用频率
- 🎓 学习和调试 Agent 行为
- 可通过 `v` 命令开关

## 📄 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件

## 🤝 贡献

欢迎提出建议和改进意见！可以通过以下方式参与：

- 🐛 提交 Issue 报告问题
- 💡 提出新功能建议
- 🔧 提交 Pull Request 改进代码
- 📖 完善文档

## 📮 联系方式

如有问题，请通过以下方式联系：

- GitHub Issues
- 项目讨论区

## 🌟 致谢

感谢以下开源项目：

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [阿里云 DashScope](https://www.aliyun.com/product/dashscope)
- [FAISS](https://github.com/facebookresearch/faiss)

---

**🎉 享受你的 AI Agent 之旅！**

> Built with ❤️ using LangGraph + Qwen
