#!/usr/bin/env /usr/bin/python36
import numpy as np

# input_data_file = "part1_test.data"
input_data_file = "part1.data"


def sichtbar_von_links(liste, x):
    count = x - 1
    while count >= 0:
        if liste[count] >= liste[x]:
            return False
        count -= 1
    return True


def sichtbar_von_rechts(liste, x):
    count = x + 1
    while count <= len(liste) - 1:
        if liste[count] >= liste[x]:
            return False
        count += 1
    return True


def erzeuge_true_false_matrix(groesse):
    true_line = [True] * groesse

    false_line = [False] * (groesse - 2)
    false_line.insert(0, True)
    false_line.append(True)

    foo = [true_line]
    for i in range(0, groesse - 2):
        foo.append(false_line)
    foo.append(true_line)
    return np.array(foo)


def main():

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
    sichtbar = erzeuge_true_false_matrix(matrix_groesse)

    # Spalten
    for i in range(1, matrix_groesse - 1):
        for j in range(1, matrix_groesse - 1):
            if sichtbar_von_links(matrix[:, i], j):
                sichtbar[j, i] = True
                continue
            elif sichtbar_von_rechts(matrix[:, i], j):
                sichtbar[j, i] = True
                continue

    # Zeilen
    for i in range(1, matrix_groesse - 1):
        for j in range(1, matrix_groesse - 1):
            if sichtbar_von_links(matrix[i, :], j):
                sichtbar[i, j] = True
                continue
            elif sichtbar_von_rechts(matrix[i, :], j):
                sichtbar[i, j] = True
                continue

    # print(matrix)
    # print(sichtbar)
    print(np.count_nonzero(sichtbar))


if __name__ == "__main__":
    main()
