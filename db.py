import sqlite3

DB_NAME = "smartsave.db"


def get_connection():

    return sqlite3.connect(
        DB_NAME
    )


def init_db():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS user_settings(
            username TEXT PRIMARY KEY,
            pocket_money REAL DEFAULT 5000
        )
        """
    )

    conn.commit()

    conn.close()
