
def read_input_to_list(file_name):
    res = []
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip().split()
            res.append(line[0])
            res.append(int(line[1]))
    return res


def navigate(data):
    horizontal = 0
    depth = 0
    aim = 0
    i = 0
    while i + 1 < len(data):
        direction = data[i]
        amount = data[i+1]
        if direction == "forward":
            horizontal += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
        i += 2
    return horizontal, depth


data = read_input_to_list("input.txt")
h, d = navigate(data)
print(h, d)
print(h * d)