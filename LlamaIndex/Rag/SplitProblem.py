# rag检索优化1 拆分问题
from IPython.display import display
from llama_index.core.indices.query.query_transform.base import (
StepDecomposeQueryTransform,
)

from LlamaIndex.Rag.AssessmentAccuary import index, ground_truth

step_decompose_transform = StepDecomposeQueryTransform(verbose=True)
# set Logging to DEBUG for more detailed outputs
from llama_index.core.query_engine import MultiStepQueryEngine

query_engine = index.as_query_engine(streaming=True, similarity_top_k=5)
multi_step_query_engine = MultiStepQueryEngine(query_engine=query_engine, query_transform=step_decompose_transform,
                              index_summary="公司人员信息")
question = '查找王芳的信息'
ground_truth = '王芳是教研部的教研专员'
print(f"用户问题:{question}\n")
print("AI正在进行多不查询...")
multi_step_response = multi_step_query_engine.query(question)
print("\n参考依据:")
print("_" * 40)
for i,node in enumerate(multi_step_response.source_nodes, 1):
    print(f"第{i}个参考依据:")
    print("-" * 30)
    display(node.text)

#评估结果
print("\n评估结果:")
print("_" * 40)
print(f"AI回答:{multi_step_response.response}\n")