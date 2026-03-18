# RAG（检索增强生成）技术指南

## 1. RAG 概述

### 1.1 什么是 RAG？

RAG（Retrieval-Augmented Generation，检索增强生成）是一种将信息检索与文本生成相结合的技术。它通过在生成回答之前先从外部知识库中检索相关信息，从而提升大语言模型的回答质量和准确性。

### 1.2 为什么需要 RAG？

**LLM 的局限性：**
- ❌ 知识截止于训练数据，无法获取最新信息
- ❌ 可能产生"幻觉"，生成不准确的内容
- ❌ 缺乏领域专业知识
- ❌ 无法访问私有数据

**RAG 的优势：**
- ✅ 可以访问最新和实时信息
- ✅ 减少幻觉，提高准确性
- ✅ 融入领域专业知识
- ✅ 利用私有数据增强能力
- ✅ 提供可追溯的信息来源

### 1.3 RAG 工作流程

```
用户查询
   ↓
┌─────────────────┐
│  查询预处理     │ → 改写、扩展、向量化
└────────┬────────┘
         ↓
┌─────────────────┐
│  检索相关文档   │ → 相似度搜索、关键词匹配
└────────┬────────┘
         ↓
┌─────────────────┐
│  结果重排序     │ → 相关性评分、去重
└────────┬────────┘
         ↓
┌─────────────────┐
│  构建增强提示词 │ → 拼接检索结果 + 原始问题
└────────┬────────┘
         ↓
┌─────────────────┐
│  LLM 生成回答    │ → 基于检索到的信息作答
└─────────────────┘
```

## 2. 核心组件详解

### 2.1 文档加载（Document Loading）

#### 支持的文档格式

**TXT 文件**
```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

**Markdown 文件**
```python
# 保留 Markdown 格式的语义结构
with open("doc.md", "r", encoding="utf-8") as f:
    content = f.read()
```

**PDF 文件**
```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("document.pdf")
documents = loader.load()
```

**其他格式：**
- Word (.docx)
- PowerPoint (.pptx)
- Excel (.xlsx)
- HTML (.html)
- JSON (.json)

### 2.2 文本分割（Text Splitting）

#### 分割策略

**按字符分割**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # 每个块的大小
    chunk_overlap=50,    # 块之间的重叠
    length_function=len,
    separators=[         # 分割优先级
        "\n\n",          # 段落
        "\n",            # 换行
        "。", "！", "？", # 中文句子
        ".", "!", "?",   # 英文句子
        "；", ";",       # 分句
        " ",             # 空格
        ""               # 字符
    ]
)
```

**为什么需要重叠？**
```
块 1: [............] 
块 2:       [............]
           ↑ 重叠部分保持上下文连续性
```

**分割最佳实践：**
1. **选择合适的 chunk_size**
   - 太小：丢失上下文
   - 太大：包含无关信息
   - 推荐：300-800 tokens

2. **设置合理的 overlap**
   - 推荐：chunk_size 的 10-20%
   - 保持语义完整性

3. **考虑文档结构**
   - 代码：按函数/类分割
   - 文章：按章节分割
   - 对话：按话轮分割

### 2.3 向量化（Embedding）

#### 嵌入模型选择

**DashScope Embeddings（阿里云）**
```python
from langchain_community.embeddings import DashScopeEmbeddings

embeddings = DashScopeEmbeddings(
    model="text-embedding-v2",
    dashscope_api_key="your-api-key"
)
```

**其他流行模型：**
- OpenAI: text-embedding-ada-002
- Cohere: embed-multilingual-v2.0
- Hugging Face: BGE, M3E 等

#### 向量维度对比

| 模型 | 维度 | 最大输入 | 性能 |
|------|------|----------|------|
| text-embedding-v2 | 1536 | 2048 tokens | 优秀 |
| text-embedding-ada-002 | 1536 | 8191 tokens | 优秀 |
| BGE-Large-zh | 1024 | 512 tokens | 良好 |

### 2.4 向量存储（Vector Store）

#### FAISS（Facebook AI Similarity Search）

**特点：**
- 🔥 高效的相似度搜索
- 📦 支持大规模向量索引
- 🚀 CPU/GPU加速
- 💾 支持持久化存储

**基本用法：**
```python
from langchain_community.vectorstores import FAISS

# 从文档创建
vectorstore = FAISS.from_documents(documents, embeddings)

# 保存索引
vectorstore.save_local("faiss_index")

# 加载索引
vectorstore = FAISS.load_local("faiss_index", embeddings)
```

**搜索方法：**
```python
# 相似度搜索
results = vectorstore.similarity_search(query, k=3)

# 带分数搜索
results = vectorstore.similarity_search_with_score(query, k=3)

# 最大边际相关（MMR）
results = vectorstore.max_marginal_relevance_search(query, k=3)
```

#### 其他向量数据库

- **Chroma**：轻量级，易于使用
- **Pinecone**：托管服务，高性能
- **Weaviate**：支持混合搜索
- **Milvus**：分布式，大规模

### 2.5 检索策略

#### 1. 相似度搜索（Similarity Search）

```python
# 余弦相似度
results = vectorstore.similarity_search(query, k=3)
```

**原理：**
- 计算查询向量与文档向量的夹角余弦值
- 返回最相似的 k 个文档

#### 2. 最大边际相关（MMR）

```python
# 平衡相关性和多样性
results = vectorstore.max_marginal_relevance_search(
    query, 
    k=3,
    fetch_k=20,  # 先取 20 个候选
    lambda_mult=0.5  # 多样性权重（0-1）
)
```

**适用场景：**
- 避免结果过于相似
- 希望获得多样化的信息

#### 3. 混合搜索（Hybrid Search）

```python
# 结合关键词搜索和语义搜索
keyword_results = keyword_search(query)
semantic_results = semantic_search(query)
final_results = merge_and_rerank(keyword_results, semantic_results)
```

## 3. RAG 优化技术

### 3.1 查询优化

**查询改写（Query Rewriting）**
```python
# 原始查询："Python 装饰器怎么用？"
# 改写后：["Python 装饰器的使用方法", "Python decorator 教程", "如何使用 Python 装饰器"]

def rewrite_query(query: str) -> List[str]:
    # 使用 LLM 生成多个变体
    prompt = f"""将以下问题改写成 3 个不同的版本：
    {query}
    """
    return llm.generate(prompt)
```

**假设性问题分解**
```python
# 复杂问题 → 多个简单问题
# "如何搭建一个完整的 Web 应用？"
# → ["Web 应用的前端用什么框架？", "后端如何选择？", "数据库怎么设计？"]
```

### 3.2 文档优化

**元数据增强**
```python
for doc in documents:
    doc.metadata.update({
        "source": doc.metadata.get("source"),
        "page": doc.metadata.get("page"),
        "section": extract_section(doc),
        "keywords": extract_keywords(doc),
        "summary": generate_summary(doc)
    })
```

**分层索引**
```python
# 粗粒度索引（章节级别）
coarse_chunks = split_by_chapter(documents)

# 细粒度索引（段落级别）
fine_chunks = split_by_paragraph(documents)

# 两级检索
chapter_results = search(coarse_chunks, query)
paragraph_results = search(fine_chunks, query, filter=chapter_results)
```

### 3.3 检索优化

**自适应 k 值**
```python
def adaptive_k_search(query: str) -> List[Document]:
    # 宽泛问题：多返回一些
    if is_broad_query(query):
        k = 10
    # 具体问题：少返回一些
    else:
        k = 3
    
    return vectorstore.similarity_search(query, k=k)
```

**过滤检索**
```python
# 只检索特定来源或时间的文档
results = vectorstore.similarity_search(
    query, 
    k=3,
    filter={"source": {"$in": ["api_docs.md", "tutorial.md"]}}
)
```

### 3.4 重排序（Rerank）

**Cross-Encoder 重排序**
```python
from sentence_transformers import CrossEncoder

cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank_documents(query: str, docs: List[Document]) -> List[Document]:
    pairs = [[query, doc.page_content] for doc in docs]
    scores = cross_encoder.predict(pairs)
    
    # 按分数排序
    ranked_docs = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    
    return [doc for doc, score in ranked_docs[:5]]
```

### 3.5 上下文压缩

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectorstore.as_retriever()
)

compressed_docs = compression_retriever.invoke(query)
```

## 4. RAG 在 Agent 中的应用

### 4.1 工具封装

```python
from langchain.tools import BaseTool

class KnowledgeRetrievalTool(BaseTool):
    name: str = "knowledge_retrieval"
    description: str = """
    从本地知识库中检索相关信息。
    当用户询问特定领域的知识、技术细节、概念解释或事实性问题时使用此工具。
    输入应该是用户的查询问题，可以是中文或英文。
    """
    
    def _run(self, query: str) -> str:
        kb = KnowledgeBase()
        results = kb.search(query, k=3)
        return results
```

### 4.2 Agent 调用示例

```python
# Agent 思考过程
"""
用户问：Python 中的装饰器是什么？

思考：这是一个关于 Python 编程概念的问题，我应该使用 knowledge_retrieval 
工具来检索相关知识。

行动：knowledge_retrieval
行动输入：Python 装饰器的概念和用法

观察：[检索到的知识内容...]

思考：现在我有了关于装饰器的详细信息，我可以给用户一个全面的解释。

最终回答：[基于检索结果生成详细解答]
"""
```

### 4.3 提示词增强

```python
RAG_ENHANCED_PROMPT = """
你是一个专业的 AI 助手，可以访问外部知识库来获取准确信息。

当你遇到以下情况时，请使用 knowledge_retrieval 工具：
1. 用户询问具体的技术概念
2. 需要引用官方文档或规范
3. 涉及最新的技术动态
4. 需要领域专业知识

检索到信息后：
- 仔细阅读并理解检索内容
- 基于检索到的信息回答问题
- 引用信息来源
- 如果检索结果不充分，诚实地告诉用户

可用工具：
{tools}

开始！
"""
```

## 5. 性能评估

### 5.1 评估指标

**检索质量**
- **召回率（Recall）**：找到多少相关文档
- **精确率（Precision）**：返回的结果有多少是相关的
- **NDCG**：排序质量的综合指标

**生成质量**
- **准确性（Accuracy）**：回答是否正确
- **忠实度（Faithfulness）**：是否基于检索内容
- **相关性（Relevance）**：是否切题

### 5.2 评估方法

**人工评估**
```python
evaluation_template = """
请评估以下 RAG 系统的输出：

问题：{question}
检索到的文档：{retrieved_docs}
生成的回答：{generated_answer}

评分标准（1-5 分）：
1. 准确性：回答是否正确
2. 完整性：是否覆盖了问题的所有方面
3. 忠实度：是否基于检索内容，没有编造
4. 流畅性：表达是否清晰流畅

请给出评分和理由。
"""
```

**自动化评估**
```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)

results = evaluate(
    dataset=test_dataset,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
)
```

## 6. 常见问题与解决方案

### 6.1 检索不到相关内容

**原因：**
- 知识库中没有相关文档
- 文本分割不合理
- 嵌入模型效果不好
- 查询表述不清晰

**解决方案：**
1. 扩充知识库
2. 调整 chunk_size 和分割策略
3. 尝试不同的嵌入模型
4. 进行查询改写

### 6.2 检索结果不精确

**原因：**
- 查询太宽泛
- 向量维度不够高
- 缺少重排序步骤

**解决方案：**
1. 引导用户提出具体问题
2. 使用更高维度的嵌入模型
3. 添加重排序机制
4. 结合关键词搜索

### 6.3 生成回答偏离检索内容

**原因：**
- LLM 过度依赖自身知识
- 提示词没有强调使用检索内容
- 检索内容太多淹没关键信息

**解决方案：**
1. 优化提示词，明确要求基于检索内容回答
2. 限制检索结果数量（k=3-5）
3. 对检索结果进行摘要或压缩
4. 在提示词中高亮关键信息

### 6.4 性能瓶颈

**问题：**
- 检索速度慢
- 内存占用大
- 并发能力有限

**优化方案：**
1. 使用 GPU 加速向量计算
2. 实施缓存机制
3. 采用近似最近邻搜索（ANN）
4. 分布式部署向量数据库

## 7. 实战技巧

### 7.1 增量更新知识库

```python
class IncrementalKnowledgeBase:
    def __init__(self):
        self.vectorstore = None
        self.processed_files = set()
    
    def add_new_documents(self, new_files: List[str]):
        # 只处理新增的文件
        files_to_process = [f for f in new_files if f not in self.processed_files]
        
        if files_to_process:
            new_docs = load_documents(files_to_process)
            self.vectorstore.add_documents(new_docs)
            self.processed_files.update(files_to_process)
```

### 7.2 多知识库检索

```python
class MultiSourceRAG:
    def __init__(self):
        self.knowledge_bases = {
            "tech_docs": KnowledgeBase("knowledge/tech"),
            "api_docs": KnowledgeBase("knowledge/api"),
            "tutorials": KnowledgeBase("knowledge/tutorials")
        }
    
    def search_all(self, query: str) -> str:
        all_results = []
        for kb_name, kb in self.knowledge_bases.items():
            results = kb.search(query, k=2)
            all_results.append(f"【来自 {kb_name}】\n{results}")
        
        return "\n\n".join(all_results)
```

### 7.3 带引用的回答

```python
def generate_cited_answer(query: str, docs: List[Document]) -> str:
    # 为每个文档编号
    context_parts = []
    for i, doc in enumerate(docs, 1):
        context_parts.append(f"[{i}] {doc.page_content}\n来源：{doc.metadata['source']}")
    
    context = "\n\n".join(context_parts)
    
    prompt = f"""
    基于以下信息回答问题，并在回答中标注引用来源：
    
    {context}
    
    问题：{query}
    
    回答：
    """
    
    return llm.invoke(prompt)
```

## 8. 安全与合规

### 8.1 数据隐私

- **敏感信息过滤**：在入库前过滤个人隐私、商业机密
- **访问控制**：不同用户只能访问授权的知识库
- **审计日志**：记录所有检索和生成操作

### 8.2 版权保护

- **来源标注**：明确标注内容的来源
- **合理使用**：遵守版权法的合理使用原则
- **版权声明**：在输出中添加版权信息

### 8.3 内容审核

```python
def content_moderation(content: str) -> bool:
    # 检查敏感词
    # 检查不当内容
    # 检查虚假信息
    return is_safe(content)
```

## 9. 未来发展趋势

### 9.1 技术演进

- **Graph RAG**：结合知识图谱的 RAG
- **Multi-modal RAG**：支持图像、音频等多模态检索
- **Agentic RAG**：Agent 自主决定检索策略
- **Self-RAG**：模型自主判断何时检索

### 9.2 应用拓展

- **企业知识库**：智能客服、内部助手
- **教育领域**：个性化学习助手
- **医疗健康**：辅助诊断、药物查询
- **法律服务**：案例检索、法律咨询

## 总结

RAG 技术通过将检索与生成相结合，有效解决了 LLM 的知识局限性、幻觉问题和时效性问题。本指南涵盖了 RAG 的核心组件、优化技术、应用场景和最佳实践，希望能帮助你构建高效的 RAG 系统。

## 参考资料

- [LangChain RAG 文档](https://python.langchain.com/docs/use_cases/question_answering/)
- [FAISS 官方仓库](https://github.com/facebookresearch/faiss)
- [RAGAS 评估框架](https://github.com/explodinggradients/ragas)
- [Graph RAG 论文](https://arxiv.org/abs/2404.16130)
