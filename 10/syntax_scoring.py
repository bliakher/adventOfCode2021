

def get_score(char):
    scoring = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        '': 0
    }
    return scoring[char]


def get_score_completion(completion):
    scoring = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    score = 0
    for c in completion:
        score *= 5
        score += scoring[c]
    return score


def find_error(line):
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for cur in line:
        if cur in opening:
            stack.append(cur)
        elif cur in closing:
            last = stack.pop()
            if pairs[last] != cur:
                return cur
    return ""


def autocomplete(line):
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for cur in line:
        if cur in opening:
            stack.append(cur)
        elif cur in closing:
            last = stack.pop()
            if pairs[last] != cur:
                return []
    if len(stack) > 0:
        return find_closings(stack, pairs)
    else:
        return []


def find_closings(openings, pairs):
    result = []
    for open in reversed(openings):
        close = pairs[open]
        result.append(close)
    return result


def solve(input_file):
    score = 0
    with open(input_file) as f:
        for line in f.readlines():
            error = find_error(line.strip())
            print(error)
            score += get_score(error)
    print(score)


def solve2(input_file):
    scores = []
    with open(input_file) as f:
        for line in f.readlines():
            completion = autocomplete(line.strip())
            if len(completion) > 0:
                score = get_score_completion(completion)
                scores.append(score)
    scores.sort()
    # print(scores)
    print(scores[len(scores) // 2])


solve2("input.txt")