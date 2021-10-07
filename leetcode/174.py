class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        self.dungeon = dungeon
        self.mn = [len(dungeon) - 1, len(dungeon[0]) - 1]
        if self.mn == [0, 0]:
            return max(1, 1 - dungeon[0][0])
        self.minima = self.starting_value()
        self.choose_path([0, 0], 1, float('inf'))
        return (self.minima + 2)

    def choose_path(self, coordinate: list[int], value: int, minimal_required_life):
        value += self.dungeon[coordinate[0]][coordinate[1]]
        if value < self.minima:
            return None
        if value < minimal_required_life:
            minimal_required_life = value
        if coordinate == self.mn:
            self.minima = minimal_required_life
        if self.mn[0] > coordinate[0]:
            self.choose_path([coordinate[0] + 1, coordinate[1]], value, minimal_required_life)
        if self.mn[1] > coordinate[1]:
            self.choose_path([coordinate[0], coordinate[1] + 1], value, minimal_required_life)

    def starting_value(self) -> int:
        values = 0
        minimum = 0
        for row in self.dungeon:
            values += row[0]
            if values < minimum:
                minimum = values
        for column in self.dungeon[-1][1:]:
            values += column
            if values < minimum:
                minimum = values
        return minimum+1

a = Solution()
a.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])