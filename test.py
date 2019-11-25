from medium.A.anagram_completion import AnagramCompletion
from medium.A.airliner_seats import AirlinerSeats
from medium.G.grafix_mask import grafixMask

def test_anagram_completion():
  a = AnagramCompletion()
  assert a.complete('AB.AC.', 'ABD..E') == ["ABDACE", "ABDACE"]

def test_airliner_seats():
  a = AirlinerSeats()
  assert a.mostAisleSeats(6, 3) == ['..SS.S']

def test_grafix_mask():
  g = grafixMask()
  assert g.sortedAreas([
    "48 192 351 207", 
    "48 392 351 407", 
    "120 52 135 547", 
    "260 52 275 547"]) == [22816, 192608]