import db

def get_categories():
    query = "SELECT category, choice FROM Categories ORDER BY id"
    result = db.query(query)

    categories = {c["category"]: [] for c in result}
    for category, choice in result:
        categories[category].append(choice)

    return categories

def add(user_id, post_time, title, quality, dream, 
        visibility, bedtime, delay):
    """Adds a post to the database."""
    db.execute("""
        INSERT INTO Posts (
            user_id, post_time, title, sleep_quality,
            dream, visibility, bedtime, sleep_delay
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, [
        user_id, post_time, title, quality, dream,
        visibility, bedtime, delay
    ])

def get_posts(user_id=None, tab="latest", q=None, 
             sleep_quality=None, tags=None, cats=None):
    sql = """
        SELECT p.id, p.title, p.dream, p.sleep_quality,
               p.bedtime, p.sleep_delay,
               p.visibility, p.user_id, u.username,
               COUNT(l.id) like_count
        FROM Posts p
        INNER JOIN Users u ON p.user_id = u.id
        LEFT JOIN Likes l ON l.post_id = p.id 
    """

    conditions = []
    args = []

    vis = ["p.visibility = 'public'"]

    if user_id is not None:
        vis.append("p.visibility = 'public'")
        vis.append(
            "(p.visibility = 'private' AND p.user_id = ?)"
            )
        args.append(user_id)

        vis.append("""
            (p.visibility = 'friends-only' AND EXISTS (
                SELECT 1 FROM Friends f
                WHERE f.user_id = p.user_id AND f.friend_id = ?
            ))
        """)
        args.append(user_id)
    
    conditions = ["(" + " OR ".join(vis) + ")"]

    if tab == "friends" and user_id is not None:
        conditions.append("""
            EXISTS (
                SELECT 1 FROM Friends f
                WHERE f.user_id = ? AND f.friend_id = p.user_id
            )
        """)
        args.append(user_id)
    
    if q:
        ex = f"%{q}%"
        conditions.append("(p.title LIKE ? OR p.dream LIKE ?)")
        args.extend([ex, ex])
    
    if sleep_quality is not None:
        conditions.append("p.sleep_quality = ?")
        args.append(sleep_quality)

    if tags:
        for t in tags:
            conditions.append("""
                EXISTS (
                    SELECT 1 FROM Tags t
                    WHERE t.post_id = p.id
                      AND t.tag = ?
                )""")
            args.append(t)

    if cats:
        for title, option in cats.items():
            conditions.append("""
                EXISTS (
                    SELECT 1 FROM PostCategories pc
                    WHERE pc.post_id = p.id
                      AND pc.category = ?
                      AND pc.choice = ?
            )""")
            args.extend([title, option])

    where = "WHERE " + " AND ".join(conditions) if conditions else ""
    group = """GROUP BY p.id, p.title, p.dream, p.sleep_quality,
                        p.bedtime, p.sleep_delay, p.visibility,
                        p.user_id, u.username"""
    
    if tab == "popular":
        order = "ORDER BY like_count DESC, p.id DESC"
    else:
        order = "ORDER BY p.id DESC"
    
    query = f"{sql} {where} {group} {order}"
    return db.query(query, args)

# TODO - rename to post id, big oversight lol
def get(user_id=None):
    """Gets a post from the database. 
    Omit the 'user_id' property to retrieve all available posts.
    """
    if user_id is None:
        query = """
            SELECT p.id, p.title, p.dream dream,
                   p.visibility,
                   u.username, u.id user_id
            FROM Posts p, Users u
            WHERE p.user_id = u.id
            ORDER BY p.id DESC"""
        return db.query(query)
    if isinstance(user_id, (int, str)):
        # TODO better type safety
        query = """
            SELECT u.id user_id, p.id post_id, 
                   p.title, u.username,
                   p.sleep_quality, p.dream,
                   p.bedtime, p.sleep_delay,
                   p.post_time,
                   p.visibility
            FROM Posts p, Users u
            WHERE p.user_id = u.id
              AND p.id = ?"""
        post = db.query(query, [user_id])
        return post[0] if post else None
    raise NotImplementedError

def get_popular_posts():
    query = """
        SELECT p.id, p.title, p.dream dream,
               p.visibility,
               u.username, u.id user_id,
               COUNT(l.id) like_count
        FROM Posts p
        JOIN Users u ON p.user_id = u.id
        LEFT JOIN Likes l ON l.post_id = p.id
        GROUP BY p.id
        ORDER BY like_count DESC, p.id DESC"""
    return db.query(query)

def get_friend_posts(user_id):
    query = """
        SELECT p.id, p.title, p.dream dream,
               p.visibility,
               u.username, u.id user_id
        FROM Posts p
        JOIN Users u ON p.user_id = u.id
        JOIN Friends f ON f.friend_id = p.user_id
        WHERE f.user_id = ?
        ORDER BY p.id DESC"""
    return db.query(query, [user_id])

def update(post_id, title, quality, dream, bedtime, delay, visibility):
    """Modifies a post's content."""
    db.execute("""
    UPDATE Posts
    SET title = ?,
        dream = ?,
        sleep_quality = ?,
        bedtime = ?,
        sleep_delay = ?,
        visibility = ?
    WHERE id = ?
    """, [title, dream, quality, bedtime, delay, visibility, post_id])

def delete(post_id):
    """Removes a post from the database."""
    delete_tags(post_id)
    db.execute("DELETE FROM PostCategories WHERE post_id = ?", [post_id])
    db.execute("DELETE FROM Likes WHERE post_id = ?", [post_id])
    db.execute("DELETE FROM Comments WHERE post_id = ?", [post_id])
    db.execute("DELETE FROM Posts WHERE id = ?", [post_id])

# TODO better filter handling
# deprecated
def find(query, quality=""):
    """Finds a post whose title or content contains the given query."""
    ex = f"%{query}%"

    if quality != "":
        return db.query("""
            SELECT id, title
            FROM Posts
            WHERE sleep_quality = ?
              AND (title LIKE ? 
               OR dream LIKE ?)
            ORDER BY id DESC
        """, [quality, ex, ex])

    return db.query("""
        SELECT id, title
        FROM Posts
        WHERE title LIKE ?
           OR dream LIKE ?
        ORDER BY id DESC
    """, [ex, ex])

def find(filters):
    query = """
        SELECT DISTINCT id, title, dream, sleep_quality, 
                        user_id, visibility
        FROM Posts
    """
    where = []
    params = []

    if filters["q"]:
        ex = f"%{filters['q']}%"
        where.append("(p.title LIKE ? OR p.dream LIKE ?)")
        params.extend([ex, ex])

    quality = filters["quality"]
    if quality is not None:
        where.append("p.sleep_quality = ?")
        params.append(quality)
    
    q = query + " WHERE " + " AND ".join(where) if where else query
    q += " ORDER BY p.id DESC"

def classify(post_id):
    return db.query("""
        SELECT category, choice FROM PostCategories WHERE post_id = ?
    """, [post_id])

def update_categories(post_id, categories):
    db.execute("DELETE FROM PostCategories WHERE post_id = ?", [post_id])
    for cat, choice in categories:
        db.execute("""
            INSERT INTO PostCategories (post_id, category, choice)
            VALUES (?, ?, ?)""", [post_id, cat, choice])

def add_tags(post_id, tags):
    post_tags = []
    for t in tags:
        post_tags.append((post_id, t))

    db.executemany(
        """INSERT INTO Tags (post_id, tag)
        VALUES (?, ?)""",
        post_tags
    )

def delete_tags(post_id):
    db.execute("DELETE FROM Tags WHERE post_id = ?", [post_id])

def get_tags(post_id):
    return db.query("SELECT tag FROM Tags WHERE post_id = ?", [post_id])

def add_comment(post_id, user_id, content):
    db.execute("""
        INSERT INTO Comments (post_id, user_id, content)
        VALUES (?, ?, ?)
    """, [post_id, user_id, content])

def get_comments(post_id):
    return db.query("""
        SELECT c.content, c.id comment_id, 
               u.id user_id, u.username
        FROM Comments c, Users u
        WHERE c.post_id = ? AND c.user_id = u.id
        ORDER BY c.id DESC
    """, [post_id])

def comment_count(post_id):
    query = "SELECT COUNT(post_id) count FROM Comments WHERE post_id = ?"
    return db.query(query, [post_id])

def like(post_id, user_id, state):
    if state:
        db.execute("""
            INSERT INTO Likes (post_id, user_id)
            VALUES (?, ?)
        """, [post_id, user_id])
    else:
        db.execute("""
            DELETE FROM Likes
            WHERE post_id = ? 
            AND user_id = ?
        """, [post_id, user_id])

def get_likes(post_id):
    query = "SELECT user_id FROM Likes WHERE post_id = ?"
    return db.query(query, [post_id])

def like_count(post_id):
    query = "SELECT COUNT(user_id) count FROM Likes WHERE post_id = ?"
    return db.query(query, [post_id])[0]["count"]

def user_count():
    query = "SELECT COUNT(id) count FROM Users"
    return db.query(query)[0]["count"]

def post_count():
    query = "SELECT COUNT(id) count FROM Posts"
    return db.query(query)[0]["count"]
