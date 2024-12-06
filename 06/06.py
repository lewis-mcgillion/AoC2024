with open("06_input.txt", "r") as file:
    lines = file.readlines()

data = [[val for val in line.strip()] for line in lines]


#starting location
#assume it always starts as ^ - think this is ok
x,y = next(
    (row_idx, col_idx)
    for row_idx, row in enumerate(data)
    for col_idx, value in enumerate(row)
    if value == '^'
)
direction = data[x][y]


on_board = True
distinct_positions = 0

directions = ["^", ">", "v", "<"]
dx_dy = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
visited = set()

while on_board:
    new_x, new_y = x + dx_dy[direction][0], y + dx_dy[direction][1]

    if 0 <= new_x < len(data) and 0 <= new_y < len(data[0]):
        new_pos = data[new_x][new_y]

        if new_pos == "#":
            direction = directions[(directions.index(direction) + 1) % 4]
        else:
            x, y = new_x, new_y
            if (x, y) not in visited:
                data[x][y] = "X"
                distinct_positions += 1
                visited.add((x, y))
    else:
        #final position before exiting board
        distinct_positions +=1
        on_board = False

print(distinct_positions)
    

