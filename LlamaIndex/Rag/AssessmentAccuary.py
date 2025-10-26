# 准确性评估
import os
import sys

# 添加父目录到路径，以便导入 Utils
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from ragas import evaluate
from ragas.metrics import answer_correctness
from Rag.Utils import get_ragas_models, llama_llm, llama_embed_model
from datasets import Dataset
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex

# 配置 LlamaIndex 全局设置
Settings.llm = llama_llm
Settings.embed_model = llama_embed_model

# 获取 ragas 评估用的 LLM 和 Embeddings
llm, embeddings = get_ragas_models()


# 定义评估函数
def evaluate_result(question, response, ground_truth):
    """
    评估 RAG 系统的回答质量
    
    参数:
        question: 用户提出的问题
        response: RAG 系统返回的响应对象
        ground_truth: 标准答案
    
    返回:
        评估结果的 DataFrame
    """
    # 第1步：获取回答内容
    # response 对象可能有 response_txt 属性，或者直接转字符串
    if hasattr(response, "response_txt"):
        answer = response.response_txt
    else:
        answer = str(response)

    # 第2步：获取检索到的上下文
    # response.source_nodes 包含了检索到的相关文档片段
    contexts = [source_node.get_content() for source_node in response.source_nodes]

    # 第3步：构造评估数据集
    # Ragas 需要特定格式的数据
    data_samples = {
        "question": [question],  # 问题列表
        "answer": [answer],  # 系统回答列表
        "ground_truth": [ground_truth],  # 标准答案列表
        "contexts": [contexts],  # 检索到的上下文列表
    }
    dataset = Dataset.from_dict(data_samples)
    
    # 输出评估数据集表格
    print("\n评估数据集 (user_input):")
    print("-" * 40)
    # 使用pandas DataFrame格式化输出
    import pandas as pd
    df = pd.DataFrame(data_samples)
    # 对contexts列进行处理，只显示前50个字符
    df["contexts"] = df["contexts"].apply(lambda x: str(x)[:50] + "...")
    print(df.to_string(index=False))

    # 第4步：使用 Ragas 评估
    score = evaluate(
        dataset=dataset, metrics=[answer_correctness], llm=llm, embeddings=embeddings
    )

    return score.to_pandas()


# ============================================================
# 主程序：执行 RAG 检索和评估
# ============================================================

print("=" * 60)
print("RAG系统评估报告")
print("=" * 60)

# 第1步：加载文档并构建索引
doc_dir = os.path.join(current_dir, "doc")
documents = SimpleDirectoryReader(input_dir=doc_dir).load_data()
index = VectorStoreIndex.from_documents(documents)

# 第2步：创建查询引擎
query_engine = index.as_query_engine(similarity_top_k=4)

# 第3步：执行查询
question = "王芳是哪个部门的？"
response = query_engine.query(question)

# 第4步：打印问题和系统回答
print(f"\n问题: {question}")
print(f"标准答案: 王芳是教研部的教研专员")
print(f"系统回答: {response}")

# 第5步：打印检索到的上下文
print(f"\n检索到的上下文:")
for i, source_node in enumerate(response.source_nodes, 1):
    content = source_node.get_content()
    # 只显示前100个字符，避免输出过长
    preview = content[:100] + "..." if len(content) > 100 else content
    print(f"{i}. {preview}")

# 第6步：执行评估
print(f"\n评估指标:")
print("-" * 40)
ground_truth = "王芳是教研部的教研专员"
result = evaluate_result(question, response, ground_truth)
print(result)

# 第7步：提取并显示答案正确性得分
answer_correctness_score = result["answer_correctness"].values[0]
print(f"\n答案正确性得分: {answer_correctness_score:.4f}")

# 第8步：给出综合评价
if answer_correctness_score >= 0.9:
    evaluation = "优秀"
elif answer_correctness_score >= 0.7:
    evaluation = "良好"
elif answer_correctness_score >= 0.5:
    evaluation = "中等"
else:
    evaluation = "需要改进"

print(f"综合评价: {evaluation}")
print("=" * 60)
