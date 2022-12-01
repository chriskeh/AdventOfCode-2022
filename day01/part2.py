#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"


def slurp_input(input_file):
    """
    Read the input file. It contains one number per line.
    Reading it in the with-statement creates a list of strings, not numbers.
    So a second command is necessary, which applies the function 'int' to the iterable 'my_list' which
    converts each element of the iterable into an int and then create a list from that again.  Et voila!
    :param input_file:
    :return: list of integers
    """
    with open(input_file) as f:
        my_list = list(f)
    my_list = list(map(int, my_list))
    return my_list


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    # numbers = slurp_input(input_data_file)

    calories = []
    sum = 0


    with open(input_data_file) as file:
        for line in file:
            # Strip of "\n"
            line = line.rstrip()
            if line == "":
                # End of block, add value to list
                calories.append(sum)
                # reset sum for next block
                sum = 0
            else:
                # a number, let's add it
                sum += int(line)

    summe = 0
    calories = sorted(calories)
    print(calories)
    for zahl in calories[-3:]:
        summe += zahl
    print("Summe der drei groessten: {}".format(summe))

if __name__ == "__main__":
    main()
