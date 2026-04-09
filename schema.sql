CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    created_at DATETIME
);

CREATE TABLE Posts (
    id INTEGER PRIMARY KEY,
    poster_id INTEGER REFERENCES Users(id),
    title TEXT,
    sleep_quality TEXT,
    dream TEXT
);

CREATE TABLE Comments (
    id INTEGER PRIMARY KEY,
    post_id INTEGER REFERENCES Posts(id),
    user_id INTEGER REFERENCES Users(id),
    content TEXT NOT NULL
);

CREATE TABLE Likes (
    id INTEGER PRIMARY KEY,
    post_id INTEGER REFERENCES Posts(id),
    user_id INTEGER REFERENCES Users(id),
    UNIQUE(post_id, user_id)
);