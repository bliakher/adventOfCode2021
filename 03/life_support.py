
def read_input_to_list(file_name):
    res = []
    with open(file_name) as f:
        for line in f.readlines():
            num = line.strip()
            res.append(num)
    return res


def solve_oxygen(data, idx=0):
    if len(data) == 1:
        return data[0]
    ones = []
    zeros = []
    for num in data:
        if num[idx] == '0':
            zeros.append(num)
        else:
            ones.append(num)
    if len(ones) == len(zeros):
        choose = ones
    elif len(ones) > len(zeros):
        choose = ones
    else:
        choose = zeros
    return solve_oxygen(choose, idx + 1)


def solve_co2(data, idx=0):
    if len(data) == 1:
        return data[0]
    ones = []
    zeros = []
    for num in data:
        if num[idx] == '0':
            zeros.append(num)
        else:
            ones.append(num)
    if len(ones) == len(zeros):
        choose = zeros
    elif len(ones) > len(zeros):
        choose = zeros
    else:
        choose = ones
    return solve_co2(choose, idx + 1)


data = read_input_to_list("input.txt")
oxygen = int(solve_oxygen(data), 2)
co2 = int(solve_co2(data), 2)
print(oxygen, co2, oxygen * co2)

