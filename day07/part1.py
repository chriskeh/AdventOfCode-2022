#!/usr/bin/env /usr/bin/python36

input_data_file = "part1_test.data"
input_data_file = "part1.data"


class Baum:
        def __init__(self, art, groesse, dotdot, name):
            self.dotdot = dotdot    # Parent
            self.name = name
            self.art = art          # dir oder datei
            self.groesse = groesse  # Groesse, 0 fuer dirs
            self.children = {}      # inhalt des Dirs, leeres Dict fuer leeres Dir und fuer Datei

        def add_child(self, name, ding):
            # self.dotdot = self
            self.children[name] = ding

        def change_dir(self, name):
            if name == "..":
                return self.dotdot
            else:
                return self.children[name]


def groesse_von(verzeichnis):
    for ding in verzeichnis.children.values():
        if ding.art == "datei":
            verzeichnis.groesse += ding.groesse
        elif ding.art == "dir":
            groesse_von(ding)
            verzeichnis.groesse += ding.groesse


def sum_small_dirs(verzeichnis, sum, max):
    for ding in verzeichnis.children.values():
        if ding.art == "dir":
            sum = sum_small_dirs(ding, sum, max)

    if verzeichnis.groesse <= max:
        sum += verzeichnis.groesse

    return sum


def main():

    # Build the tree
    wurzel = Baum("dir", 0, None, "wurzel")
    localdir = wurzel
    with open(input_data_file) as file:
        for line in file:
            line = line.strip()
            # We can ignore the ls command for now
            if line.startswith("$ ls"):
                continue

            # act on the cd command
            elif line.startswith("$ cd"):
                target = line[5:]
                if target == "/":
                    localdir = wurzel
                else:
                    localdir = localdir.change_dir(target)

            # OK, we have a directory
            elif line.startswith("dir "):
                name = line[4:]
                new_dir = Baum("dir", 0, localdir, name)
                localdir.add_child(name, new_dir)

            # everything else should be a number
            else:
                groesse, name = line.split()
                new_datei = Baum("datei", int(groesse), localdir, name)
                localdir.add_child(name, new_datei)

    # Now calculate and store the directory sizes
    groesse_von(wurzel)

    # now find all dirs >= 100000
    max_groesse = 100000
    total = sum_small_dirs(wurzel, 0, max_groesse)

    print(total)


if __name__ == "__main__":
    main()
