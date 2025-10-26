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
    print("\n📋 评估数据集:")
    print("-" * 60)
    # 使用pandas DataFrame格式化输出
    import pandas as pd
    df = pd.DataFrame({
        '问题': data_samples['question'],
        '系统回答': data_samples['answer'],
        '标准答案': data_samples['ground_truth'],
        '检索文档数': [len(data_samples['contexts'][0])]
    })
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
print("=" * 60)
ground_truth = "王芳是教研部的教研专员"
result = evaluate_result(question, response, ground_truth)

# 第7步：美化输出评估结果表格
print("\n📊 详细评估结果表格:")
print("=" * 60)

# 设置 pandas 显示选项
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 50)

# 创建一个更易读的结果表格
result_display = result.copy()

# 如果有 contexts 列，简化显示
if 'retrieved_contexts' in result_display.columns:
    result_display['retrieved_contexts'] = result_display['retrieved_contexts'].apply(
        lambda x: f"[{len(x)} 个文档片段]" if isinstance(x, list) else str(x)[:30] + "..."
    )

# 简化 response 和 reference 列的显示
if 'response' in result_display.columns:
    result_display['response'] = result_display['response'].apply(
        lambda x: str(x)[:40] + "..." if len(str(x)) > 40 else str(x)
    )
if 'reference' in result_display.columns:
    result_display['reference'] = result_display['reference'].apply(
        lambda x: str(x)[:40] + "..." if len(str(x)) > 40 else str(x)
    )

print(result_display.to_string(index=False))

# 第8步：提取并显示各项指标
print("\n" + "=" * 60)
print("📈 评估指标详情:")
print("=" * 60)

answer_correctness_score = result["answer_correctness"].values[0]

# 创建指标汇总表
metrics_summary = pd.DataFrame({
    '指标名称': ['答案正确性 (Answer Correctness)'],
    '得分': [f'{answer_correctness_score:.4f}'],
    '百分比': [f'{answer_correctness_score * 100:.2f}%'],
    '评级': ['优秀' if answer_correctness_score >= 0.9 
             else '良好' if answer_correctness_score >= 0.7 
             else '中等' if answer_correctness_score >= 0.5 
             else '需要改进']
})

print(metrics_summary.to_string(index=False))

# 第9步：答案对比表格
print("\n" + "=" * 60)
print("� 答案对比分析):")
print("=" * 60)

comparison_df = pd.DataFrame({
    '类型': ['标准答案', '系统回答'],
    '内容': [ground_truth, str(response)],
    '长度': [len(ground_truth), len(str(response))],
    '匹配度': ['-', f'{answer_correctness_score * 100:.2f}%']
})
print(comparison_df.to_string(index=False))

# 第10步：给出综合评价和建议
print("\n" + "=" * 60)
print("💡 综合评价:")
print("=" * 60)

if answer_correctness_score >= 0.9:
    evaluation = "优秀 ⭐⭐⭐⭐⭐"
    suggestion = "系统回答非常准确，与标准答案高度一致。"
    emoji = "🎉"
elif answer_correctness_score >= 0.7:
    evaluation = "良好 ⭐⭐⭐⭐"
    suggestion = "系统回答基本准确，但可能在细节上与标准答案有些差异。"
    emoji = "👍"
elif answer_correctness_score >= 0.5:
    evaluation = "中等 ⭐⭐⭐"
    suggestion = "系统回答部分正确，建议优化检索策略或增加相关文档。"
    emoji = "⚠️"
else:
    evaluation = "需要改进 ⭐⭐"
    suggestion = "系统回答与标准答案差异较大，需要检查文档质量和检索算法。"
    emoji = "❌"

print(f"{emoji} 评级: {evaluation}")
print(f"📝 建议: {suggestion}")
print(f"📊 准确率: {answer_correctness_score * 100:.2f}%")

# 第11步：检索质量分析
print("\n" + "=" * 60)
print("📚 检索质量分析:")
print("=" * 60)
print(f"检索到的文档数量: {len(response.source_nodes)}")
print(f"使用的文档数量: {len([node for node in response.source_nodes])}")

# 显示每个检索文档的相关性（如果有分数）
if hasattr(response.source_nodes[0], 'score') and response.source_nodes[0].score is not None:
    print("\n各文档相关性得分:")
    for i, node in enumerate(response.source_nodes, 1):
        print(f"  文档 {i}: {node.score:.4f}")
else:
    print("(未提供文档相关性得分)")

print("=" * 60)
