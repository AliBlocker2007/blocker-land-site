import sqlite3

try:
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        service TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL
    );
    """)

    conn.commit()
    conn.close()
    print("✅ دیتابیس database.db با موفقیت ساخته شد!")

except Exception as e:
    print("❌ خطا در ساخت دیتابیس:")
    print(e)
