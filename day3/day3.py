#!/usr/bin/env python3

from pathlib import Path
import numpy as np

def create_matrix(file, mat):
  file.seek(0)
  for ix_line,line in enumerate(file):
    for ix_col,char in enumerate(line):
      if char == '0':
        mat[ix_line, ix_col] = 0
      if char == '1':
        mat[ix_line, ix_col] = 1

def init_matrix(file):
  nb_lines = 0
  nb_columns = 0
  for line in file:
    nb_lines += 1
  file.seek(0)
  for line in file.readlines():
    line = line.strip()
    for char in line:
      nb_columns += 1
    break
  return np.empty((nb_lines, nb_columns,))

def sum_column(mat, col_ix):
    return sum(mat[:,col_ix])

def part1(mat):
    bin_list = []
    line_size = mat.shape[0]
    col_size = mat.shape[1]
    for column in mat.T:
        if sum(column) > line_size / 2:
            bin_list.append('1')
        else:
            bin_list.append('0')
    bin_num = "".join(bin_list)

    inverse = bin_num.replace('1', '2')
    inverse = inverse.replace('0', '1')  
    inverse = inverse.replace('2', '0')
    return int(bin_num, 2), int(inverse, 2) 

def remove_lines_for_column_starting_with(mat, zero_or_one, col_ix):
    if mat.shape[0] == 1:
        return mat
    ix_to_remove = []
    for ix, line in enumerate(mat):
        if int(line[col_ix]) == zero_or_one:
            ix_to_remove.append(ix)
    
    mat = np.delete(mat, ix_to_remove, 0)
    return mat

def find_oxygen_rating(mat):
    amount_col = mat.shape[1]
    
    for ix in range(0, amount_col):
        if sum_column(mat, ix) > mat.shape[0] / 2:
            mat = remove_lines_for_column_starting_with(mat, 0, ix)
        elif sum_column(mat, ix) < mat.shape[0] / 2:
            mat = remove_lines_for_column_starting_with(mat, 1, ix)
        else:
            mat = remove_lines_for_column_starting_with(mat, 0, ix)

    bin_num = ''
    for elt in mat[0]:
        bin_num += str(int(elt))
    return int(bin_num, 2)


def find_CO2_rating(mat):
    amount_col = mat.shape[1]
    
    for ix in range(0, amount_col):
        if sum_column(mat, ix) > mat.shape[0] / 2:
            mat = remove_lines_for_column_starting_with(mat, 1, ix)
        elif sum_column(mat, ix) < mat.shape[0] / 2:
            mat = remove_lines_for_column_starting_with(mat, 0, ix)
        else:
            mat = remove_lines_for_column_starting_with(mat, 1, ix)

    bin_num = ''
    for elt in mat[0]:
        bin_num += str(int(elt))
    return int(bin_num, 2)


def part2(mat):
    oxygen_rate = find_oxygen_rating(mat)
    CO2_rate = find_CO2_rating(mat)
    return oxygen_rate, CO2_rate
    

def main():
    src_dir = Path(__file__).parent
    with open(src_dir / 'input.txt', 'r') as file:
        mat = init_matrix(file)
        create_matrix(file, mat)
        gamma_rate, epsilon_rate = part1(mat)
        print(f'Result part 1 : {gamma_rate * epsilon_rate}')

        oxygen_rate, CO2_rate = part2(mat)
        print(f'Result part 2 : {oxygen_rate * CO2_rate}')


if __name__ == '__main__':
    main()

