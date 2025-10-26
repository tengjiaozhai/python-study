# 准确性评估
import os
from ragas import evaluate, EvaluationDataset, SingleTurnSample
from ragas.metrics import answer_correctness
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_community.llms import Tongyi
from langchain_community.embeddings import DashScopeEmbeddings

# 设置通义千问API密钥
api_key = "sk-1f612002f98343a6891a6bf27100b282"
os.environ["DASHSCOPE_API_KEY"] = api_key

# 使用 langchain 包装的 LLM 和 Embeddings
llm = LangchainLLMWrapper(Tongyi(model_name="qwen-max", dashscope_api_key=api_key))
embeddings = LangchainEmbeddingsWrapper(DashScopeEmbeddings(model="text-embedding-v3", dashscope_api_key=api_key))

# 创建评估样本
samples = [
    SingleTurnSample(
        user_input='王芳是哪个部门的',
        response='无法确定王芳所属的部门，因为提供的信息中没有提到名为"王芳"的人员',
        reference='王芳是教研部成员'
    ),
    SingleTurnSample(
        user_input='王芳是哪个部门的',
        response='王芳是人事部门的',
        reference='王芳是教研部成员'
    ),
    SingleTurnSample(
        user_input='王芳是哪个部门的',
        response='王芳是教研部的',
        reference='王芳是教研部成员'
    ),
]

# 创建评估数据集
dataset = EvaluationDataset(samples=samples)

# 评估模型准确性
print("正在评估模型准确性...")
score = evaluate(
    dataset=dataset,
    metrics=[answer_correctness],
    llm=llm,
    embeddings=embeddings
)

# 打印评估结果
print("\n评估结果:")

# 转换为DataFrame以便查看详细信息
df = score.to_pandas()
print(df)

# 打印每一行的详细得分
print("\n详细得分:")
for i, row in df.iterrows():
    print(f"\n样本 {i+1}:")
    print(f"问题: {samples[i].user_input}")
    print(f"回答: {samples[i].response}")
    print(f"参考答案: {samples[i].reference}")
    print(f"答案正确性得分: {row['answer_correctness']:.4f}")
