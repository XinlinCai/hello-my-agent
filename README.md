# 🤖 Agent 智能对话系统

基于 **LangGraph** 和 **阿里云千问模型（Qwen）** 构建的多 Agent 智能对话系统，集成 RAG 知识库检索、多工具调用、记忆管理和模块化扩展能力。

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ 核心特性

- 🚀 **现代化架构** - LangGraph 框架 + ReAct 模式，支持多参数工具调用
- 🇨🇳 **国产大模型** - 阿里云 DashScope 千问系列（Qwen-Max/Plus/Turbo）
- 🎯 **多 Agent 协同** - 通用问答 + 旅行规划 + 编程专家，支持自定义扩展
- 🧠 **智能记忆系统** - 短期记忆 + 长期记忆 + 上下文工程，实现个性化对话
- 🔧 **模块化扩展** - 自动工具发现机制，5 分钟快速添加新 Agent
- 💬 **自然交互** - 简洁 CLI 界面，支持思考过程可视化
- 📚 **RAG 增强** - 本地知识库检索，支持 PDF/TXT/MD 文档
- ⚡ **性能优化** - 知识库预加载、向量库缓存、全局单例管理

## 🎯 Agent 角色

### 1️⃣ 通用问答 Agent
**定位**：全能型 AI 助手，适合日常交互

**核心能力**：
- 日常聊天对话
- 知识问答（支持 RAG 知识库检索）
- 数学计算（内置计算器工具）
- 逻辑推理与问题解决
- 创意写作协助
- 代码编程指导
- Python 代码执行、语法验证、格式化

### 2️⃣ 旅行规划 Agent
**定位**：专业旅行顾问，提供全方位出行建议

**核心能力**：
- 🗺️ 目的地信息查询
- 💰 旅行预算计算（经济型/舒适型/豪华型）
- 🌤️ 天气查询服务
- 📅 行程规划建议
- 🍜 当地文化和美食推荐
- 🎫 景点门票和活动安排

### 3️⃣ 编程专家 Agent
**定位**：资深技术架构师，10+ 年il全栈开发经验

**核心能力**：
- 💻 代码编写和调试（Python/Java/JS/Go 等）
- 🐛 Bug 定位和修复
- 🏗️ 架构设计咨询（微服务/分布式/云原生）
- 🔍 代码质量分析和性能优化
- 📚 技术文档查询（RAG）
- 🛡️ 安全性审查和最佳实践

### 🌟 特色 Agent（可扩展）

#### 林黛玉 Agent
- 🌸 古典文学风格，诗词歌赋
- 💭 敏感细腻，言辞犀利
- 📚 精通红楼梦典故

#### 自定义 Agent
- 🤖 根据需求快速定制
- 🎨 支持任意角色设定
- 🔧 灵活配置工具和能力

## 🏗️ 项目结构

```
hello-my-agent/
├── config/                      # 配置模块
│   └── settings.py              # 环境变量和路径配置
├── src/
│   ├── agents/                  # Agent 模块
│   │   ├── general_agent.py     # 通用问答 Agent（支持 RAG且带记忆系统）
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
│   │   └── memory/              # 记忆系统
│   │       ├── __init__.py      # 记忆模块接口
│   │       ├── manager.py       # 统一记忆管理器
│   │       ├── short_term.py    # 短期记忆（轮次控制）
│   │       ├── long_term.py     # 长期记忆（用户画像）
│   │       └── context_engine.py # 上下文工程（优化策略）
│   ├── rag/                     # RAG 知识库模块
│   │   ├── __init__.py          # RAG 接口
│   │   ├── knowledge_base.py    # 知识库核心（文档加载、向量化）
│   │   └── retriever.py         # 检索工具（Agent 调用）
│   └── main.py                  # 主程序入口
├── data/                        # 数据存储目录
│   └── user_profiles.json       # 用户画像文件（长期记忆）
├── knowledge/                   # 知识库文档目录
│   ├── agent_basics.md          # Agent 基础知识
│   └── rag_technology.md        # RAG 技术文档
├── tests/                       # 测试用例
│   ├── test_general_agent_rag.py
│   ├── test_long_term_optimization.py
│   └── test_memory.py
├── .env                         # 环境变量配置
├── requirements.txt             # Python 依赖
└── README.md                    # 项目说明
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- 阿里云 DashScope API Key（[获取地址](https://dashscope.console.aliyun.com/)）

### 安装步骤

1. **克隆项目**
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

编辑 `.env` 文件：
```env
# API 配置
DASHSCOPE_API_KEY=sk-your_api_key_here

# 记忆模块配置
DEFAULT_USER_ID=default_user
SHORT_TERM_MAX_TURNS=10
CONTEXT_MAX_TURNS=5
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
══════════════════════════════════════════════════════════
✨  欢迎使用我的 Agent 系统  ✨
                       (基于阿里云千问大模型)
══════════════════════════════════════════════════════════

🎯  当前可用 Agent:
   🤖  [1] 通用问答  - 聊天、知识问答、计算
   🗺️  [2] 旅行规划  - 行程规划、预算、天气
   💻  [3] 编程专家  - 代码编写、调试、优化

💡  快速上手:
   • 直接输入问题即可开始
   • 输入数字 1/2/3 切换 Agent
   • 输入 'v' 切换思考过程显示 (开/关)
   • 输入 'memory' 查看当前记忆状态 | 'clear' 清空短期记忆 | 'profile' 查看用户画像
   • 输入 'help' 查看更多帮助 | 'refresh' 刷新知识库 | 'q' 退出
══════════════════════════════════════════════════════════
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
| `memory` | 查看记忆状态 | 显示短期/长期记忆统计 |
| `clear` | 清空短期记忆 | 保留用户画像数据 |
| `reset` | 清空所有记忆 | 包括用户画像 |
| `profile` | 查看用户画像 | 显示长期记忆中的用户信息 |
| `storage` | 查看存储信息 | 显示文件路径和用户 ID |
| `q` / `quit` / `exit` | 退出程序 | 安全退出系统 |

### 使用示例

#### 通用问答 Agent（带思考过程）

```
🤖 [通用问答] 请输入你的问题：什么是 RAG 技术？

⏳ 通用 Agent 正在思考中...

══════════════════════════════════════════════════════════
🧠 通用 Agent 思考链路
══════════════════════════════════════════════════════════

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

══════════════════════════════════════════════════════════

💬 通用问答 Agent 回答:
RAG（Retrieval-Augmented Generation）即检索增强生成，是一种结合...
```

#### 编程专家 Agent

```
💻 [编程专家] 请输入你的问题：如何用 Python 实现快速排序？

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

#### 记忆系统演示

```
🤖 [通用问答] 请输入你的问题：我喜欢吃川菜

💬 通用问答 Agent 回答: 好的，我已经记住了！您喜欢吃川菜...

---
memory 命令查看记忆状态:

💾 记忆状态:
   短期记忆：3 轮对话
   长期记忆：1 条用户信息

---
profile 命令查看用户画像:

👤 用户画像:
   • 饮食偏好：川菜
```

## 🔧 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| **LLM** | Qwen-Max/Plus/Turbo | 阿里云千问大模型系列 |
| **Agent 框架** | LangGraph | 新一代 Agent 编排框架，支持 ReAct 模式 |
| **工具定义** | StructuredTool / @tool / BaseTool | 支持单参数和多参数工具 |
| **RAG 引擎** | FAISS + LangChain | 向量数据库和文档处理 |
| **嵌入模型** | text-embedding-v2 | DashScope 嵌入模型 |
| **环境管理** | python-dotenv | 环境变量加载 |
| **核心库** | langchain, langchain_classic | LangChain 生态 |
| **消息处理** | langchain_core.messages | SystemMessage, HumanMessage |
| **文档加载** | PyPDFLoader, TextLoader | 支持 PDF/TXT/MD 格式 |
| **记忆系统** | 自研 MemoryManager | 短期记忆 + 长期记忆 + 上下文工程 |

## 📐 架构设计

### 核心模块

#### 1. Agent 层 (`src/agents/`)
- **职责**：业务逻辑和工具调用
- **实现**：使用 `create_react_agent()` 创建 ReAct 模式 Agent
- **特性**：支持系统提示词定制
- **成员**：三个专用 Agent（通用、旅行、编程）

#### 2. 工具层 (`src/tools/`)
- **职责**：封装具体功能实现
- **支持**：单参数（`@tool`）和多参数（`StructuredTool`）
- **管理**：统一导出 + 自动发现机制
- **特性**：支持排除规则和去重

#### 3. 提示词层 (`src/core/prompts/`)
- **职责**：统一管理所有 Agent 的系统提示词
- **提供**：提示词模板和获取接口
- **扩展**：支持快速添加新 Agent 类型

#### 4. 记忆系统 (`src/core/memory/`)
- **短期记忆** (`short_term.py`)：维护最近 N 轮对话，默认 10 轮
- **长期记忆** (`long_term.py`)：提取并存储用户画像信息，持久化到 JSON
- **上下文工程** (`context_engine.py`)：智能拼接历史，优化 Token 使用
- **统一管理器** (`manager.py`)：提供简洁的对外接口

#### 5. RAG 层 (`src/rag/`)
- **KnowledgeBase**: 文档加载、切分、向量化
- **Retriever**: 知识检索工具（供 Agent 调用）
- **全局单例**: 启动预加载，避免重复初始化
- **支持格式**: PDF, TXT, Markdown

#### 6. 配置层 (`config/`)
- **API Key 管理**：DashScope API Key
- **环境变量**：从 `.env` 文件加载
- **路径配置**：项目根目录、知识库目录、数据目录

### 工作流程

```
用户输入 → main.py → 选择 Agent → 加载提示词 → LangGraph Agent 
         → 调用工具（计算器/旅行/编程/RAG） → 返回结果
         → 保存到记忆系统（短期 + 长期） → 更新上下文
```

### RAG 工作流程

```
知识库文档 → 文档加载 → 文本切分 → 向量化 → FAISS 索引
                                    ↓
用户查询 ← 相似度搜索 ← 向量查询 ← Agent 调用 ← 触发检索
```

### 记忆系统工作流程

```
用户输入 → 短期记忆存储（最近 N 轮）
         → 长期记忆提取（用户画像信息）
         → 上下文工程（智能拼接历史）
         → Agent 调用（携带优化后的上下文）
```

### 核心优势

- ✅ **ReAct 模式**：推理 + 行动，让 AI 先思考再执行
- ✅ **多参数工具**：支持复杂函数签名，AI 精准调用
- ✅ **记忆持久化**：用户画像永久保存，实现个性化服务
- ✅ **上下文优化**：只保留关键信息，节省 Token
- ✅ **模块化设计**：各层职责清晰，易于维护和扩展

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
- 生产环境建议设置 `verbose=False` 减少日志输出

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

### 自定义记忆系统

#### 调整记忆参数

在 `.env` 文件中配置：

```env
# 短期记忆最大轮数（默认 10）
SHORT_TERM_MAX_TURNS=15

# 上下文工程保留轮数（默认 5）
CONTEXT_MAX_TURNS=8
```

#### 自定义用户 ID

```python
# 在代码中指定用户 ID
from src.core.memory.manager import MemoryManager

memory = MemoryManager(user_id="custom_user_123")
```

### 扩展 RAG 知识库

#### 添加新文档

1. 将 PDF/TXT/MD 文件放入 `knowledge/` 目录
2. 重启程序或使用 `refresh` 命令刷新
3. Agent 会自动检索新文档内容

#### 调整切分策略

在 `src/rag/knowledge_base.py` 中：

```python
class KnowledgeBase:
    def __init__(
        self, 
        knowledge_dir: str = None,
        chunk_size: int = 500,     # 文本块大小
        chunk_overlap: int = 50    # 文本块重叠量
    ):
```

## ⚙️ 配置说明

### 环境变量配置（.env）

```env
# ========== API 配置 ==========
DASHSCOPE_API_KEY=sk-your_api_key_here

# ========== 记忆模块配置 ==========
# 默认用户 ID（用于长期记忆）
DEFAULT_USER_ID=default_user

# 短期记忆最大轮数（控制对话历史长度）
SHORT_TERM_MAX_TURNS=10

# 上下文工程保留轮数（优化 Token 使用）
CONTEXT_MAX_TURNS=5
```

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

**模型选择建议**：
- `qwen-turbo`：速度快，成本低，适合简单任务
- `qwen-max`：能力最强，适合复杂推理和代码生成
- `qwen-plus`：平衡性能和成本，适合生产环境

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

**配置建议**：
- 技术文档：chunk_size=500, chunk_overlap=50
- 对话内容：chunk_size=300, chunk_overlap=30
- 长篇文章：chunk_size=800, chunk_overlap=100

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
- **生产建议**：设置 `verbose=False` 减少日志输出

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
2. **temperature 调优**：事实性问题用低值（0.2-0.5），创意性内容用高值（0.7-0.9）
3. **工具精简**：只添加必要的工具，减少 LLM 选择负担
4. **RAG 预加载**：启动时完成向量库构建，避免首次查询延迟
5. **全局单例**：知识库使用全局实例，避免重复加载
6. **记忆管理**：定期清理短期记忆，保持上下文精炼

### RAG 最佳实践

1. **文档质量**：确保文档内容清晰、结构化
2. **切分策略**：根据文档类型调整 chunk_size 和 overlap
3. **来源标注**：为检索结果添加来源，便于追溯
4. **定期更新**：及时刷新知识库保持信息最新

### 记忆系统最佳实践

1. **个性化服务**：利用长期记忆记录用户偏好，提供定制化建议
2. **上下文优化**：使用 context_engine 智能拼接历史，节省 Token
3. **数据持久化**：定期备份 user_profiles.json 文件
4. **隐私保护**：不存储敏感信息（密码、身份证号等）

## 📝 常见问题

### Q: 如何获取 API Key？

A: 访问 [阿里云 DashScope 控制台](https://dashscope.console.aliyun.com/) 注册账号，创建 API Key 并复制到 `.env` 文件中。

### Q: 支持哪些模型？

A: 目前支持阿里云千问系列模型：
- `qwen-turbo`：速度快，成本低
- `qwen-max`：能力最强，适合复杂任务
- `qwen-plus`：平衡性能和成本

可在 Agent 配置文件中切换模型。

### Q: 可以添加自己的工具吗？

A: 当然可以！参考「扩展开发」部分，轻松添加自定义工具。工具支持自动发现机制，无需手动注册。

### Q: LangGraph 有什么优势？

A: 
- ✅ 支持多参数工具调用
- ✅ 现代化的消息传递架构
- ✅ 更好的状态管理
- ✅ 官方长期支持
- ✅ 支持 ReAct 模式（推理 + 行动）
- ✅ 清晰的思考链路可视化

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

### Q: 记忆系统如何工作？

A: 
- **短期记忆**：保存最近 10 轮对话（可配置），用于上下文理解
- **长期记忆**：提取用户画像信息（如偏好、习惯），永久保存到 JSON 文件
- **上下文工程**：智能拼接历史消息，优化 Token 使用

### Q: 思考过程显示有什么用？

A: 
- 🔍 了解 AI 的推理过程
- 🛠️ 查看工具调用情况
- 📊 统计方法使用频率
- 🎓 学习和调试 Agent 行为
- 可通过 `v` 命令开关

### Q: 如何保护用户隐私？

A: 
- 用户画像数据存储在本地 `data/user_profiles.json`
- 不会上传到任何外部服务器
- 可随时使用 `reset` 命令清空所有记忆
- 建议不要存储敏感个人信息

### Q: 生产环境需要注意什么？

A: 
- ✅ 设置 `verbose=False` 减少日志输出
- ✅ 使用 `qwen-plus` 平衡性能和成本
- ✅ 定期备份 `data/` 目录
- ✅ 监控 API 调用量和费用
- ✅ 配置合适的 max_tokens 限制

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

- [LangChain](https://github.com/langchain-ai/langchain) - LLM 应用开发框架
- [LangGraph](https://github.com/langchain-ai/langgraph) - Agent 编排框架
- [阿里云 DashScope](https://www.aliyun.com/product/dashscope) - 千问大模型 API
- [FAISS](https://github.com/facebookresearch/faiss) - 向量相似度搜索库

---

**🎉 享受你的 AI Agent 之旅！**

> Built with ❤️ using LangGraph + Qwen

---

## 📊 项目统计

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-Latest-green.svg)
![Qwen](https://img.shields.io/badge/Qwen-Max%2FPlus%2FTurbo-orange.svg)
