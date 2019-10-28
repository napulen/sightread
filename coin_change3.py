# Copyright 2019 Nestor Napoles Lopez
import pprint

solutions = {0: []}

def recurse(problem, branch=[]):
    if problem == 0:
        # TODO: reverse the rhythmic durations
        print(branch)
        return
    for solution in solutions[problem]:
        note, subproblem = solution
        recurse(subproblem, branch + [note])

def create_tree(coins, amount):
    for problem in range(1, amount + 1):
        print(problem)
        solution_list = []
        for coin in coins:
            subproblem = problem - coin
            if subproblem < 0:
                # No solution
                break
            solution_list += [(coin, subproblem)]
        solutions[problem] = solution_list

if __name__ == '__main__':
    coins = [1, 2, 4, 8, 16, 32]
    coins_reversed = list(reversed(coins))
    amount = 16
    create_tree(coins, amount)
    pprint.pprint(solutions)
    recurse(amount)
