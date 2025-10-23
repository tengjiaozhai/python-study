#Mysql
import psycopg2
from psycopg2.extras import Json
from psycopg2.extensions import register_adapter
# 如果你想用 pgvector-python 库
# from pgvector.psycopg2 import register_vector

# 连接参数 — 根据你的 Docker 容器环境修改
conn = psycopg2.connect(
    host="120.27.157.161",        # 容器映射到主机的地址（移除了 https://）
    port=5432,               # 容器 / 主机对应的 Port（默认 PostgreSQL 是5432）
    dbname="ai-agent",
    user="tengjiao",
    password="Lcx20001201"
)

cur = conn.cursor()

# 确认 pgvector 扩展已启用（首次在数据库中运行一次即可）
cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")

# 创建一个示例表，包含 vector 类型列
cur.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id SERIAL PRIMARY KEY,
        embedding VECTOR(3)      -- 举例：3维向量
    );
""")
conn.commit()

# 插入一些向量数据
cur.execute("""
    INSERT INTO items (embedding)
    VALUES ('[1.0, 2.0, 3.0]'),
           ('[4.0, 5.0, 6.0]');
""")
conn.commit()

# 执行一个向量距离查询（例如 L2 距离，最近邻查找）
cur.execute("""
    SELECT id, embedding
    FROM items
    ORDER BY embedding <-> '[2.0, 3.0, 4.0]'
    LIMIT 3;
""")
rows = cur.fetchall()
for row in rows:
    print(row)

# 关闭连接
cur.close()
conn.close()
