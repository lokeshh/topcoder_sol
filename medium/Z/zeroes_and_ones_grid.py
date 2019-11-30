class ZeroesAndOnesGrid:
  def flip(self, table, x, y):
    # breakpoi  nt()
    for i in range(x+1):
      for j in range(y+1):
        if table[i][j] == '1':
          table[i][j] = '0'
        else:
          table[i][j] = '1'
    return table

  def remove_row(self, table):
    return table[:-1]

  def remove_col(self, table):
    for i in range(len(table)):
      table[i] = table[i][:-1]
    return table

  def minMovesCount(self, table):
    if type(table) == tuple:
      table = list(table)
    if len(table) > 0 and type(table[0]) == str:
      for i in range(len(table)):
        table[i] = list(table[i])
    if table == [[]] or table == []:
      return 0
    r = len(table)
    c = len(table[0])
    f = 0
    if r >= c:
      for i in range(c)[::-1]:
        if table[r-1][i] == '1':
          table = self.flip(table, r-1, i)
          f += 1
      table = self.remove_row(table)
    else:
      for i in range(r)[::-1]:
        if table[i][c-1] == '1':
          table = self.flip(table, i, c-1)
          f += 1
      table = self.remove_col(table)
    
    return f + self.minMovesCount(table)