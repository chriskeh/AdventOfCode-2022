#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"

def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    # two comma-separated ranges
    # if one range is fully contained in the other, count it
    # return sum of those contained lines
    # 1-2, 2-3
    # 2-2, 2-3
    # 1-2, 2-3


    result1 = 0
    result2 = 0
    with open(input_data_file) as file:
        for line in file:
            # print(line)
            eins, zwei = line.split(',')
            min_eins, max_eins = eins.split('-')
            min_zwei, max_zwei = zwei.split('-')

            if int(min_eins) >= int(min_zwei) and int(max_eins) <= int(max_zwei):
                # print("eins in zwei")
                result1 += 1
            else:
                if int(min_zwei) >= int(min_eins) and int(max_zwei) <= int(max_eins):
                    # print("zwei in eins")
                    result1 += 1

            if int(max_eins) < int(min_zwei):
                continue
            else:
                if int(max_zwei) < int(min_eins):
                    # print("eins in zwei")
                    continue
                else:
                    result2 += 1

    print("Result Part 1: {}".format(result1))
    print("Result Part 2: {}".format(result2))


if __name__ == "__main__":
    main()
