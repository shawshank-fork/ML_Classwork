import csv
import random
from datetime import datetime
import os

file_name = "experimental_system_data.csv"
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as f:
        f.write("timestamp,cpu,temp,ram\n")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
cpu = random.randint(30, 90)
temp = random.randint(50, 80)
ram = random.randint(40, 95)

with open(file_name, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([timestamp, cpu, temp, ram])

print(f"Data recorded → {file_name}")
