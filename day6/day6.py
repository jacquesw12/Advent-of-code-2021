import pathlib


def iterate_one_day_p1(fish):
    fish_next_it = []
    amount_new_fish = fish.count(0)
    for f in fish:
        next_f = 0
        if f == 0:
            next_f = 6
        else:
            next_f = f-1
        fish_next_it.append(next_f)
    fish_next_it.extend([8] * amount_new_fish)
    return fish_next_it


def iterate_one_day_p2(fish):
    fish_next_it = []
    amount_new_fish = fish.count(0)
    for f in fish:
        next_f = 0
        if f == 0:
            next_f = 6
        else:
            next_f = f-1
        fish_next_it.append(next_f)
    fish_next_it.extend([8] * amount_new_fish)
    return fish_next_it

def update_age(ages):
    amount_new_fish = ages[0]
    for i in range(len(ages)-1):
        ages[i] = ages[i+1]
    ages[6] += amount_new_fish
    ages[8] = amount_new_fish 

def main():
    src_dir = pathlib.Path(__file__).parent
    with open(src_dir / 'input.txt', 'r') as file:
        fish = [int(elt) for elt in file.readline().strip('\n').split(',')]
        #fish = [0]
        fish_part1 = fish
        for i in range(80):
            fish_part1 = iterate_one_day_p1(fish_part1)

        ages = [0] * 9
        for i in range(len(ages)):
            ages[i] = fish.count(i)

        for i in range(256):
            update_age(ages)

        print(f'Amount fish part 2 {sum(ages)}')
            


        


if __name__ == '__main__':
    main()
