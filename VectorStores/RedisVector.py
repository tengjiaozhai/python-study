# redis数据库做向量存储
import os
import json
import numpy as np
from llama_index.core import Document
from llama_index.embeddings.dashscope import DashScopeEmbedding
from redis import Redis
from redis.exceptions import ConnectionError

# 设置通义千问API密钥
os.environ["DASHSCOPE_API_KEY"] = "sk-1f612002f98343a6891a6bf27100b282"

# 创建嵌入模型
embed_model = DashScopeEmbedding(model_name="text-embedding-v1")

try:
    # 连接Redis
    redis_client = Redis.from_url("redis://localhost:6379/")
    # 测试连接
    redis_client.ping()
    print("成功连接到Redis数据库")
except ConnectionError as e:
    print(f"无法连接到Redis数据库: {e}")
    print("请确保Redis服务器已启动并运行在localhost:6379")
    exit(1)

# 创建示例文档（在实际应用中，这里应该是您的真实文档数据）
documents = [
    Document(text="退款流程：1. 登录账户 2. 进入订单页面 3. 点击退款申请 4. 填写退款原因 5. 提交申请 6. 等待审核"),
    Document(text="退款政策：购买后7天内可申请全额退款，超过7天但未超过30天可申请部分退款，超过30天不予退款"),
    Document(text="退款到账时间：退款申请审核通过后，一般需要3-5个工作日到账，具体到账时间以银行处理为准"),
    Document(text="退款失败原因：1. 超过退款期限 2. 商品已使用 3. 退款信息填写错误 4. 银行卡状态异常"),
]

# 将文档转换为向量并存储到Redis
print("正在处理文档并存储到Redis...")
for i, doc in enumerate(documents):
    # 生成文档向量
    embedding = embed_model.get_text_embedding(doc.text)
    
    # 存储到Redis，使用文档ID作为键
    doc_id = f"doc:{i}"
    redis_client.hset(
        doc_id,
        mapping={
            "text": doc.text,
            "embedding": json.dumps(embedding)  # 将向量转换为JSON字符串存储
        }
    )
    print(f"已存储文档 {i+1}/{len(documents)}")

print("所有文档已成功存储到Redis")

# 查询函数
def query_redis(query_text, top_k=3):
    # 生成查询向量
    query_embedding = embed_model.get_text_embedding(query_text)
    
    # 获取所有文档
    all_docs = []
    for key in redis_client.scan_iter(match="doc:*"):
        doc_data = redis_client.hgetall(key)
        text = doc_data["text"].decode("utf-8")
        embedding = json.loads(doc_data["embedding"].decode("utf-8"))
        all_docs.append({"id": key.decode("utf-8"), "text": text, "embedding": embedding})
    
    # 计算相似度并排序
    for doc in all_docs:
        # 计算余弦相似度
        query_vec = np.array(query_embedding)
        doc_vec = np.array(doc["embedding"])
        similarity = np.dot(query_vec, doc_vec) / (np.linalg.norm(query_vec) * np.linalg.norm(doc_vec))
        doc["similarity"] = similarity
    
    # 按相似度排序并返回top_k结果
    sorted_docs = sorted(all_docs, key=lambda x: x["similarity"], reverse=True)[:top_k]
    return sorted_docs

# 检索相关文档
query = "怎么退款"
print(f"\n正在查询: {query}")
results = query_redis(query)

# 输出结果
print("\n查询结果:")
for i, result in enumerate(results, 1):
    print(f"{i}. 相似度: {result['similarity']:.4f}")
    print(f"   内容: {result['text']}\n")

