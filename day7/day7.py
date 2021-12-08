#!/usr/bin/env python3

import sys
import pathlib


def shortest_fuel_part1(positions):
    max_pos = max(positions)
    min_pos = min(positions)

    vec_diffs = []
    for i in range(min_pos, max_pos):
        sum_diff = 0
        for j in range(len(positions)):
            sum_diff += abs(positions[j] - i)
        vec_diffs.append(sum_diff)
    print(f'Solution part 1 : {min(vec_diffs)}')


def distance_part2(n):
    return (n * (n+1)) // 2


def shortest_fuel_part2(positions):
    max_pos = max(positions)
    min_pos = min(positions)

    vec_diffs = []
    for i in range(min_pos, max_pos):
        sum_diff = 0
        for j in range(len(positions)):
            sum_diff += distance_part2(abs(positions[j] - i))
        vec_diffs.append(sum_diff)
    print(f'Solution part 2 : {min(vec_diffs)}')


def solution_part1_shorter(positions):
    min_p1 = sys.maxsize
    for i in range(min(positions), max(positions)):
        dist = sum([abs(pos - i) for pos in positions])
        min_p1 = min(dist, min_p1)
    print(f'Solution shorter code part 1 : {min_p1}')


def solution_part2_shorter(positions):
    min_p2 = sys.maxsize
    for i in range(min(positions), max(positions)):
        dist = sum([distance_part2(abs(pos - i)) for pos in positions])
        min_p2 = min(dist, min_p2)
    print(f'Solution shorter code part 2 : {min_p2}')

    


def main():
    src_dir = pathlib.Path(__file__).parent
    with open(src_dir / 'input.txt', 'r') as file:
        input_list = [int(elt) for elt in file.readline().strip('\n').split(',')]

        shortest_fuel_part1(input_list)
        shortest_fuel_part2(input_list)

        # After some refactoring to make the code more "pythonic"
        solution_part1_shorter(input_list)
        solution_part2_shorter(input_list)
        


if __name__ == '__main__':
    main()
