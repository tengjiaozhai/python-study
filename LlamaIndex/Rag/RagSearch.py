# RAG检索
import os
import sys

# 添加父目录到路径，以便导入 Utils
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from Rag.Utils import llama_llm, llama_embed_model

# 配置全局设置
Settings.llm = llama_llm
Settings.embed_model = llama_embed_model

# 获取文档目录
doc_dir = os.path.join(current_dir, "doc")

# 加载文档
documents = SimpleDirectoryReader(input_dir=doc_dir).load_data()
index = VectorStoreIndex.from_documents(documents)

# 构建索引，一次检索出4个文档切片，默认为2
query_engine = index.as_query_engine(similarity_top_k=4)
response = query_engine.query("王芳是哪个部门的")
print(response)
