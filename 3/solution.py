from math import prod

def count_slope(lines, slope):
    position = {'row': 0, 'col': 0}
    trees_encountered = 0

    while position['row'] < len(lines):
        if lines[position['row']][position['col']] == '#':
            trees_encountered += 1

        position = {'row':(position['row'] + slope[1]),
                    'col': (position['col'] + slope[0]) % len(lines[position['row']].strip())}

    return trees_encountered


def find_solution_one(lines):
    print(f'Solution 1: {count_slope(lines, (3, 1))}')


def find_solution_two(lines):
    trees = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    
    for slope in slopes:
        trees.append(count_slope(lines, slope))

    print(f'Solution 2: {prod(trees)}')


def main():
    lines = open('input.txt', 'r').readlines()

    find_solution_one(lines)
    find_solution_two(lines)


if __name__ == "__main__":
    main()
