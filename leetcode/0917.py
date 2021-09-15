class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        indexes = []
        strings = []
        for index, element in enumerate(s):
            if element.isalpha():
                indexes.append(index)
                strings.append(element)
        s = list(s)
        for index,string in zip(indexes,reversed(strings)):
            s[index] = string
        return( "".join(s))