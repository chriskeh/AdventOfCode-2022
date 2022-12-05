#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"

def get_part(stapel, count):
    result = []
    for i in range(0, count):
        result.append(stapel.pop())
    return result



def main():
    stapel = []
    stapel.append(list("HRBDZFLS"))
    stapel.append(list("TBMZR"))
    stapel.append(list("ZLCHNS"))
    stapel.append(list("SCFJ"))
    stapel.append(list("PGHWRZB"))
    stapel.append(list("VJZGDNMT"))
    stapel.append(list("GLNWFSPQ"))
    stapel.append(list("MZR"))
    stapel.append(list("MCLGVRT"))

    with open(input_data_file) as file:
        for line in file:
            line = line.strip()
            zeile = line.split(" ")
            anzahl = int(zeile[1])
            woher = int(zeile[3]) - 1
            wohin = int(zeile[5]) - 1

            temporary = get_part(stapel[woher], anzahl)
            stapel[wohin].extend(temporary)

    # Now get the top of the crates
    result1 = []
    for i in range(0,len(stapel)):
        result1.append(stapel[i][-1])

    print(''.join(result1))

    # print("Result Part 1: {}".format(result1))
    # print("Result Part 2: {}".format(result2))


if __name__ == "__main__":
    main()
