class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        self.m = len(board)-1
        self.n = len(board[0]) -1
        letter_list = list(word)
        for  row in board:
            for  letter in row:
                # if letter not in word:
                # else:
                if letter in letter_list:
                    letter_list.remove(letter)
        if letter_list:
            return False
        for col_n, row in enumerate(board):
            for row_n, letter in enumerate(row):
                if letter == word[0]:
                    if self.find_next_element(board, [col_n,row_n],word[1:]):
                        return True
        return False

    def find_next_element(self, table, position: list, rest_of_word):
        table1=copy.deepcopy(table)
        table1[position[0]][position[1]] = False
        if not rest_of_word:
            return True
        if position[0] < self.m:
            if table1[position[0]+1][position[1]] == rest_of_word[0]:
                if self.find_next_element (table1, [position[0]+1, position[1]],rest_of_word[1:]):
                    return True
        if position[0] > 0:
            if table1[position[0]+-1][position[1]] == rest_of_word[0]:
                if self.find_next_element (table1, [position[0]-1, position[1]],rest_of_word[1:]):
                    return True
        if position[1] < self.n:
            if table1[position[0]][position[1]+1] == rest_of_word[0]:
                if self.find_next_element (table1, [position[0], position[1]+1],rest_of_word[1:]):
                    return True
        if position[1] > 0:
            if table1[position[0]][position[1]-1] == rest_of_word[0]:
                if self.find_next_element (table1, [position[0], position[1]-1],rest_of_word[1:]):
                    return True

