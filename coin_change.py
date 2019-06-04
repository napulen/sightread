# Copyright 2019 Nestor Napoles Lopez

import copy


def count(coins, number_of_coins, amount, trajectory=[]):
    if (amount == 0):
        print(trajectory)
        return 1

    if (amount < 0):
        return 0
    
    results = 0

    for i in range(number_of_coins):
        new_trajectory = trajectory[:]
        new_trajectory.append(coins[i])
        results += count(coins, number_of_coins, amount - coins[i], new_trajectory)
    
    return results

if __name__ == '__main__':
    coins = [1, 2, 3]
    number_of_coins = len(coins)

    amount = 4

    print(count(coins, number_of_coins, amount))
    