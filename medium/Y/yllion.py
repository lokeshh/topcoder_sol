class Yllion:
    POWER_LIST = [
        'ten',
        'hundred',
        'myriad',
        'myllion',
        'byllion',
        'tryllion',
        'quadryllion',
        'quintyllion',
        'sextyllion',
        'septyllion',
        'octyllion',
        'nonyllion',
        'decyllion'
    ]

    def __init__(self):
        self.str_map = {}
        self.inverse_str_map = {}
        for idx, i in enumerate(self.POWER_LIST):
            self.str_map[i] = idx
            self.inverse_str_map[idx] = i

    def parse_from_str(self, a):
        a = a.split(' ')
        bin_value = ['0'] * 15
        for i in a:
            if i == 'one':
                continue
            bin_value[self.str_map[i]] = '1'
        return int(''.join(bin_value[::-1]), 2)

    def value_to_str(self, z):
        z = z[::-1]
        # breakpoint()
        s = []
        for i in range(len(z)):
            if i == 0 and len(s) != 0 and s[0] == 'ten':
                continue
            if z[i] == '1':
                s.append(self.inverse_str_map[i])
        return s


    def getPower(self, a, b):
        x = self.parse_from_str(a)
        y = self.parse_from_str(b)
        s = self.value_to_str(bin(x + y)[2:])
        if len(s) == 0 or s[0] != 'ten':
            s = ['one'] + s
        return ' '.join(s)


