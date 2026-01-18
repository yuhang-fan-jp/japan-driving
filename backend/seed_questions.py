from app.db import get_db

questions = [
    (
        "前方有铁路道口时，必须减速确认安全。",
        "https://example.com/q1.jpg",
        True,
        "铁路道口前必须减速并确认安全。"
    ),
    (
        "夜间行车时可以不开近光灯。",
        "https://example.com/q2.jpg",
        False,
        "夜间行车必须开启前照灯。"
    ),
]

db = get_db()
cursor = db.cursor()

cursor.executemany("""
INSERT INTO questions (content, image_url, correct_answer, explanation)
VALUES (?, ?, ?, ?)
""", questions)

db.commit()
db.close()

print("示例题目已插入")
