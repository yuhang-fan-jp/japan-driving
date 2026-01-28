from app.database import engine
from app.models import Base

def init_db():
    print("📦 开始初始化数据库表结构...")

    Base.metadata.create_all(bind=engine)

    print("✅ 数据库初始化完成")

if __name__ == "__main__":
    init_db()