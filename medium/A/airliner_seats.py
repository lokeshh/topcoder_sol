class AirlinerSeats:
    def doit(self, width, seats):
        arrangement = 'S' * seats
        spaces = width - seats
        req_spaces = None
        if seats % 2 == 0:
            req_spaces = seats // 2
        else:
            req_spaces = (seats + 1) // 2
        if spaces >= req_spaces:
            arrangement = 'S.S' * req_spaces
            if seats % 2 == 1:
                arrangement = arrangement[1:]
            return ('.' * (spaces-req_spaces)) + arrangement
        else:
            return ('S.S' * spaces) + ('S' * (seats - 2 * spaces))

    def mostAisleSeats(self, width, seats):
        v = self.doit(width, seats)
        if len(v) <= 50:
            return [v]
        elif len(v) <= 100:
            return [v[:50], v[50:]]
        else:
            return [v[:50], v[-50:]]