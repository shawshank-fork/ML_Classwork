x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

n = len(x)

# Calculate mean
x_bar = sum(x) / n
y_bar = sum(y) / n

# Calculate slope
num = sum((x[i] - x_bar) * (y[i] - y_bar) for i in range(n))
den = sum((x[i] - x_bar) ** 2 for i in range(n))
m = num / den

# Calculate intercept 
b = y_bar - m * x_bar

print("\nSlope (m):", m)
print("Intercept (b):", b)
print(f"Equation: y = {m:.4f}x + {b:.4f}")
