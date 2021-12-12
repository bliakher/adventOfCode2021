counter = 0


def read_input(input_file):
    result = []
    with open(input_file) as f:
        for line in f.readlines():
            row = [int(x) for x in line.strip()]
            result.append(row)
    return result


def add_one(map):
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == 9:
                map[x][y] = '.'
            else:
                map[x][y] += 1


def explode_all(map):
    while True:
        no_explosions = True
        for x in range(len(map)):
            for y in range(len(map[0])):
                if map[x][y] == '.':
                    explode(x, y, map)
                    no_explosions = False
        if no_explosions:
            return


def explode(x, y, map):
    global counter
    counter += 1
    map[x][y] = '*'
    for i in range(-1, 2):
        if x + i < 0 or x + i >= len(map):
            continue
        for j in range(-1, 2):
            if y + j < 0 or y + j >= len(map):
                continue
            if map[x + i][y + j] == '.' or map[x + i][y + j] == '*':
                continue
            elif map[x + i][y + j] == 9:
                explode(x + i, y + j, map)
            else:
                map[x + i][y + j] += 1


def set_to_zero(map):
    all_exploded = True
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == '*':
                map[x][y] = 0
            else:
                all_exploded = False
    return all_exploded


def simulate(n, map):
    for round in range(n):
        add_one(map)
        explode_all(map)
        set_to_zero(map)


def simulate_until_all(map):
    all_exploded = False
    round = 0
    while not all_exploded:
        add_one(map)
        explode_all(map)
        all_exploded = set_to_zero(map)
        round += 1
    print(round)


map = read_input("input.txt")
simulate_until_all(map)

