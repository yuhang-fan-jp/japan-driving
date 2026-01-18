from app.db import get_db

db = get_db()
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    image_url TEXT,
    correct_answer BOOLEAN NOT NULL,
    explanation TEXT
)
""")

db.commit()
db.close()

print("questions 表创建完成")
