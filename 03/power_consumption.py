def solve(file_name):
    bit_counts = []
    for _ in range(12):
        bit_counts.append([0, 0])
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip()
            i = 0
            for char in line:
                result_bit_idx = 0 if char == '0' else 1
                bit_counts[i][result_bit_idx] += 1
                i += 1
    gamma = ""
    epsilon = ""
    for count in bit_counts:
        if count[0] > count[1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    print(gamma)
    print(epsilon)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma, epsilon, gamma * epsilon)


solve("input.txt")