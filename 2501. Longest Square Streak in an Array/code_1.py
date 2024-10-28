"""
Intutition:
It is normal to think of this question as a dynamic programming
question, and it can technically be solved in that manner. However,
thinking about it, this is more close to a greedy problem. 

Firstly, it makes more sense to pick the smallest element and 
check if its squared form exist (Greedy choice). Reason is that 
the smaller the element, the higher the chance you can 
construct a longer chain.

E.g
[2, 4, 16]

You can form a longer chain 2 -> 4 -> 16 than picking 4 -> 16.
So you have a better chance of getting a longer chain by starting
from the smallest.

Secondly, you can technically use a similar "memoization" technique
as dynamic programming. Fundamentally, you don't want to repeatedly
search for a chain if the element is found before. This can be done
by maintaining a set of explored elements. You can implement a 
similar idea in the greedy method so te greedy method also works

E.g
[2, 4, 8]

explored = {} <- set

i = 0. curr_element = 2
=========================
check if curr_element in explored => NO
explored = {2} next = 4
explored = {2, 4} next = 16
explored = {2, 4, 16} next = 256 (does not exit)

longest length = 3

i = 1. curr_element = 4
========================
Check if curr_element in explored => YES
DON'T DO ANYTHING

longest length = 3

i = 2. curr_element = 16
========================
Check if curr_element in explored => YES
DON'T DO ANYTHING

longest length = 3
"""

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        #A set copy of nums to make checking O(1)
        copy = set(nums)
        explored = set()
        longest = 0
        nums.sort()

        for i in nums:
            temp = 0
            while i not in explored:
                explored.add(i)
                temp += 1
                if i**2 in copy:
                    i = i**2
                else:
                    longest = max(longest, temp)
                    break
        return -1 if longest == 1 else longest