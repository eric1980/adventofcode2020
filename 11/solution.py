from copy import deepcopy


def run_iteration(seats):
    new_seat_map = deepcopy(seats)
    has_changed = False

    for row in range(1, len(seats)-1):
        for col in range(1, len(seats[0])-1):

            occupied = adjacent_occupied(seats, row, col)

            if seats[row][col] == 'L' and occupied == 0:
                new_seat_map[row][col] = '#'
                has_changed = True
            elif seats[row][col] == '#' and occupied >= 4:
                new_seat_map[row][col] = 'L'
                has_changed = True

    return has_changed, new_seat_map


def adjacent_occupied(seats, row, col):
    return seats[row-1][col-1:col+2].count('#') + \
           (seats[row][col-1] + seats[row][col+1]).count('#') + \
           seats[row+1][col-1:col+2].count('#')


def find_solution_one(seats):
    has_changed = True
    while has_changed:
        has_changed, seats = run_iteration(seats)

    return sum([row.count('#') for row in seats])


def print_seat_map(seats):
    for row in seats:
        print(''.join(row))


def main():
    seats = [list('.' + value.strip() + '.') for value in open('input.txt', 'r').readlines()]
    seats.insert(0, '.'*len(seats[0]))
    seats.append('.'*len(seats[0]))

    test_data = [
        list('............'),
        list('.L.LL.LL.LL.'),
        list('.LLLLLLL.LL.'),
        list('.L.L.L..L...'),
        list('.LLLL.LL.LL.'),
        list('.L.LL.LL.LL.'),
        list('.L.LLLLL.LL.'),
        list('...L.L......'),
        list('.LLLLLLLLLL.'),
        list('.L.LLLLLL.L.'),
        list('.L.LLLLL.LL.'),
        list('............')
    ]

    test_result = find_solution_one(test_data)
    # solution_one = find_solution_one(seats)

    print(f'Test result: {test_result}')
    # print(f'Solution 1: {solution_one}')
    # print(f'Solution 2: {}')


if __name__ == "__main__":
    main()
