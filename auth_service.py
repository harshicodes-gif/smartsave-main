from db import get_connection

def register_user(username, password):

    conn = get_connection()
    cur = conn.cursor()

    try:

        cur.execute(
            """
            INSERT INTO users(username,password)
            VALUES(?,?)
            """,
            (username,password)
        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()


def login_user(username,password):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM users
        WHERE username=?
        AND password=?
        """,
        (username,password)
    )

    user = cur.fetchone()

    conn.close()

    return user
