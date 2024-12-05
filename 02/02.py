import numpy as np

with open("./02_input.txt", 'r') as file:
    data = []
    for line in file:
        row = np.array(line.strip().split(), dtype=int)
        data.append(row)

safe_count = 0

# stinky brute force solution hehe
for row in data:
    direction = 0  # 1 for ascending, -1 for descending
    safe = True
    damper = True
    
    for i in range(len(row) - 1):
        if not safe:
            break

        diff = row[i + 1] - row[i]

        if direction == 0:
            direction = 1 if diff > 0 else -1

        if (direction == 1 and diff < 0) or (direction == -1 and diff > 0):
            safe = False

        if not (1 <= abs(diff) <= 3):
            safe = False

    if safe:
        safe_count += 1
    
print(safe_count)

#couldnt figure out pt2 :(

