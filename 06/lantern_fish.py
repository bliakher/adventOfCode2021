
def read_input_into_list(input_file):
    with open(input_file) as f:
        line = f.readline().strip()
        result = [int(x) for x in line.split(',')]
        return result


def count_frequencies(fish):
    frequencies = [0] * 9
    for f in fish:
        frequencies[f] += 1
    return frequencies


def count_fish(freq):
    count = 0
    for i in range(len(freq)):
        count += freq[i]
    return count


def simulate_quick(fish, days):
    freq = count_frequencies(fish)
    for day in range(days):
        print("day", day)
        next_freq = [0] * 9
        for i in range(len(freq)):
            if i == 0:
                next_freq[6] += freq[i]
                next_freq[8] += freq[i]
            else:
                next_freq[i - 1] += freq[i]
        freq = next_freq
    count = count_fish(freq)
    print(count)


def simulate(fish, days):
    simulation = fish.copy()
    for day in range(days):
        print("day", day)
        spawned = []
        for i in range(len(simulation)):
            if simulation[i] == 0:
                simulation[i] = 6
                spawned.append(8)
            else:
                simulation[i] -= 1
        simulation.extend(spawned)
    return simulation


fish = read_input_into_list("input.txt")
# simulate_quick(fish, 18)
# print("-------------------------------------")
simulate_quick(fish, 256)
# #d18 = simulate(fish, 18)
# d80 = simulate(fish, 256)
# print(len(d80))

