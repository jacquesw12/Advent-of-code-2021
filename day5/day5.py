#!/usr/bin/env python3

import pathlib
import numpy as np

def read_input(file):
    list_segments = []
    for line in file.readlines():
        seg1_2 = line.strip('\n').split('->')

        segs = []
        for seg in seg1_2:
            split = [int(x) for x in seg.split(',')]
            segs.append(split)
                
        list_segments.append(segs)
    return list_segments


# The problem uses coordinates in x,y. Numpy uses the matrix notation.
# This is why x is use for the matrix column and y for the matrix row.
# The visualisation is then the same as described in the problem.
def update_matrix_part1(mat, segs):
    for seg in segs:
        x1, y1 = seg[0]
        x2, y2 = seg[1]

        if x1 == x2:
            if y1 < y2:
                for i in range(y1, y2 + 1):
                    mat[i][x1] += 1
            if y2 < y1:
                for i in range(y2, y1 + 1):
                    mat[i][x1] += 1

        if y1 == y2:
            if x1 < x2:
                for i in range(x1, x2 + 1):
                    mat[y1][i] += 1
            if x2 < x1:
                for i in range(x2, x1 + 1):
                    mat[y1][i] += 1


def update_matrix_part2(mat, segs):
    for seg in segs:
        x1, y1 = seg[0]
        x2, y2 = seg[1]

        # Checks that the directing vector is perpendicular to (1,-1)
        if ((x1-x2) - (y1-y2) == 0): 
            if x1 < x2 and y1 < y2:
                for i, j in zip(range(x1, x2+1), range(y1, y2+1)):
                    mat[j][i] += 1
            if x1 > x2 and y1 > y2:
                for i, j in zip(range(x2, x1+1), range(y2, y1+1)):
                    mat[j][i] += 1

        # Checks that the directing vector is perpendicular to (1,1)
        if ((x1-x2) + (y1-y2) == 0):
            if x1 < x2 and y1 > y2:
                for i, j in zip(range(x1, x2+1), reversed(range(y2, y1+1))):
                    mat[j][i] += 1
            if x1 > x2 and y1 < y2:
                for i, j in zip(reversed(range(x2, x1+1)), range(y1, y2+1)):
                    mat[j][i] += 1


def main():
    src_dir = pathlib.Path(__file__).parent
    with open(src_dir / 'input.txt', 'r') as file:
        list_segments = read_input(file)
        matrix = np.zeros((1000,1000))

        update_matrix_part1(matrix, list_segments)
        solution1 = np.count_nonzero(matrix >= 2)
        print(f'Solution part 1: {solution1}')

        update_matrix_part2(matrix, list_segments)
        solution2 = np.count_nonzero(matrix >= 2)
        print(f'Solution part 2: {solution2}')


if __name__ == '__main__':
    main()
