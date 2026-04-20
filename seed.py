"""
Exceedingly simple performance/stress-testing program.
Run to populate app with large amounts of dummy data.
"""

import random
import sqlite3

from datetime import datetime

con = sqlite3.connect("database.db")

# Make sure to run `flask run` at least once before
con.execute("DELETE FROM Likes")
con.execute("DELETE FROM Comments")
con.execute("DELETE FROM PostCategories")
con.execute("DELETE FROM Tags")
con.execute("DELETE FROM Friends")
con.execute("DELETE FROM Posts")
con.execute("DELETE FROM Users")
con.commit()

con.execute("PRAGMA foreign_keys = ON")

USER_COUNT = 10_000
POST_COUNT = 1_000_000
COMMENT_COUNT = 3_000_000
LIKE_COUNT = 50_000_000
TAG_COUNT = 600_000
FRIEND_COUNT = 70_000

USER_CREATE_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
POST_CREATE_TIME = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
TAGS = ["mardröm", "klardröm", "vision", "hallucination"]

errs = 0

try:
    for i in range(USER_COUNT):
        con.execute("""
            INSERT INTO Users (username, created_at)
            VALUES (?, ?)
        """, [f"user{i+1}", USER_CREATE_TIME])

    con.commit()
    user_ids = list(range(USER_COUNT))
    for i in range(POST_COUNT):
        user = random.choice(user_ids)
        con.execute("""
            INSERT INTO Posts (user_id, post_time, title, sleep_quality,
                            dream, visibility, bedtime, sleep_delay)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            user+1, POST_CREATE_TIME, f"Inlägg {i}", 
            random.randint(1, 5), "dröm", "public", 
            POST_CREATE_TIME, random.randint(0, 775)
        ])

    post_ids = list(range(POST_COUNT))

    con.commit()
    for i in range(COMMENT_COUNT):
        pid = random.choice(post_ids) + 1
        uid = random.choice(user_ids) + 1
        con.execute("""
            INSERT INTO Comments (post_id, user_id, content)
                VALUES (?, ?, ?)""", [pid, uid, "Hello!"])

    con.commit()
    for i in range(LIKE_COUNT):
        pid = random.choice(post_ids) + 1
        uid = random.choice(user_ids) + 1
        con.execute("INSERT INTO Likes (post_id, user_id) VALUES (?, ?)",
            [pid, uid])

    con.commit()    
    for i in range(TAG_COUNT):
        pid = random.choice(post_ids) + 1
        tag = random.choice(TAGS)
        con.execute("INSERT INTO Tags (post_id, tag) VALUES (?, ?)",
            [pid, tag])

    con.commit()

    i = 0
    friends = set()
    while len(friends) < FRIEND_COUNT:
        if i > FRIEND_COUNT * 2:
            break
        i += 1

        a = random.choice(user_ids)
        b = random.choice(user_ids)

        if a == b:
            continue

        con.execute("""
            INSERT INTO Friends (user_id, friend_id)
                VALUES (?, ?)
        """, [a, b])

    con.commit()
    cats = con.execute("""
            SELECT category, choice 
            FROM Categories"""
        ).fetchall()

    for i in range(POST_COUNT):
        pid = random.choice(post_ids)
        con.execute("""
            INSERT INTO PostCategories (post_id, category, choice)
                VALUES (?, ?, ?)""", [pid, cat[0], cat[1]])
except Exception:
    errs += 1

con.commit()
con.close()
print(f"Completed with {errs} errors")