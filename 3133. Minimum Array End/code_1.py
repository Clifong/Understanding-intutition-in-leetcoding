"""
Intuition:

Tricky if you don't have any clue on bit manipulation. To solve this,
we need to first understand the effect of AND operator (&)

1 & 0 = 0
1 & 1 = 1
0 & 0 = 0

So to get a x, any numbers that we use must have a 1 bit at exactly
the same posiiton.

E.g
x = 7 = 110

Candidates:
[11]0
[11]1

1[11]0
1[11]1

10[11]0
10[11][1]
...

Because we must find the minimum number, it means we cannot just freely
add 1 anywhere we want and the numbers must be sequentially created.
Meaning 110 -> 111 -> 1110 -> 1111 -> 10110... 

Notice that the 1st numebr is always x itself, because x is the 
smallest number that will produce itself. This means the last number
is obtained by incrementing 1 consecutively up to n - 1 times. So
we have an idea of who the last number is.

Also notice that you are always trying to "fill" up the zeroes in x
in order to get the number! And each time you need to overflow to
a new position, the number is resetted

Meaning,
11[00]1 -> 11[01]1 -> 11[10]1 -> 11[11]1 

[1]11[00]1 -> [1]11[01]1 -> [1]11[10]1 -> [1]11[11]1 
^
|
Overflowed bit

Both hints that to get the answer, check if the number has a 0 bit, 
if so, copy the last bit of n to it and shift n to the right

In simpler words,
n = 5 
x = 9 = 1001

n - 1 = 4 = 100

01001
1 00
-----
11001

"""

class Solution:
    def minEnd(self, n: int, x: int) -> int:

        #This question needs at least 46 bits to cover all case
        b = [0]*46
        n -= 1
        
        #Make b to become x
        for i in range(45, -1, -1):
            if x == 0:
                break
            if b[i] == 0:
                b[i] = x & 1
                x >>= 1
        
        #Fill in the zero with the last bit of n
        for i in range(45, -1, -1):
            if n == 0:
                break
            if b[i] == 0:
                b[i] = n & 1
                #Remember to shift your n to the right!
                n >>= 1
        
        #Get back the answer by conevrting it to a number
        ans = 0
        for i in range(45):
            ans += 2**i * b[45 - i]
        return ans 