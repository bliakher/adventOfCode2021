def read_input(input_file):
    result = []
    with open(input_file) as f:
        for line in f.readlines():
            row = [int(x) for x in line.strip()]
            result.append(row)
    return result


def neighbors_are_higher(x, y, map):
    # copy = deep_copy(map)
    result = True
    for i in [-1, 1]:
        if x + i < len(map) and x + i >= 0:
            n = map[x + i][y]
            c = map[x][y]
            # copy[x + i][y] = '.'
            if n <= c:
                result = False
    for i in [-1, 1]:
        if y + i < len(map[0]) and y + i >= 0:
            n = map[x][y + i]
            c = map[x][y]
            # copy[x][y + i] = '.'
            if n <= c:
                result = False
    # print_map(copy)
    return result


def deep_copy(map):
    copy = []
    for x in range(len(map)):
        row = []
        for y in range(len(map[0])):
            row.append(map[x][y])
        copy.append(row)
    return copy


def print_map(map):
    for x in range(len(map)):
        for y in range(len(map[0])):
            print(map[x][y], end='')
        print()
    print()


def find_low_points(map):
    print_map(map)
    risk = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            #print(map[x][y], end='')
            if neighbors_are_higher(x, y, map):
                risk += map[x][y] + 1
                #print(map[x][y] + 1)
        #print()
    print(risk)


map = read_input("input.txt")
find_low_points(map)
