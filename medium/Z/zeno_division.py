class ZenoDivision:
  def find_length(self, x):
    for i in range(1, 61):
      if (2**i - 1) % x == 0:
        return i

  def cycle(self, a, b):
    a = int(a)
    b = int(b)
    length = self.find_length(b)
    if length is None:
      return 'impossible'
    true_a = (2**length - 1) // b * a
    res = ''.join(['*' if i == '1' else '-' for i in bin(true_a)[2:]])
    return '-' * (length - len(res)) + res