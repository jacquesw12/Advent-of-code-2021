#!/usr/bin/env python3

import sys
import pathlib
from more_itertools import triplewise

def part1(input_list):
    prev_elt = sys.maxsize
    counter = 0
    for elt in input_list:
        if elt > prev_elt:
            counter += 1
        prev_elt=elt
    return counter

def part2(input_list):
    counter = 0
    size = len(input_list)
    prev_sum = sys.maxsize
    for i in range(0,size-2):
        cur_sum = sum(input_list[i:i+3])
        if cur_sum > prev_sum:
            counter += 1
        prev_sum = cur_sum
    return counter
        
# Optimised solution, less quick and dirty
def part2_optimised(input_data):
    sums = [sum(input_data[i-3:i]) for i in range(3,len(input_data)+1)]
    return sum([sums[i-1] < sums[i] for i in range(1,len(sums))])

# With more_itertools
def part2_itertools(input_data):
    sums = list(triplewise(input_data))
    return sum([sum(sums[i-1]) < sum(sums[i]) for i in range(1,len(sums))])

# Function working for both part 1 and 2
def sum_sliding_window(input_data, window_size):
    sums = [sum(input_data[i-window_size:i]) for i in range(window_size, len(input_data)+1)]
    return sum([sums[i-1] < sums[i] for i in range(1,len(sums))])

def main():
    src_dir = pathlib.Path(__file__).parent
    with open(src_dir / 'input.txt', 'r') as file:
        input_list = [int(elt) for elt in file.read().splitlines()]

        result1 = part1(input_list)
        print(f'Result part 1 : {result1}')
        
        result2 = part2(input_list)
        print(f'Result part 2 : {result2}')
        
        result2_opt = part2_optimised(input_list)
        print(f'Result part 2 optimised : {result2_opt}')

        result2_iter = part2_itertools(input_list)
        print(f'Result part 2 more-itertools : {result2_iter}')
        
        result_part1_refactored = sum_sliding_window(input_list, 1)
        result_part2_refactored = sum_sliding_window(input_list, 3)
        print(f'Result part 1 refactored : {result_part1_refactored}')
        print(f'Result part 2 refactored : {result_part2_refactored}')

if __name__ == '__main__':
    main()

