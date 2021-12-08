def read_input_into_list(input_file):
    with open(input_file) as f:
        line = f.readline().strip()
        return [int(x) for x in line.split(',')]


def count_fuel(crabs, position):
    count = 0
    for crab in crabs:
        fuel = abs(position - crab)
        count += fuel
    return count


def try_all_positions(crabs):
    min_fuel = 100_000_000
    optimal_pos = 0
    min_pos = min(crabs)
    max_pos = max(crabs)
    for pos in range(min_pos, max_pos + 1):
        fuel = count_fuel(crabs, pos)
        if fuel < min_fuel:
            min_fuel = fuel
            optimal_pos = pos
    print(min_pos, max_pos)
    print(optimal_pos)
    print(min_fuel)


def count_fuel2(crabs, position):
    count = 0
    for crab in crabs:
        diff = abs(position - crab)
        fuel = arithmetic_progression(1, diff, 1)
        count += fuel
    return count


def try_all_positions2(crabs):
    min_fuel = 100_000_000
    optimal_pos = 0
    min_pos = min(crabs)
    max_pos = max(crabs)
    for pos in range(min_pos, max_pos + 1):
        fuel = count_fuel2(crabs, pos)
        if fuel < min_fuel:
            min_fuel = fuel
            optimal_pos = pos
    print(min_pos, max_pos)
    print(optimal_pos)
    print(min_fuel)


def arithmetic_progression(a1, an, step):
    n = ((an - a1) // step) + 1
    sum = n * (a1 + an) // 2
    return sum


def find_median(crabs):
    crabs.sort()
    print(crabs[len(crabs) // 2])


crabs = read_input_into_list("input.txt")
try_all_positions2(crabs)
find_median(crabs)
