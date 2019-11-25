from medium.A.anagram_completion import AnagramCompletion
from medium.A.airliner_seats import AirlinerSeats

def test_anagram_completion():
  a = AnagramCompletion()
  assert a.complete('AB.AC.', 'ABD..E') == ["ABDACE", "ABDACE"]

def test_airliner_seats():
  a = AirlinerSeats()
  assert a.mostAisleSeats(6, 3) == ['..SS.S']
