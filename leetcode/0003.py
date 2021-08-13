class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = 0
        sbs = ""
        for element in range(len(s)):
            score = 1
            sbs = f"{s[element]}"
            for element in s[element+1:]:
                if element not in sbs:
                    sbs+=element
                    score+=1
                else:
                    break
            if score>record:
                record = score
        return (record)


                