import sqlite3

db_file = "system_data.db"
conn = sqlite3.connect(db_file)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS system_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    cpu_usage REAL,
    temperature REAL,
    memory_percent REAL
);
""")

rows = [
    ("2025-01-01 10:00", 40, 60, 55),
    ("2025-01-01 10:05", 45, 62, 57),
    ("2025-01-01 10:10", 50, 65, 60),
    ("2025-01-01 10:15", 55, 68, 63),
    ("2025-01-01 10:20", 60, 70, 67),
]

cur.executemany(
    "INSERT INTO system_logs (timestamp, cpu_usage, temperature, memory_percent) VALUES (?, ?, ?, ?);",
    rows
)

conn.commit()
conn.close()

print(f"✔ Database Created and Data Added → {db_file}")
