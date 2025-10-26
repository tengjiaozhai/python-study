# 工具函数模块
import os
from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels
from llama_index.embeddings.dashscope import (
    DashScopeEmbedding,
    DashScopeTextEmbeddingModels,
)

# 设置通义千问API密钥
api_key = "sk-1f612002f98343a6891a6bf27100b282"
os.environ["DASHSCOPE_API_KEY"] = api_key

# LlamaIndex 使用的 LLM 和 Embeddings（用于 RAG）
llama_llm = DashScope(model_name=DashScopeGenerationModels.QWEN_MAX, api_key=api_key)
llama_embed_model = DashScopeEmbedding(
    model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V3, api_key=api_key
)


# Ragas 使用的 LLM 和 Embeddings（用于评估）- 延迟导入
def get_ragas_models():
    """延迟导入 ragas 相关模块，避免导入冲突"""
    from ragas.llms import LangchainLLMWrapper
    from ragas.embeddings import LangchainEmbeddingsWrapper
    from langchain_community.llms import Tongyi
    from langchain_community.embeddings import DashScopeEmbeddings

    ragas_llm = LangchainLLMWrapper(
        Tongyi(model_name="qwen-max", dashscope_api_key=api_key)
    )
    ragas_embeddings = LangchainEmbeddingsWrapper(
        DashScopeEmbeddings(model="text-embedding-v3", dashscope_api_key=api_key)
    )

    return ragas_llm, ragas_embeddings


# 为了向后兼容，提供获取 ragas 模型的函数
def get_llm_and_embeddings():
    """获取 ragas 评估用的 LLM 和 Embeddings"""
    return get_ragas_models()
