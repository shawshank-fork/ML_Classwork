x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

n = len(x)

# Calculate slope (m)
m = (n * sum(x[i] * y[i] for i in range(n)) - sum(x) * sum(y)) / \
    (n * sum(i*i for i in x) - (sum(x) ** 2))

# Calculate intercept (b)
b = (sum(y) - m * sum(x)) / n

print("\nSlope (m):", m)
print("Intercept (b):", b)
print(f"Equation of line: y = {m:.4f}x + {b:.4f}")
