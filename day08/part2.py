#!/usr/bin/env /usr/bin/python36
import numpy as np

# input_data_file = "part1_test.data"
input_data_file = "part1.data"



def get_left(vektor, index):
    max_view = 1
    count = index - 1
    while count > 0:
        foo1 = vektor[count]
        foo2 = vektor[index]
        if vektor[count] < vektor[index]:
            max_view += 1
            count -= 1
        else:
            return max_view
    return max_view

def get_right(vektor, index):
    max_view = 1
    count = index + 1
    while count < len(vektor) - 1:
        foo1 = vektor[count]
        foo2 = vektor[index]
        if vektor[count] < vektor[index]:
            max_view += 1
            count += 1
        else:
            return max_view
    return max_view

def main():

    max_score = 0

    # Read the matrix from the file
    read_matrix = []
    with open(input_data_file) as file:
        for line in file:
            line = line.strip()
            # We can ignore the ls command for now
            zeile = list(line)
            # print(zeile)
            read_matrix.append(zeile)

    # macht es spaeter einfacher
    matrix_groesse = len(zeile)

    matrix = np.array(read_matrix)

    # find the best spot
    for i in range(1, matrix_groesse - 1):
        for j in range(1, matrix_groesse - 1):
            zeile = matrix[i, :]
            left = get_left(zeile, j)
            right = get_right(zeile, j)
            foo = left
            spalte = matrix[:, j]
            up = get_left(spalte, i)
            down = get_right(spalte, i)
            score = left * right * up * down
            print("i: {}, j; {}, wert: {}, score: {}".format(i, j, matrix[i][j], score))
            if score > max_score:
                max_score = score


    print(max_score)


if __name__ == "__main__":
    main()
