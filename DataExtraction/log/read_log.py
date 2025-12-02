log_errors = []

with open("system.log", "r") as log:
    for line in log:
        if "ERROR" in line:
            log_errors.append(line.strip())

print("errors found in log:\n")
for error in log_errors:
    print(error)