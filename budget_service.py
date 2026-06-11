from db import get_connection

def add_transaction(
    username,
    category,
    amount,
    description
):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO transactions
        (
            username,
            category,
            amount,
            description
        )
        VALUES(?,?,?,?)
        """,
        (
            username,
            category,
            amount,
            description
        )
    )

    conn.commit()
    conn.close()


def get_transactions(username):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM transactions
        WHERE username=?
        """,
        (username,)
    )

    rows = cur.fetchall()

    conn.close()

    return rows
