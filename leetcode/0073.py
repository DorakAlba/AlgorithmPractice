class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        m = len(matrix)
        killer_line = set()
        killer_column = set()
        for ma, element in enumerate(matrix):
            for na,element2 in enumerate(element):
                if element2 == 0:
                    killer_line.add(ma)
                    killer_column.add(na)
        # print(killer_line, killer_column)
        for element in killer_line:
            for _ in range (n):
                matrix[element][_]=0
        for element in killer_column:
            for _ in range (m):
                matrix[_][element]=0

        """
        Do not return anything, modify matrix in-place instead.
        """
        