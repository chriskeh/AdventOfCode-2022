#!/usr/bin/env /usr/bin/python36

input_data_file = "part1.data"

def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    ######  Part 1
    # A Rock
    # B Paper
    # C Scissors

    # X Rock 1
    # Y Paper 2
    # Z Scissors 3

    # 0 if you lost
    # 3 if the round was a draw
    # 6 if you won
    werte1 = {"A": {'X': 3 + 1,
                   'Y': 6 + 2,
                   'Z': 0 + 3
                   },
             "B": {'X': 0 + 1,
                   'Y': 3 + 2,
                   'Z': 6 + 3
                   },
             "C": {'X': 6 + 1,
                   'Y': 0 + 2,
                   'Z': 3 + 3
                   }
             }


    ######    Part 2
    # A Rock
    # B Paper
    # C Scissors

    # X Loose
    # Y Draw
    # Z Win

    # 0 if you lost
    # 3 if the round was a draw
    # 6 if you won

    werte2 = {"A": {'X': 0 + 3,
                    'Y': 3 + 1,
                    'Z': 6 + 2
                    },
              "B": {'X': 0 + 1,
                    'Y': 3 + 2,
                    'Z': 6 + 3
                    },
              "C": {'X': 0 + 2,
                    'Y': 3 + 3,
                    'Z': 6 + 1
                    }
              }

    # Code does Part 1 and Part2
    result1 = 0
    result2 = 0
    with open(input_data_file) as file:
        for line in file:
            eins, zwei = line.split()
            result1 += werte1[eins][zwei]
            result2 += werte2[eins][zwei]

    print("Result Part 1: {}".format(result1))
    print("Result Part 2: {}".format(result2))


if __name__ == "__main__":
    main()
