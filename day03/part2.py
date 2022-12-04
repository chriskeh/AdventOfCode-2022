#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"



def gemeinsam(eins, zwei):
    result = ''
    eins = list(set(eins))
    zwei = list(set(zwei))
    for zeichen in eins:
        if zeichen in zwei:
            result += zeichen
            # print('{} ist {}'.format(zeichen, value))
    return result

def wert(buchstabe):
    if buchstabe.islower():
        return ord(buchstabe) - 96
    else:
        return ord(buchstabe) - 38

def main():

    # read three lines
    # find identical char in all three lines
    # calc value of char (a=1, .., z=26, A=27, ..., Z=52)
    # sum up values

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    result2 = 0
    with open(input_data_file) as file:
        for line1 in file:
            line1 = line1.strip()
            line2 = file.readline().strip()
            line3 = file.readline().strip()
            result2 += wert(gemeinsam(gemeinsam(line1, line2), line3))

    print("Result Part 2: {}".format(result2))
    # print("Result Part 2: {}".format(result2))


if __name__ == "__main__":
    main()
