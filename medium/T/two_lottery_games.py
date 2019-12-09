import itertools as it

class TwoLotteryGames:
    def getHigherChanceGame(self, n, m, k):
        s = 0
        a = 0
        for comb in it.combinations(range(n), m):
            a += 1
            t = 0
            for i in comb:
                if i < m:
                    t += 1
            if t >= k:
                s += 1
        return s / a
