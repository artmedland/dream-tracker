import db

def add(user_id, title, quality, dream):
    """Adds a post to the database."""
    db.execute("""
        INSERT INTO Posts (poster_id, title, sleep_quality, dream)
        VALUES (?, ?, ?, ?)
    """, [user_id, title, quality, dream])

def get(user_id=None):
    """Gets a post from the database. 
    Omit the 'user_id' property to retrieve all available posts.
    """
    if user_id is None:
        query = """
            SELECT p.id, p.title, u.username, u.id user_id
            FROM Posts p, Users u
            WHERE p.poster_id = u.id
            ORDER BY p.id DESC"""
        return db.query(query)
    if isinstance(user_id, (int, str)):
        # TODO better type safety
        query = """
            SELECT u.id user_id, p.id post_id, 
                   p.title, u.username,
                   p.sleep_quality, p.dream
            FROM Posts p, Users u
            WHERE p.poster_id = u.id
              AND p.id = ?"""
        post = db.query(query, [user_id])
        return post[0] if post else None
    raise NotImplementedError

def get_popular_posts():
    raise NotImplementedError

def get_friend_posts():
    raise NotImplementedError

def update(post_id, title, quality, dream):
    """Modifies a post's content."""
    db.execute("""
    UPDATE Posts
    SET title = ?,
        dream = ?,
        sleep_quality = ?
    WHERE id = ?
    """, [title, dream, quality, post_id])

def delete(post_id):
    """Removes a post from the database."""
    db.execute("DELETE FROM Posts WHERE id = ?", [post_id])

# TODO better filter handling
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

def user_count():
    query = "SELECT COUNT(id) count FROM Users"
    return db.query(query)[0]["count"]

def post_count():
    query = "SELECT COUNT(id) count FROM Posts"
    return db.query(query)[0]["count"]
