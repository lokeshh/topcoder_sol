class WordCompositionGame:
  def score(self, listA, listB, listC):
    super_d = {}
    for i in listA:
      if i not in super_d:
        super_d[i] = [1]
      else:
        super_d[i].append(1)

    for i in listB:
      if i not in super_d:
        super_d[i] = [2]
      else:
        super_d[i].append(2)

    for i in listC:
      if i not in super_d:
        super_d[i] = [3]
      else:
        super_d[i].append(3)      

    score_1, score_2, score_3 = 0, 0, 0
    for i in super_d:
      score = 3 - len(super_d[i]) + 1
      for j in super_d[i]:
        if j == 1:
          score_1 += score
        elif j == 2:
          score_2 += score
        elif j == 3:
          score_3 += score
    
    return str(score_1) + "/" + str(score_2) + "/" + str(score_3)

              