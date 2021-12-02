#!/usr/bin/env python3

import pathlib

def part2(commands):
    x = 0
    z = 0
    aim = 0
    for command in commands:
        dir_step = command.split(' ')
        if dir_step[0] == 'forward':
            x += int(dir_step[1])
            z += aim * int(dir_step[1])
        if dir_step[0] == 'up':
            aim -= int(dir_step[1])
        if dir_step[0] == 'down':
            aim += int(dir_step[1])
    return x,z

def part1(commands):
    x = 0
    z = 0
    for command in commands:
        dir_step = command.split(' ')
        if dir_step[0] == 'forward':
            x+=int(dir_step[1])
        if dir_step[0] == 'up':
            z-=int(dir_step[1])
        if dir_step[0] == 'down':
            z+=int(dir_step[1])
    return x,z

def main():
    src_dir = pathlib.Path(__file__).parent
    with open(src_dir / 'input.txt', 'r') as file:
        commands = file.read().splitlines()
        x,z = part1(commands)
        print(f'Result part 1 : {x*z}')

        x,z = part2(commands)
        print(f'Result part 2 : {x*z}')


if __name__ == '__main__':
    main()
    


