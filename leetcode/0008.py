class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip()
        if not s:
            return 0
        positive = 1
        if s[0] == '-':
            positive = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        output = ''
        if not s:
            return 0
        if not s[0].isdigit():
            return 0
        for l in s:
            if l.isdigit():
                output += l
            else:
                break
        output = (int(output)) * positive
        if output > 2 ** 31 - 1:
            return (2 ** 31 - 1)
        if output < -2 ** 31:
            return -2 ** 31
        return (output)
