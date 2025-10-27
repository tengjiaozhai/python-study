# 向量存储
from sklearn.metrics.pairwise import cosine_similarity
from llama_index.embeddings.dashscope import (
DashScopeEmbedding,
DashScopeTextEmbeddingModels,
DashScopeTextEmbeddingType,
)

import numpy as np

text1 = '我喜欢吃苹果'
text2 = '苹果是最爱吃的水果'
text3 = '今天天气不错'
embedder = DashScopeEmbedding(
    model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V3,
    text_type=DashScopeTextEmbeddingType.TEXT_TYPE_DOCUMENT,
    api_key='sk-1f612002f98343a6891a6bf27100b282'
)

# 先获取嵌入向量列表，然后转换为NumPy数组并重塑
embedding1 = embedder.get_text_embedding(text1)
embedding2 = embedder.get_text_embedding(text2)
embedding3 = embedder.get_text_embedding(text3)

vector1 = np.array(embedding1).reshape(1, -1)
vector2 = np.array(embedding2).reshape(1, -1)
vector3 = np.array(embedding3).reshape(1, -1)

similarity12 = cosine_similarity(vector1, vector2)[0][0]
similarity13 = cosine_similarity(vector1, vector3)[0][0]
print(f"\"{text1}\" 和 \"{text2}\" 的相似度: {similarity12:.4f}")
print(f"\"{text1}\" 和 \"{text3}\" 的相似度: {similarity13:.4f}")
