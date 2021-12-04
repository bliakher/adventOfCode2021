
def solve(file_name):
    min_count = 100
    win_score = 0
    with open(file_name) as f:
        numbers = get_numbers(f.readline(), ',')
        board = []
        f.readline() # skip first empty line
        line = f.readline()
        while line != "":
            if len(board) < 5:
                row = get_numbers(line, ' ')
                board.append(row)
            else:
                score, count = check_board(numbers,board)
                if count < min_count:
                    min_count = count
                    win_score = score
                board = []
            line = f.readline()
    print(min_count, win_score)


def solve2(file_name):
    max_count = 0
    win_score = 0
    with open(file_name) as f:
        numbers = get_numbers(f.readline(), ',')
        board = []
        f.readline() # skip first empty line
        line = f.readline()
        while line != "":
            if len(board) < 5:
                row = get_numbers(line, ' ')
                board.append(row)
            else:
                score, count = check_board(numbers,board)
                if count > max_count:
                    max_count = count
                    win_score = score
                board = []
            line = f.readline()
    print(max_count, win_score)


def get_numbers(line, splitter):
    line = line.strip()
    tokens = line.split(splitter)
    tokens = filter(lambda x: (x != ""), tokens)
    return [int(x) for x in tokens]


def check_board(numbers, board):
    sum = 0
    count_to_win = 0
    for num in numbers:
        count_to_win += 1
        found = find_and_mark(num, board)
        if found and check_winning(board):
            sum = get_sum_unmarked(board)
            score = sum * num
            return score, count_to_win
    return 0, 100


def find_and_mark(num, board):
    for i in range(5):
        for j in range(5):
            if num == board[i][j]:
                board[i][j] = -1
                return True
    return False


def check_winning(board):
    # check rows
    for i in range(5):
        wins = True
        for j in range(5):
            if board[i][j] != -1:
                wins = False
                break
        if wins:
            return True
    # check columns
    for j in range(5):
        wins = True
        for i in range(5):
            if board[i][j] != -1:
                wins = False
                break
        if wins:
            return True
    return False


def get_sum_unmarked(board):
    sum = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != -1:
                sum += board[i][j]
    return sum


solve2("input.txt")
