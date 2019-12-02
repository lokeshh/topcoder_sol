class YetAnotherORProblem:
  def countSequences(self, R):
    R = list(R)
    for idx, i in enumerate(R):
      R[idx] = bin(i)
    # breakpoint()
    max_len = max(map(lambda x: len(x) - 2, R))
    for idx, i in enumerate(R):
      i = i[2:]
      R[idx] = '0' * (max_len - len(i)) + i
    
    locked = [True] * len(R)
    dp = {}
    return self.compute_count(R, locked, dp) % 1000000009

  def compute_count(self, r, locked, dp = {}):
    if tuple(r + locked) in dp:
      return dp[tuple(r + locked)]
    # print(r)
    count = 0
    if r[0] == '':
      return 1
    if locked == [False] * len(locked):
      count = (len(r) + 1)**len(r[0])
      count = count % 1000000009
      dp[tuple(r + locked)] = count
      return count
    possible_first_digits = ['0' * len(r)]
    for i in range(len(r)):
      temp = '0' * len(r)
      possible_first_digits.append(temp[:i] + '1' + temp[i+1:])
    # breakpoint()
    for first_digits in possible_first_digits:
      new_locked = []
      new_r = []
      useless = False
      for i in range(len(r)):
        new_r.append(r[i][1:])
        if not locked[i] or first_digits[i] < r[i][0]:
          new_locked.append(False)
        elif first_digits[i] == r[i][0]:
          new_locked.append(True)
        else:
          useless = True
      if not useless:
        count += self.compute_count(new_r, new_locked)
    
    dp[tuple(r + locked)] = count
    return count % 1000000009






    
