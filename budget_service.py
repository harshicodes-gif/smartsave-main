# Budget engine
from backend.database.db import get_connection

def add_transaction(category, amount, description):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO transactions
        (category, amount, description)
        VALUES (?, ?, ?)
        """,
        (category, amount, description)
    )

    conn.commit()
    conn.close()


def get_transactions():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM transactions")

    rows = cur.fetchall()

    conn.close()

    return rows