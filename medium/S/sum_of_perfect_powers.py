# import bisec

class SumsOfPerfectPowers:
    def perfect_powers_till(self, n):
        x = {0, 1}
        for i in range(2, n):
            j = 2
            while i**j <= n:
                x.add(i**j)
                j += 1
        return sorted(x)

    def howMany(self, lowerBound, upperBound):
        perfect_powers = self.perfect_powers_till(upperBound)
        res = 0
        v = {}
        for i in perfect_powers:
            for j in perfect_powers:
                if (i+j) >= lowerBound and (i+j) <= upperBound:
                    v[i+j] = True
        return len(v)