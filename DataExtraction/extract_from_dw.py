import pandas as pd

input_file = "dw_system_metrics.csv"
output_file = "system_metrics_dw.csv"

df = pd.read_csv(input_file)

print("📌 Extracted Data from DW Preview:")
print(df.head())

df.to_csv(output_file, index=False)

print(f"\n✔ Saved processed file → {output_file}")
