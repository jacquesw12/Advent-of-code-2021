#!/usr/bin/env python3

import sys
import pathlib

def part1(inp):
    counter = 0
    for line in inp:
        for digit in line[1]:
            if len(digit) ==  2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                counter += 1
    print(f'Solution part 1: {counter}')


def find_missing_segs(dig):
    list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    output = []
    for seg in list_letters:
        if seg not in dig:
            output.append(seg)
    return output


def find_f(letter_not ,one):
    for letter in one:
        if letter != letter_not:
            return letter

def find_a(one, seven):
    for letter in seven:
        if letter not in one:
            return letter

def find_9(e, dig_one_seg_miss):
    for digit in dig_one_seg_miss:
        if e not in list(digit):
            return digit

def find_0(nine, six, dig_one_seg_missing):
    dig_one_seg_missing.remove(nine)
    dig_one_seg_missing.remove(six)
    return dig_one_seg_missing[0]
    
def find_e(five, six):
    missing_seg_6 = find_missing_segs(list(six))[0]
    missing_seg_5 = find_missing_segs(list(five))
    for letter in missing_seg_5:
        if letter != missing_seg_6:
            return letter

    
    
def find_5(six, dig_two_seg_missing):
    missing_seg_6 = find_missing_segs(list(six))[0]
    five = ''
    for dig in dig_two_seg_missing:
        missing_segs = find_missing_segs(list(dig))
        if missing_seg_6 in missing_segs:
            five = dig

    return five

def find_3_2(five, dig_two_seg_missing):
    missing_seg_5 = find_missing_segs(list(five))
    three = ''
    two = ''
    dig_two_seg_missing.remove(five)
    for dig in dig_two_seg_missing:
        missing_segs = find_missing_segs(list(dig))
        if bool(set(missing_seg_5) & set(missing_segs)):
            three = dig
        if not bool(set(missing_seg_5) & set(missing_segs)):
            two = dig
    return two, three

def find_numbers(dig_one_seg_miss, one, dig_two_seg_missing, numbers_map):
    six = ''
    for dig in dig_one_seg_miss:
        missing_segs = find_missing_segs(list(dig))
        if missing_segs[0] in list(one):
            six = dig

    numbers_map[''.join(sorted(six))] = 6
    five = find_5(six, dig_two_seg_missing)
    numbers_map[''.join(sorted(five))] = 5
    

    e = find_e(list(five), list(six))
    nine = find_9(e, dig_one_seg_miss)

    numbers_map[''.join(sorted(nine))] = 9

    zero = find_0(nine, six, dig_one_seg_miss)
    numbers_map[''.join(sorted(zero))] = 0

    d = find_missing_segs(list(zero))[0]

    two, three = find_3_2(five, dig_two_seg_missing)
    numbers_map[''.join(sorted(two))] = 2
    numbers_map[''.join(sorted(three))] = 3
    

def identify_digits(inp_list):
    
    digits_missing_one_seg = []
    digits_missing_two_seg = []
    one = ''
    numbers_map = {}

    for digit in inp_list:
        if len(digit) == 6:
            digits_missing_one_seg.append(digit)
        if len(digit) == 5:
            digits_missing_two_seg.append(digit)
        if len(digit) == 2:
            one = digit
            numbers_map[''.join(sorted(digit))] = 1
        if len(digit) == 3:
            numbers_map[''.join(sorted(digit))] = 7
        if len(digit) == 4:
            numbers_map[''.join(sorted(digit))] = 4
        if len(digit) == 7:
            numbers_map[''.join(sorted(digit))] = 8

    find_numbers(digits_missing_one_seg, one, digits_missing_two_seg, numbers_map)
    return numbers_map

    
def part2(inp):
    grand_total = 0
    for line in inp:
        random_digits = line[0]
        numbers_map = identify_digits(random_digits)
        p2 = line[1]

        grand_total += 1000 * numbers_map[''.join(sorted(p2[0]))] + 100 * numbers_map[''.join(sorted(p2[1]))] + 10 * numbers_map[''.join(sorted(p2[2]))] + numbers_map[''.join(sorted(p2[3]))]

    print(f'Solution part 2: {grand_total}')


def main():
    src_dir = pathlib.Path(__file__).parent
    with open(src_dir / 'input.txt', 'r') as file:
        inp = [line.strip('\n').split('|') for line in file.read().splitlines()]

        input_list = []
        for elt in inp:
            cur_line = [elt[0].split(), elt[1].split()]
            input_list.append(cur_line)
        
        part1(input_list)
        part2(input_list)
        
        

if __name__ == '__main__':
    main()


