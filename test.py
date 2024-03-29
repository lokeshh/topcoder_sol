from medium.A.anagram_completion import AnagramCompletion
from medium.A.airliner_seats import AirlinerSeats
from medium.G.grafix_mask import grafixMask
from medium.B.bloggo_doc_structure import bloggoDocStructure
from medium.Z.zig_zag import ZigZag
from medium.Z.zeroes_and_ones_grid import ZeroesAndOnesGrid
from medium.Z.zeno_division import ZenoDivision
from medium.Y.yllion import Yllion
from medium.Y.yet_another_or_problem import YetAnotherORProblem
from medium.W.word_composition_game import WordCompositionGame
from medium.W.who_will_win import WhoWillWin
from medium.T.two_lottery_games import TwoLotteryGames
from medium.T.true_statements import TrueStatements
from medium.T.trainyard import Trainyard
from medium.T.tax_table import TaxTable
from medium.T.tandem_repeats import TandemRepeats
from medium.T.tall_people import TallPeople
from medium.S.sums_of_perfect_powers import SumsOfPerfectPowers

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

def test_bloggo_doc_structure():
  b = bloggoDocStructure()
  assert b.compare(["<html><h1></h1></html>"],
    ["<html><h1>abc</h1></html>"]) == 'equivalent'

def test_zig_zag():
  z = ZigZag()
  seq = [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]
  assert z.longestZigZag(seq) == 8

def test_zeroes_and_ones_grid():
  z = ZeroesAndOnesGrid()
  assert z.minMovesCount(['1110', '0011']) == 5

def test_zeno_division():
  z = ZenoDivision()
  assert z.cycle('5', '9') == '*---**'

def test_yllion():
  y = Yllion()
  assert y.getPower('ten hundred myriad', 'ten') == 'one myllion'

def test_yet_another_or_problem():
  y = YetAnotherORProblem()
  assert y.countSequences([576460752303423488, 288230376151711744]) == 566919206

def test_word_composition_game():
  w = WordCompositionGame()
  assert w.score(["cat", "dog", "pig", "mouse"], ["cat", "pig"], ["dog", "cat"]) == '8/3/3'

def test_who_will_win():
  w = WhoWillWin()
  assert w.determineWinner(100) == 73

def test_two_lottery_games():
  t = TwoLotteryGames()
  assert t.getHigherChanceGame(3, 1, 1) == 1/3

def test_true_statements():
  t = TrueStatements()
  assert t.numberTrue((0, 1, 3, 2, 2)) == 2

def test_trainyard():
  t = Trainyard()
  assert t.reachableSquares(["++++++++S+", "++++++++++", "++++++++++"], 10) == 30

def test_tax_table():
  t = TaxTable()
  assert t.income(1000000) == 2929591

def test_tandem_repeats():
  t = TandemRepeats()
  assert t.maxLength('AGAGAAAGAA', 3) == 5

def test_tall_people():
  t = TallPeople()
  assert t.getPeople(["9 2 3", "4 8 7"]) == (4, 7)

def test_sums_of_perfect_powers():
  s = SumsOfPerfectPowers()
  assert s.howMany(1, 100) == 60

