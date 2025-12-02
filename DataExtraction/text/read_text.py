with open("data.txt", "r") as file:
    lines = file.readlines()

print("data read from text file:\n")
for line in lines:
    print(line.strip())    