class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return(s)
        left = True
        index = 0
        word = ['' for _ in range(numRows)]
        for number, letter in enumerate (s):
            word[index]+=letter
            if index == numRows-1 or index ==0:
                left = not left
            if left:
                index-=1
            else:
                index+=1
        answer = ''
        for z in word:
            answer+=z
        return (answer)


        
            