#Rag检索2 HyDE增强
from llama_index.core.indices.query.query_transform.base import (
HyDEQueryTransform,

)
from llama_index.core.query_engine import TransformQueryEngine

from LlamaIndex.Rag.AssessmentAccuary import index, question

hyde = HyDEQueryTransform(include_original=True)
query_engine = index.as_query_engine(streaming=True, similarity_top_k=5)
query_engine = TransformQueryEngine(query_engine=query_engine, query_transform=hyde)
print(f"用户问题:{question}\n")
print(" AI正在通过HyDE 分析...")
streaming_response = query_engine.query(question)

print("\n AI回答:")
print("_" * 40)
print(streaming_response.print_response_stream())

#显示参考文档
print("\n参考依据:")
print("_" * 40)
for i,node in enumerate(streaming_response.source_nodes, 1):
    print(f"第{i}个参考依据:")
    print("-" * 30)
    print(node.text)

print("\n AI回答:",streaming_response)
query_bundle = hyde(question)
hyde_doc = query_bundle.embedding_strs[0]
print(f" AI⽣成的假想⽂档:\n{hyde_doc}\n")