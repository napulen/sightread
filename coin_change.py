# Copyright 2019 Nestor Napoles Lopez
import copy
import pprint

solutions = {}

def solve(problem):
    if problem in solutions:
        return solutions[problem]
    elif problem == 0:
        return [[]]
    elif problem < 0:
        return []
    else:
        print('Error')


def get_combinations(coins, amount):
    for amount_step in range(1, amount + 1):
        print(amount_step)
        solution_list = []
        for coin in coins:
            prefix = [coin]
            problem = amount_step - coin
            solution = solve(problem)
            if solution:
                branch = [prefix + sol for sol in solution]
                solution_list += branch
        solutions[amount_step] = solution_list

if __name__ == '__main__':
    coins = [1, 2, 4, 8, 16, 32]
    coins_reversed = list(reversed(coins))
    amount = 32
    get_combinations(coins, amount)
    for solution in solutions[amount]:
        solution_reversed = [coins_reversed[coins.index(x)] for x in solution]
        print(solution_reversed)
    print(len(solutions[amount]))
