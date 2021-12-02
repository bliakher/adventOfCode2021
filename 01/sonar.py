
def read_input_to_list(file_name):
    res = []
    with open(file_name) as f:
        for line in f.readlines():
            num = int(line.strip())
            res.append(num)
    return res


def sonar(data):
    counter = 0
    win_before = data[0] + data[1] + data[2]
    last_idx = 0
    next_idx = 3
    while next_idx < len(data):
        win_new = win_before - data[last_idx] + data[next_idx]
        if win_new > win_before:
            counter += 1
        win_before = win_new
        last_idx += 1
        next_idx += 1
    return counter


sonar_data = read_input_to_list("../02/input.txt")
result = sonar(sonar_data)
print(result)