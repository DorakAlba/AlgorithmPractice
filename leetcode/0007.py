class Solution:
    def reverse(self, x: int) -> int:

        if str(x).startswith("-"):
            x=str(x)[1:]
            result = int('-'+(x)[::-1])
            if abs(result) <= 2147483647:
                return result
            else:
                return 0
        result = (int(str(x)[::-1]))
        if result  <= 2147483647:
            return result
        else:
            return 0