from medium.A.anagram_completion import AnagramCompletion

def test_anagram_completion():
  a = AnagramCompletion()
  assert a.complete('AB.AC.', 'ABD..E') == ["ABDACE", "ABDACE"]
