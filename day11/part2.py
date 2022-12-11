#!/usr/bin/env /usr/bin/python36
from pprint import pprint

import numpy as np

# input_data_file = "part1_test.data"
input_data_file = "part1.data"

def slurp_input(input_file):
    # monkeys = [
    #             { # Monkey 0
    #               starters: [ 78, 89 ],
    #               divisor: 12,
    #               test_wahr: 12,
    #               test_falsch: 23,
    #             },
    #             { # Monkey 1
    #               starters: [ 1, 2 ],
    #               divisor: 23,
    #               test_wahr: 9,
    #               test_falsch: 67,
    #             },
    #           ]
    # inspected = [ 12, 23, 99, 3, ... ]

    monkey_liste = []
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Monkey"):
                monkey = {}
            elif line.startswith("Starting items:"):
                temp = line.split(":")[1].split(",")
                monkey["starters"] = [ int(x) for x in temp]
            elif line.startswith("Operation:"):
                monkey["operation"] = line.split("= ")[1]
            elif line.startswith("Test:"):
                monkey["divisor"] = int(line.split("by ")[1])
            elif line.startswith("If true:"):
                monkey["aktion_wahr"] = int(line.split("monkey ")[1])
            elif line.startswith("If false:"):
                monkey["aktion_falsch"] = int(line.split("monkey ")[1])
            elif line == "":
                monkey_liste.append(monkey)
            else:
                print("Unknown line: X{}X".format(line))
    monkey_liste.append(monkey)
    return monkey_liste


def addiere(worry, todo):
    operand = int(todo.split("+ ")[1])
    return worry + operand


def teilbar(new_worry, divisor):
    result = int(new_worry) % int(divisor) == 0
    return result


def wohin(worry, todo, divisor, next_wahr, next_falsch):
    if "+" in todo:
        new_worry = addiere(worry, todo)
    elif "*" in todo:

        # Too slow :(
        operand = todo.split(" * ")[1]
        if operand == "old":
            print("Square")
            new_worry = worry ** 2
        else:
            new_worry = worry * int(operand)

    else:
        print("In wohin: Unknown operation: {}".format(todo))
        new_worry = 0
    if teilbar(new_worry, divisor):
        next_monkey = next_wahr
    else:
        next_monkey = next_falsch

    return next_monkey, new_worry

def main():

    # Read the monkeys from the file
    monkey = slurp_input(input_data_file)

    # pprint(monkey)

    inspected = [0] * len(monkey)
    # for round in range(1, 2):
    # for round in range(1, 21):
    for round in range(1, 10001):
        print("Runde: {}".format(round))

        for id in range(0, len(monkey)):
            # print("Monkey {}".format(id))
            for worry in monkey[id]["starters"]:
                # print("Worries {}".format(worry))
                todo = monkey[id]["operation"]
                divisor = monkey[id]["divisor"]
                next_wahr = monkey[id]["aktion_wahr"]
                next_falsch = monkey[id]["aktion_falsch"]

                next_monkey, new_worry = wohin(worry, todo, divisor, next_wahr, next_falsch)
                inspected[id] += 1
                monkey[next_monkey]["starters"].append(new_worry)

            # der Affe hat alle abgegeben, also hat er nichts mehr
            monkey[id]["starters"] = []

    highest = sorted(inspected)[-2:]
    monkey_business = highest[0] * highest[1]
    print("Monkey Business: {}".format(monkey_business))


if __name__ == "__main__":
    main()
