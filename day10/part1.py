#!/usr/bin/env /usr/bin/python36

# input_data_file = "part1_test.data"
input_data_file = "part1.data"

grenze_initial = 20
grenze_add = 40


class Geraet:
    def __init__(self):
        self.strength = 0
        self.wert = 1
        self.schritt = 1
        self.match = grenze_initial

    def check_and_increase(self, parameter):
        if self.match == parameter:
            temp = parameter * self.wert
            self.strength += temp
            self.match += grenze_add

    def execute(self, anweisung):
        if anweisung.startswith("noop"):
            self.noop()
        elif anweisung.startswith("add"):
            nothing, parameter = anweisung.split()
            self.add_value(parameter)

    def add_value(self, mehr):
        self.check_and_increase(self.schritt)
        self.check_and_increase(self.schritt+1)
        self.wert += int(mehr)
        self.schritt += 2

    def noop(self):
        self.check_and_increase(self.schritt)
        self.schritt += 1


def main():

    geraet = Geraet()

    with open(input_data_file) as file:
        for line in file:
            line = line.strip()
            geraet.execute(line)

    print("Part 1: {}".format(geraet.strength))


if __name__ == "__main__":
    main()
