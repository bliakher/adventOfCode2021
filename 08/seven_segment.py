
def read_output_digits(input_file):
    output = []
    with open(input_file) as f:
        for line in f.readlines():
            tokens = line.strip().split()
            output_started = False
            for token in tokens:
                if output_started:
                    output.append(token)
                if token == "|":
                    output_started = True
    return output


def count_unique_digits(output):
    counter = 0
    for o in output:
        if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
            counter += 1
    print(counter)


output = read_output_digits("input.txt")
count_unique_digits(output)

# get a from 7 and 1

# six segments - 0, 6, 9
# diff 6 from 0, 9 - has only f - 0 and 9 have both
# -> we know f
# d is only one that 0 doesn't have
# with d diff between 0 and 9
# five segments - 2, 3, 5
# 3 has both c, f
# 5 has only f
# 2 has only c

