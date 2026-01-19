import pandas as pd

data = {
    "Income": [60,75,85.5,52.8,64.8,64.8,61.5,43.2,87,84,110.1,49.2,108,59.2,82.8,66,69,47.4,93,33,51,51,81,63],
    "LawnSize": [18.4,19.6,16.8,20.8,21.6,17.2,20.8,20.4,23.6,17.6,19.2,17.6,17.6,16,22.4,18.4,20,16.4,20.8,18.8,22,14,20,14.8],
    "Owner": ["Owner","Nonowner","Owner","Nonowner","Owner","Nonowner","Owner","Nonowner","Owner","Nonowner",
              "Owner","Nonowner","Owner","Nonowner","Owner","Nonowner","Owner","Nonowner","Owner","Nonowner",
              "Owner","Nonowner","Owner","Nonowner"]
}

df = pd.DataFrame(data)
df["y"] = df["Owner"].map({"Owner":1,"Nonowner":0})

def gini(labels):
    p1 = sum(labels)/len(labels)
    p0 = 1 - p1
    return 1 - (p1**2 + p0**2)

def weighted_gini(left, right):
    n = len(left)+len(right)
    return (len(left)/n)*gini(left) + (len(right)/n)*gini(right)

def midpoints(values):
    values = sorted(values)
    return [(values[i]+values[i+1])/2 for i in range(len(values)-1)]

print("Root Gini =", gini(df["y"]))

results = []

for feature in ["Income","LawnSize"]:
    mids = midpoints(df[feature].unique())
    for m in mids:
        left = df[df[feature] <= m]["y"]
        right = df[df[feature] > m]["y"]
        wg = weighted_gini(left, right)
        results.append([feature, round(m,2), round(wg,4)])

res_df = pd.DataFrame(results, columns=["Feature","Midpoint","Weighted_Gini"])
res_df = res_df.sort_values(by="Weighted_Gini")

print("\nAll candidate split points ranked:\n")
print(res_df)

best = res_df.iloc[0]
print("\nBEST FIRST SPLIT:")
print("Feature =", best["Feature"])
print("Split at =", best["Midpoint"])
print("Weighted Gini =", best["Weighted_Gini"])
