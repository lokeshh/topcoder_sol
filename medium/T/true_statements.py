class TrueStatements:
  def numberTrue(self, statements):
    statements = sorted(statements, reverse=True)
    for i in statements:
      if i == statements.count(i):
        return i
    if 0 not in statements:
      return 0
    return -1