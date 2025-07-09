from database.db import get_connection
from datetime import datetime

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            text TEXT,
            target_lang TEXT,
            translated_text TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_translation(text, target_lang, translated_text):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO logs (text, target_lang, translated_text, timestamp)
        VALUES (?, ?, ?, ?)
    """, (text, target_lang, translated_text, datetime.now().isoformat()))
    conn.commit()
    conn.close()
