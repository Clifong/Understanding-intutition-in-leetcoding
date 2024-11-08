"""
Intutition:

Notice that the question is accumulatively using repeated values.
For e.g, consider
[1, 2, 3, 4, 5]

Prefix 1:
1 XOR 2 XOR 3 XOR 4 XOR 5 
= Query 2 XOR 5

Prefix 2:
1 XOR 2 XOR 3 XOR 4
= Query 3 XOR 4

Prefix 3:
1 XOR 2 XOR 3
= Query 4 XOR 3

Prefix 4:
1 XOR 2
= Query 5 XOR 2

Prefix 5:
1

Therefore, it makes sense to efficiently calculate the accumulative
prefix XOR first because the next query depends on the previous query.
This saves us time from repeated calculation

Next, now that we have all he prefix calculation, we need to consider
how are we going to get a k value such the k XOR query ith maximimise
the value.

Notice the qns asks for a max value less than 2^(maximumBit). So
the largest value is 2^(maximumBit) - 1. Since we have the freedom
to pick any k, then we simplify the problem to just this

Prefix ith XOR k = 2^(maximumBit) - 1

By the properties of XOR, that is
x XOR x = 0

XOR prefix ith on both side
k = [2^(maximumBit) - 1] XOR prefix ith

We thus solved the problem
"""

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        #Prefix formation
        arr = [nums[0]]
        for i in range(1, len(nums)):
            arr.append(arr[-1] ^ nums[i])
        
        ans = []
        counter = len(arr) - 1
        while counter >= 0:
            ans.append((2**maximumBit - 1) ^ arr[counter])
            counter -= 1
        return ans
        
        

