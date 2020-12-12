from math import fmod

DIRECTIONS = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}

MOVEMENT = {'x': {'N': 0, 'S':  0, 'E': 1, 'W': -1},
            'y': {'N': 1, 'S': -1, 'E': 0, 'W':  0}}

def execute_command(position, command):
    instruction = command[:1]
    amount = int(command[1:])
    if instruction in 'NSEWF':
        instr = DIRECTIONS[position['direction']] if instruction == 'F' else instruction
        position['x'] += amount * MOVEMENT['x'][instr]
        position['y'] += amount * MOVEMENT['y'][instr]
    else:
        position['direction'] = (position['direction'] + amount * (-1 if instruction == 'R' else 1)) % 360


def find_solution_one(data):
    position = {'x': 0, 'y': 0, 'direction': 0}

    for command in data:
        execute_command(position, command)

    return abs(position['x']) + abs(position['y'])


def main():
    data = [value.strip() for value in open('input.txt', 'r').readlines()]
    test_data = ['F10', 'N3', 'F7', 'R90', 'F11']

    test_result = find_solution_one(test_data)
    print(f'Test result : {test_result}')
    assert test_result == 25, 'Test does not pass'

    solution_one = find_solution_one(data)
    solution_two = 0

    print(f'Solution 1: {solution_one}')
    print(f'Solution 2: {solution_two}')


if __name__ == "__main__":
    main()
