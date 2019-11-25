import sys

sys.setrecursionlimit(1000000000)

class grafixMask:
  def find_area(self, matrix, queue):
    area = 1
    while True:
      # print(len(queue))
      if queue == []:
        return area
      x, y = queue.pop(0)
      if (x + 1) < 400 and matrix[x+1][y] == 0:
        area += 1
        matrix[x+1][y] = 1
        queue.append((x+1, y))
      if (x - 1) >= 0 and matrix[x-1][y] == 0:
        area += 1
        matrix[x-1][y] = 1
        queue.append((x-1, y))
      if (y + 1) < 600 and matrix[x][y+1] == 0:
        area += 1
        matrix[x][y+1] = 1
        queue.append((x, y+1))
      if (y - 1) >= 0 and matrix[x][y-1] == 0:
        area += 1
        matrix[x][y-1] = 1
        queue.append((x, y-1))

  def sortedAreas(self, rectangles):
    matrix = []
    for row in range(400):
      matrix.append([0] * 600)
    # breakpoint()
    for rect in rectangles:
      a, b, c, d = map(int, rect.split(' '))
      for row in range(a, c+1):
        for col in range(b, d+1):
          matrix[row][col] = 1
    
    areas = []
    cur_index = 0
    while not cur_index == 400 * 600:
      x = cur_index // 600
      y = cur_index % 600
      if matrix[x][y] == 1:
        cur_index += 1
        continue
      else:
        matrix[x][y] = 1
        areas.append(self.find_area(matrix, [(x, y)]))
        # breakpoint()
    # breakpoint()
    return sorted(areas)