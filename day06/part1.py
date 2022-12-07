#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"

groesse = 14

def all_are_different(wort):
    sortiertes_wort = sorted(list(wort))
    for i in range(0,groesse-1):
        if sortiertes_wort[i] == sortiertes_wort[i+1]:
            return False

    return True

def main():

    with open(input_data_file) as file:
        for line in file:
            line = line.strip()

            i = groesse
            while i < len(line):
                sub = line[i-groesse:i]

                if line[i] in line[i-groesse:i]:
                    i += 1
                else:
                    if all_are_different(sub):
                        break
                    else:
                        i += 1

            print(i, line)

if __name__ == "__main__":
    main()
