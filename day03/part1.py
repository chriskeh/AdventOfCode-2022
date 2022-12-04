#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"

def wert(buchstabe):
    if buchstabe.islower():
        return ord(buchstabe) - 96
    else:
        return ord(buchstabe) - 38

def main():

    # split line in two halves
    # find identic char in left and right half
    # calc value of char (a=1, .., z=26, A=27, ..., Z=52)
    # sum up values

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    result1 = 0
    with open(input_data_file) as file:
        for line in file:
            line = line.strip()
            links = line[0:len(line)//2]
            links = list(set(links))
            rechts = line[len(line)//2:]
            rechts = list(set(rechts))
            # print("L: {}, R: {}".format(links, rechts))
            for zeichen in links:
                if zeichen in rechts:
                    result1 += wert(zeichen)
                    # print('{} ist {}'.format(zeichen, value))
                    break

    print("Result Part 1: {}".format(result1))
    # print("Result Part 2: {}".format(result2))


if __name__ == "__main__":
    main()
