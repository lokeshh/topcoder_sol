class WhoWillWin:
  def determineWinner(self, N):
    arr = list(range(1, N+1))
    while len(arr) != 1:
      if len(arr) % 2 == 1:
        arr = [arr[-1]] + arr[:-1:2]
      else:
        arr = arr[::2]
    return arr[0]