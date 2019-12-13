class Trainyard:
    def find_reachable_squares(self, layout, fuel):
        reachable = 0
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                current_pos = (i, j)
                # breakpoint()
                if self.is_reachable_from(layout, current_pos, fuel):
                    reachable += 1
                    # print(current_pos)
        return reachable

    def is_reachable_from(self, layout, current_pos, fuel):
        x, y = current_pos
        if layout[x][y] == 'S':
            return True
        if fuel == 0:
            return False
        res = False
        if x + 1 < len(layout):
            if layout[x][y] in ['|', '+'] and layout[x+1][y] in ['|', '+', 'S']:
                res = self.is_reachable_from(layout, (x+1, y), fuel - 1)
        if res:
            return res
        if x - 1 >= 0:
            if layout[x][y] in ['|', '+'] and layout[x-1][y] in ['|', '+', 'S']:
                res = self.is_reachable_from(layout, (x-1, y), fuel - 1)
        if res:
            return res
        if y + 1 < len(layout[0]):
            if layout[x][y] in ['-', '+'] and layout[x][y+1] in ['-', '+', 'S']:
                res = self.is_reachable_from(layout, (x, y+1), fuel - 1)
        if res:
            return res
        if y - 1 >= 0:
            if layout[x][y] in ['-', '+'] and layout[x][y-1] in ['-', '+', 'S']:
                return self.is_reachable_from(layout, (x, y-1), fuel - 1)
        return False


    def reachableSquares(self, layout, fuel):
       return self.find_reachable_squares(layout, fuel)
        