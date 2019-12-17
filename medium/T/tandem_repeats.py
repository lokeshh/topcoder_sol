class TandemRepeats:
    def same(self, x, y):
        diff = 0
        for i, j in zip(x, y):
            if i != j:
                diff += 1
        # breakpoint()
        return diff <= self.k

    def works(self, dna, n):
        start = 0
        while start + 2*n <= len(dna):
            # breakpoint()
            if self.same(dna[start:start+n], dna[start+n:start+2*n]):
                return True
            start += 1
        return False


    def maxLength(self, dna, k):
        self.k = k
        n = len(dna)//2
        # breakpoint()
        while n > 0:
            if self.works(dna, n):
                return n
            n -= 1
        return n

