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
        print('Error')


def get_combinations(coins, amount):
    for amount_step in range(1, amount + 1):
        print(amount_step)
        solution_list = []
        for coin in coins:
            prefix = [coin]
            new_amount = amount_step - coin
            solution = solve(new_amount)
            if solution:
                if isinstance(solution, list):
                    for combination in solution:
                        solution_list.append(prefix + combination)
                else:
                    solution_list.append(prefix)
        solutions[amount_step] = solution_list

if __name__ == '__main__':
    coins = [1, 2, 3, 4, 6, 8, 12, 16]
    amount = 32
    get_combinations(coins, amount)
    for solution in solutions[amount]:
        print(solution)
