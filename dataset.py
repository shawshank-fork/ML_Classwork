import numpy as np
import random


names = ["Shashank", "Neha", "hariom", "vishal", "Akanksha", "Akshat", "Rakesh", "Suresh", "Mukesh", "Bhupesh", "Bablu", "Dablu", "Bunty", "Bublee", "A", "Z", "ABC", "ABCDE", "GFG", "LTC"]

record = []

for i in range(20):
    stuid = f"STD-{i+1:03}"
    MLscore = random.randint(50, 100)
    AIscore = random.randint(45, 95)
    average = round((MLscore + AIscore) / 2, 2)

    record.append([stuid, names[i], MLscore, AIscore, average])

records = np.array(record)


np.savetxt(
    "students.csv",
    records,
    fmt="%s",
    delimiter=",",
    header="stuid, Name, MLscore, AIscore, average",
    comments=""
)

print(records)