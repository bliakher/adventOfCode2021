class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print(self):
      print(self.x, ",", self.y, end='')


class Line:
  def __init__(self, fr, to):
    self.fr = fr
    self.to = to

  def print(self):
      self.fr.print()
      print(" -> ", end='')
      self.to.print()
      print()


def parse_lines(input_file):
  lines = []
  with open(input_file) as f:
    for line in f.readlines():
      tokens = line.strip().split()
      t1 = tokens[0].split(',')
      p1 = Point(int(t1[0]), int(t1[1]))
      t2 = tokens[2].split(',')
      p2 = Point(int(t2[0]), int(t2[1]))
      l = Line(p1, p2)
      lines.append(l)
  return lines


def filter_straight(lines):
  result = []
  for l in lines:
    if l.fr.x == l.to.x or l.fr.y == l.to.y:
      result.append(l)
  return result


def get_biggest_coordinate(lines):
  mx = 0
  my = 0
  for l in lines:
    cx = max(l.fr.x, l.to.x)
    if cx > mx:
      mx = cx
    cy = max(l.fr.y, l.to.y)
    if cy > my:
      my = cy
  return mx, my


def create_map(sizex, sizey):
  map = []
  for _ in range(sizey + 1):
    map.append([0] * (sizex + 1))
  return map


def mark_line(line, map):
    if line.fr.x == line.to.x: # vertical line
        fr, to = (line.fr, line.to) if line.fr.y < line.to.y else (line.to, line.fr)
        length = to.y - fr.y + 1
        for i in range(length):
            map[fr.y + i][fr.x] += 1

    elif line.fr.y == line.to.y: # vertical line
        fr, to = (line.fr, line.to) if line.fr.x < line.to.x else (line.to, line.fr)
        length = to.x - fr.x + 1
        for i in range(length):
            map[fr.y][fr.x + i] += 1
    else:
        # diagonal to right
        if (line.fr.x < line.to.x and line.fr.y < line.to.y) or (line.fr.x > line.to.x and line.fr.y > line.to.y):
            fr, to = (line.fr, line.to) if line.fr.x < line.to.x else (line.to, line.fr)
            length = to.x - fr.x + 1
            for i in range(length):
                map[fr.y + i][fr.x + i] += 1
        # diagonal to left
        else:
            # x in from is bigger: 9,7 -> 7,9 not 7,9 -> 9,7
            fr, to = (line.fr, line.to) if line.fr.x > line.to.x else (line.to, line.fr)
            length = to.y - fr.y + 1
            for i in range(length):
                map[fr.y + i][fr.x - i] += 1


def count_intersections(map):
    counter = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] > 1:
                counter += 1
    return counter


def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                print(".", end="")
            else:
                print(map[i][j], end="")
        print()


def solve(lines):
  # lines = filter_straight(lines)
  mx, my = get_biggest_coordinate(lines)
  print(mx, my)
  map = create_map(mx, my)
  for line in lines:
      line.print()
      mark_line(line, map)
  # print_map(map)
  count = count_intersections(map)
  print(count)


lines = parse_lines("input.txt")
solve(lines)


