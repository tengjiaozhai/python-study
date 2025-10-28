#重排序 精排
# 使用阿里云百炼的排序模型
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.postprocessor.dashscope_rerank import DashScopeRerank

from LlamaIndex.Rag.AssessmentAccuary import index, question

rerank_query_engine = index.as_query_engine(
    # 设置一个较大的召回切片数量
    similarity_top_k=20,
    streaming=True,
    node_postprocessor=[
        # 在rerank模型中选择你想召回的切片个数
        DashScopeRerank(top_n=3, model='gte-rerank', api_key='sk-1f612002f98343a6891a6bf27100b282'),
        # 设置一个相似度阈值，地域该阈值的切片过滤
        SimilarityPostprocessor(similarity_cutoff=0.2)
    ]
)
reranked_response = rerank_query_engine.query(question)
#显示参考文档
print("\n参考依据:")
print("_" * 40)
for i,node in enumerate(reranked_response.source_nodes, 1):
    print(f"第{i}个参考依据:")
    print("-" * 30)
    print(node.text)

#评估结果
print("\n评估结果:")
print("_" * 40)
# 对于流式响应，需要先获取完整响应文本
response_text = ""
for text in reranked_response.response_gen:
    response_text += text
print(f"AI回答:{response_text}\n")
