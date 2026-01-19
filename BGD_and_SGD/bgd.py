import numpy as np

x = np.array([1,2,3,4,5], dtype=float)
y = np.array([5,6,10,13,11], dtype=float)

b0 = 3.3
b1 = 1.9
lr = 0.1
epochs = 10

def mseloss(y, ypred):
    return(1/(2*len(y))) * np.sum((ypred - y)**2)

for epoch in range(epochs):
    ypred = b0 + b1 * x
    db0 = (1/len(x)) * np.sum(y - ypred)
    db1 = (1/len(x)) * np.sum((y - ypred)*x)

    b0 = b0 + lr * db0
    b1 = b1 + lr * db1

    loss = mseloss(y, ypred)


    print(f"Epoch {epoch+1}: b0={b0:.4f}, b1={b1:.4f}, loss={loss:.4f}")



