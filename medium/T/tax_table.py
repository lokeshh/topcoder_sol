class TaxTable:
    def round(self, x):
        if x - int(x) < 0.5:
            return int(x)
        return int(x) + 1

    def income(self, taxAmount):
        a = self.round((taxAmount + 6525) / 0.25)
        b = self.round((taxAmount + 10042.5) / 0.28)
        c = self.round((taxAmount + 18975) / 0.33)
        d = self.round((taxAmount + 25357) / 0.35)
        if 100000 <= a < 117250:
            return a
        if 117250 <= b < 178650:
            return b
        if 178650 <= c < 319100:
            return c
        if 319100 <= d:
            return d
        return -1

t = TaxTable()
breakpoint()