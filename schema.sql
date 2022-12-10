DROP TABLE IF EXISTS cards;

CREATE TABLE cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status INTEGER,
    link TEXT,
    price REAL,
    img TEXT
);