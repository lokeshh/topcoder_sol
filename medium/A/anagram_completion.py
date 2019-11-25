import string

class AnagramCompletion:
  def complete(self, word1, word2):
      word1_dict = {}
      word2_dict = {}
      for i in string.ascii_uppercase + '.':
        word1_dict[i] = word1.count(i)
        word2_dict[i] = word2.count(i)

      missing1 = ''
      missing2 = ''
      for i in string.ascii_uppercase:
        diff = (word1_dict.get(i, 0) - word2_dict.get(i, 0))
        if diff < 0:
          missing1 += i * abs(diff)
        elif diff > 0:
          missing2 += i * diff

      if word1_dict.get('.', 0) < len(missing1) or word2_dict.get('.', 0) < len(missing2):
        return []
      else:
        missing1 += 'A' * (word1_dict.get('.', 0) - len(missing1))
        missing2 += 'A' * (word2_dict.get('.', 0) - len(missing2))

      missing1 = sorted(missing1)
      missing2 = sorted(missing2)

      word1_new = ''
      word2_new = ''
      for i in word1:
        if i != '.':
          word1_new += i
        else:
          word1_new += missing1.pop(0)
      for i in word2:
        if i != '.':
          word2_new += i
        else:
          word2_new += missing2.pop(0)
      return [word1_new, word2_new]
