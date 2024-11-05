"""
Intuition:

Try to think of a few examples first. You'll realize that you only 
need to care about substrings of length 2 (i.e consecutive pair)

The reason is that if a pair fail, then it is guranteed any longer
consecutive substring must fail. Moreover, considering a pair has
a higher chance of minimising the moves needed since a pair is
the smallest unit possible. You can thus find consecutive 
successful pairs

For e.g
111000 

Substring of length 6: 
- 111000 invalid so need modify 3 character

Substring of length 2 and 4: 
- 11 valid
- 1000 invalid so need modify 1 character 

Substring of length 2: 
- 11 valid
- 10 invalid so need modify 1 character 
- 00 valid 
"""

class Solution:
    def minChanges(self, s: str) -> int:
        
        move = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                move += 1
        return move