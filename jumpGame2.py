"""
DP Approach -
what is the decision that we must optimize?
  - if, for example, nums[i] = 3, you can take 1 step or 2 steps or 3 steps
  - so the decision is *how many* number of steps you will take at each location

############
recurrence relation:

for any point, i:
  minJumps[i] = 1 + min(minJumps[i+1], minJumps[i+2], ..., minJumps[i + k]) if nums[i] > 0
  ( where k = nums[i])

BASE CASES:
  minJumps[n] = 0
  if nums[i] = 0,
    minJumps[i] = inf (or some ridic high number like len(nums) + 1)


#############

here's what that looks like in action >>>>>
[2, 3, 1, 1, 2]

cache at initialization: [inf, inf, inf, inf, 0]

minJumps[0] = 1 + min(minJumps[1], minJumps[2])
minJumps[1] = 1 + min(
                    minJumps[2],
                    minJumps[3],
                    minJumps[4])
minJumps[2] = 1 + min(
                    minJumps[3]
)
minJumps[3] = 1 + min(
                  minJumps[4]
)

---- BASE REACHED
minJumps[4] = 0
minJumps[3] = 1 + minJumps[4] = 1
minJumps[2] = 1 + minJumps[3] = 2
minJumps[1] = 1 + min(minJumps[2], minJumps[3], minJumps[4]) = 1
minJumps[0] = 1 + min(minJumps[1], minJumps[2]) = 2

cache at end: [2, 1, 2, 1, 0]
>>>> return minJumps[0]

######

psuedocode >>>>>>
  intialize cache [inf, inf, inf, inf, 0]
  throw cache into helper function with 0 as starting point
  return the value of cache[0]

  helper function:
    if cache[i] != inf:
      return cache[i]

    for step in range(1, nums[i] + 1):
      cache[i] = min(cache[i], minJumpsHelper[i + step])

    return cache[i]

"""
from math import inf
from typing import List


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        # initialize the cache
        cache = [inf for num in nums]

        # set the base case
        cache[len(nums) - 1] = 0

        # throw the cache into a helper function
        return self.minJumpsHelper(nums, 0, cache)

    def minJumpsHelper(self, nums: List[int], index: int, cache: List[int]) -> int:
        # if the index is out of range, return inf
        if index >= len(nums):
            return inf

        # if you've already solved this, then just return it
        if cache[index] != inf:
            return cache[index]

        # if 0 steps available, return inf
        elif nums[index] == 0:
            return inf

        # otherwise, solve it, and return the solution
        for step in range(1, nums[index] + 1):
            cache[index] = min(cache[index], 1 + self.minJumpsHelper(nums, index + step, cache))

        return cache[index]


"""
EVALUATION:
            0  1  2  3  4
test case: [2, 3, 1, 1, 2]

####
cache at initialization: [inf, inf, inf, inf, 0]

------------- minJumpsHelper(0) 

for step in range(1, 3):
  cache[0] = min(cache[0], 1 + minJumpsHelper(index + step)) = 

  step = 1:
    cache[0] = min(inf, 1 + minJumpsHelper(1))
              |
              |
              |
              V

------------- minJumpsHelper(1)
for step in range(1, 4):
  cache[1] = min(cache[1], 1 + minJumpsHelper(index + step)) = 

  step = 1:
    cache[1] = min(inf, 1 + minJumpsHelper(2))

              |
              |
              |
              V

------------- minJumpsHelper(2)
for step in range(1, 2):
  cache[2] = min(cache[2], 1 + minJumpsHelper(index + step)) = 

  step = 1:
    cache[2] = min(inf, 1 + minJumpsHelper(3))

              |
              |
              |
              V

------------- minJumpsHelper(3)
for step in range(1, 2):
  cache[3] = min(cache[3], 1 + minJumpsHelper(index + step)) = 

  step = 1:
    cache[3] = min(inf, 1 + minJumpsHelper(4))

              |
              |
              |
              V

------------- minJumpsHelper(4)

BASE CASE REACHED
cache[4] != inf
XXX return 0

              |
              |
              |
              V

------------- minJumpsHelper(3)
for step in range(1, 2):
  cache[3] = min(cache[3], 1 + minJumpsHelper(index + step)) = 

  step = 1:
    cache[3] = min(inf, 1 + minJumpsHelper(4)) = min(inf, 1 + 0) = 1

cache is now: [inf, inf, inf, 1, 0]

XXX return 1

              |
              |
              |
              V

------------- minJumpsHelper(2)
for step in range(1, 2):
  cache[2] = 1 + min(cache[2], minJumpsHelper(index + step)) = 

  step = 1:
    cache[2] = min(inf, 1 + minJumpsHelper(3)) = min(inf, 1 + 1) = 2

cache is now: [inf, inf, 2, 1, 0]

XXX return 2

              |
              |
              |
              V

------------- minJumpsHelper(1)
for step in range(1, 4):
  cache[1] = 1 + min(cache[1], minJumpsHelper(index + step)) 

  step = 1:
    cache[1] = min(inf, 1 + minJumpsHelper(2)) = min(inf, 1 + 2) = 3

  step = 2:
    cache[1] = min(3, 1 + minJumpsHelper(3)) = min(3, 1 + 1) = 2

  step = 3:
    cache[1] = min(2, 1 + minJumpsHelper(4)) = min(2, 1 + 0) = 1

cache is now: [inf, 1, 2, 1, 0]

XXXX return 1

              |
              |
              |
              V

------------- minJumpsHelper(0) 

for step in range(1, 3):
  cache[0] = min(cache[0], 1 + minJumpsHelper(index + step)) = 

  step = 1:
    cache[0] = min(inf, 1 + minJumpsHelper(1)) = min(inf, 1 + 1) = 2

  step = 2:
    cache[0] = min(2, 1 + minJumpsHelper(2)) = min(2, 1 + 2) = 2

cache is now: [2, 1, 2, 1, 0]

XXX return 2

"""

testCase1 = [2, 3, 1, 1, 4]
testCase2 = [2, 3, 0, 1, 4]

solution = Solution()
print(solution.minJumps(testCase1))
print(solution.minJumps(testCase2))