"""
Intuition:

It feels intutive to do a dynamic programming approach because
the question is a case of "pick number or do not pick". Thus making
it similar to a 1/0 knapsack qns.

However, if you think about how the AND of 2 numbers is 0, it only
happens if there are no common 1 bit in the same position. For e.g

  11001
& 00110
--------
  00000

Therefore, in order to get the logest possible sequence, you will
have to pick consecutive numbers with a 1 in the same position. This
forms the basis for our greedy approach.

Since the max limit is 10^5, we have to deal with at most 24 bits.
Therefore, for every value in candidate, we just need to increment
a 1 to the position if the bit at that posiion is 1. For example

Suppose the array length is 6
[0, 0, 0, 0, 0, 0]

Numbers =[011, 1100, 0001, 1101]

num = 011
=> [0, 0, 0, 0, 1, 1]

num = 1100
=> [0, 0, 0, 1, 2, 1]

num = 0001
=> [0, 0, 0, 1, 2, 2]

num = 1101
=> [0, 0, 1, 2, 2, 3]

As such, you can see, the longest sequence is found by picking
011, 0001 and 1101 which is the expected answer!
"""

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        #Create a 24 bit array
        arr = [0]*24

        for i in candidates:
            #Find the binary equivalent of the ith number
            b = bin(i)

            #Handles the increment
            for j in range(2, len(b)):
                arr[j - 2] += b[len(b) - j + 1] == "1"
        return max(arr)
        