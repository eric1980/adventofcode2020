DIRECTIONS = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}

MOVEMENT = {'x': {'N': 0, 'S':  0, 'E': 1, 'W': -1},
            'y': {'N': 1, 'S': -1, 'E': 0, 'W':  0}}


def execute_command_ver1(position, command):
    instruction = command[:1]
    amount = int(command[1:])

    if instruction in 'NSEWF':
        instr = DIRECTIONS[position['direction']] if instruction == 'F' else instruction
        position['x'] += amount * MOVEMENT['x'][instr]
        position['y'] += amount * MOVEMENT['y'][instr]
    else:
        position['direction'] = (position['direction'] + amount * (-1 if instruction == 'R' else 1)) % 360


def execute_command_ver2(position, waypoint, command):
    instruction = command[:1]
    amount = int(command[1:])

    if instruction in 'NSEW':
        waypoint['x'] += amount * MOVEMENT['x'][instruction]
        waypoint['y'] += amount * MOVEMENT['y'][instruction]
    elif instruction == 'F':
        position['x'] += amount * waypoint['x']
        position['y'] += amount * waypoint['y']
    else:
        rotation = (amount * (-1 if instruction == 'R' else 1)) % 360
        rotate(waypoint, rotation)


def rotate(point, rotation):
    if rotation == 90:
        tmp = point['x']
        point['x'] = -point['y']
        point['y'] = tmp

    elif rotation == 180:
        point['x'] *= -1
        point['y'] *= -1

    elif rotation == 270:
        tmp = point['x']
        point['x'] = point['y']
        point['y'] = -tmp


def find_solution_one(data):
    position = {'x': 0, 'y': 0, 'direction': 0}

    for command in data:
        execute_command_ver1(position, command)

    return abs(position['x']) + abs(position['y'])


def find_solution_two(data):
    position = {'x':  0, 'y': 0}
    waypoint = {'x': 10, 'y': 1}

    for command in data:
        execute_command_ver2(position, waypoint, command)

    return abs(position['x']) + abs(position['y'])


def main():
    data = [value.strip() for value in open('input.txt', 'r').readlines()]
    test_data = ['F10', 'N3', 'F7', 'R90', 'F11']

    test_result_one = find_solution_one(test_data)
    test_result_two = find_solution_two(test_data)

    print(f'Test result 1: {test_result_one}')
    print(f'Test result 2: {test_result_two}')

    assert test_result_one == 25, 'Test 1 does not pass'
    assert test_result_two == 286, 'Test 2 does not pass'

    solution_one = find_solution_one(data)
    solution_two = find_solution_two(data)

    print(f'Solution 1: {solution_one}')
    print(f'Solution 2: {solution_two}')


if __name__ == "__main__":
    main()
