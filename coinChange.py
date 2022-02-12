"""
This looks like a DP problem, because we're trying to optimize

recurrence relation:
fewestCoins[amount]_i =
    min(1 + fewestCoins[amount - coins[i]]_i, fewestCoins[amount]_i+1)

BASE CASE:
    - fewestCoins[amount][i] = 0, when amount = 0
    - fewestCoins[amount][i] = 0, when i >= len(coins)

meaning, the fewest coins is the minimum of:
    - 1 + whatever the minimum is when you take the coin
    - whatever the minimum is when you don't take the coin

#########

psuedocode:
    create a cache of len(amount) + 1 * len(coins) + 1 and initialize all values to inf
    when amount = 0, initialize to 0

    iterate through rows and cols and solve for values

        if coin <= amount:
            minCoinsWithCoin = 1 + cache[amount - nums[i]]

        cache[amount][i] = min(minCoinsWithCoin, cache[amount][i - 1])

    return cache[len(coins) - 1)][amount]

[     0    1    2    3    4    5    6    7    8    9   10    11
  0  [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
  1  [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
  2  [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
  5  [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
    ]

if coin <= amount:
    minCoinsWithCoin = 1 + cache[amount - nums[i]]

cache[amount][i] = min(minCoinsWithCoin, cache[amount][i - 1])

   0   1    2    3
0 [0, inf, inf, inf]
2 [0, inf, 1, 1 + inf]

"""
from typing import List
from math import inf


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0

        # create a cache and intialize 0s
        cache = [[inf for amnt in range(amount + 1)] for coin in range(len(coins) + 1)]
        for row in range(len(coins) + 1):
            cache[row][0] = 0

        # iterate through rows and columns and solve subproblems
        for coin in range(1, len(cache)):
            for amnt in range(1, len(cache[0])):
                if coins[coin - 1] <= amnt:
                    # set the amount temporarily to 1 + subsolution of amnt - coin's value
                    cache[coin][amnt] = 1 + cache[coin][amnt - coins[coin - 1]]

                # set cached value to min of using coin versus not using coin
                cache[coin][amnt] = min(cache[coin][amnt], cache[coin - 1][amnt])

        if cache[len(coins)][amount] == inf:
            return -1

        else:
            return cache[len(coins)][amount]


"""
EVALUATION:
[     0    1    2    3    4    5    6    7    8    9   10    11
  0  [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
  1  [0,   1,   2,    3,   4,   5,  6,   7,   8,   9,  10,   11],
  2  [0,   1,   1,    2,   2,   3,  3,   4,   4,   5,   5,   6],
  5  [0,  1,    1,    2,   2,    1, 2,  2,    3,   3,  2,    3]
    ]

coins = [1,2,5], amount = 11

coin = 2
amnt = 3

"""
solution = Solution()
print(solution.coin_change([1,2,5], 11)) # expected = 3
print(solution.coin_change([2], 3)) # expected = -1
print(solution.coin_change([1], 0)) # expected = 0