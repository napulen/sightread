# Copyright 2019 Nestor Napoles Lopez
import copy

solutions = {}

def solve(problem):
    if problem == 0:
        return True
    elif problem < 0:
        return False
    elif problem in solutions:
        return solutions[problem]
    else:
        compute_solution(problem)


def count(coins, amount, trajectory={}):
    if (amount == 0):
        # print(trajectory)
        return 1

    if (amount < 0):
        return 0

    results = 0

    for coin in coins:
        new_amount = amount - coin
        new_trajectory = {}
        print('{}_{}'.format(coin, new_amount))
        if not new_amount in lookup:
            lookup[new_amount] = count(coins, new_amount, new_trajectory)
        results += lookup[new_amount]
        trajectory[coin] = new_trajectory


    return results

if __name__ == '__main__':
    coins = [1, 2, 3] #, 4, 6, 8, 12, 16]
    amount = 4
    print(count(coins, amount))
