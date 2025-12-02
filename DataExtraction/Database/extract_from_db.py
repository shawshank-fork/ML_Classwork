import sqlite3
import pandas as pd

db_file = "system_data.db"
output_file = "system_metrics_db.csv"

conn = sqlite3.connect(db_file)

query = "SELECT timestamp, cpu_usage, temperature, memory_percent FROM system_logs;"
df = pd.read_sql_query(query, conn)

conn.close()

print("Extracted")
print(df.head())

df.to_csv(output_file, index=False)

print(f"\n✔ Saved processed file → {output_file}")
