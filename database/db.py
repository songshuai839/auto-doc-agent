
import sqlite3

def init_db():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        doc_type TEXT,
        content TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_history(filename, doc_type, content):
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history VALUES (NULL,?,?,?)",
                   (filename, doc_type, content))
    conn.commit()
    conn.close()
