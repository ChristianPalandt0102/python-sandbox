import sqlite

DB = "data/client.db"

def init_db():
    con = sqlite.connect(DB)
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients(
        id TEXT PRIMARY KEY,
        port INTEGER
    )
    """)

    con.commit()
    con.close()
