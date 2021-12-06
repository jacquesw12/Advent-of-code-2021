#!/usr/bin/env python3

import pathlib
import numpy as np

def create_matrices_from_input(file):
    file.readline()
    boards = []
    cur_board = []
    for line in file:
        if line in ['\n', '\r\n']:
            boards.append(cur_board)
            cur_board=[]
        else:
            cur_board.append([int(x) for x in line.strip('\n').split()])

    matrices = []
    for board in boards:
        mat = np.array([np.array(elt) for elt in board])
        matrices.append(mat)

    return matrices


def init_control_matrices(amount_control_matrices):
    control_matrices = []
    for i in range(amount_control_matrices):
        control_matrices.append(np.zeros((5,5)))
    return control_matrices


def update_control_matrices(mats, control_mats, nb):
    for i, mat in enumerate(mats):
        ixs = np.where(mat == nb)
        control_mat = control_mats[i]
        control_mat[ixs[0], ixs[1]] = 1


def check_if_bingo(mat):
    for row in mat:
        if sum(row) == 5:
            return True
    for col in np.transpose(mat):
        if sum(col) == 5:
            return True
    return False
    

def find_mat_first_bingo(bingo_input, matrices):
    control_matrices = init_control_matrices(len(matrices))

    for num in bingo_input:
        update_control_matrices(matrices, control_matrices, num)
        for ix, control_mat in enumerate(control_matrices):
            if check_if_bingo(control_mat):
                return matrices[ix], control_mat, num


def find_mat_last_bingo(bingo_input, matrices):
    control_matrices = init_control_matrices(len(matrices))
    list_mat_bingo = []
    last_num = -1

    for num in bingo_input:
        update_control_matrices(matrices, control_matrices, num)

        for ix, mat in enumerate(control_matrices):
            if check_if_bingo(mat) and ix not in list_mat_bingo:
                list_mat_bingo.append(ix)
                last_num = num

    return list_mat_bingo[-1], last_num


def find_mat_with_ix(bingo_input, matrices, bg_ix):
    control_matrices = init_control_matrices(len(matrices))
    for num in bingo_input:
        update_control_matrices(matrices, control_matrices, num)

        for ix, mat in enumerate(control_matrices):
            if ix == bg_ix and check_if_bingo(mat):
                return mat, matrices[ix]


def calculate_mat_score(mat, control_mat, bingo_number):
    ixs = np.where(control_mat == 0)
    mat_sum = 0

    for i in range(0, len(ixs[0])):
        mat_sum += mat[ixs[0][i], ixs[1][i]]

    return mat_sum * bingo_number
    

def part1(bingo_input, matrices):
    mat, control_mat, bg_nb = find_mat_first_bingo(bingo_input, matrices)
    board_score = calculate_mat_score(mat, control_mat, bg_nb)

    print(f'Solution part1: {board_score}')


def part2(bingo_input, matrices):
    bg_ix, last_num = find_mat_last_bingo(bingo_input, matrices)
    last_control_mat, last_mat = find_mat_with_ix(bingo_input, matrices, bg_ix)
    board_score = calculate_mat_score(last_mat, last_control_mat, last_num)

    print(f'Solution part2: {board_score}')
    

def main():
    src_dir = pathlib.Path(__file__).parent
    with open(src_dir / 'input.txt', 'r') as file:

        bingo_input = [int(x) for x in file.readline().strip('\n').split(',')]

        matrices = create_matrices_from_input(file)

        part1(bingo_input, matrices)
        part2(bingo_input, matrices)

            
if __name__ == '__main__':
    main()
