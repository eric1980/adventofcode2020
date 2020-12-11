from copy import deepcopy


def run_iteration(seats, check_function, occupied_limit):
    new_seat_map = deepcopy(seats)
    has_changed = False

    for row in range(1, len(seats)-1):
        for col in range(1, len(seats[0])-1):

            occupied = check_function(seats, row, col)

            if seats[row][col] == 'L' and occupied == 0:
                new_seat_map[row][col] = '#'
                has_changed = True
            elif seats[row][col] == '#' and occupied >= occupied_limit:
                new_seat_map[row][col] = 'L'
                has_changed = True

    return has_changed, new_seat_map


def adjacent_occupied(seats, row, col):
    return seats[row-1][col-1:col+2].count('#') + \
           (seats[row][col-1] + seats[row][col+1]).count('#') + \
           seats[row+1][col-1:col+2].count('#')


def visible_occupied(seats, row, col):
    # Dummy
    return 1


def count_stable_seats(seats, check_function, occupied_limit):
    has_changed = True
    while has_changed:
        has_changed, seats = run_iteration(seats, check_function, occupied_limit)

    return sum([row.count('#') for row in seats])


def print_seat_map(seats):
    for row in seats:
        print(''.join(row))


def main():
    # Get data and add 'border'
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

    test_result_one = count_stable_seats(test_data, adjacent_occupied, 4)
    test_result_two = count_stable_seats(test_data, visible_occupied, 5)

    print(f'Test result 1: {test_result_one}')
    print(f'Test result 2: {test_result_two}')

    assert test_result_one == 37, 'Test 1 does not pass'
    assert test_result_two == 26, 'Test 2 does not pass'

    solution_one = count_stable_seats(seats, adjacent_occupied, 4)
    solution_two = count_stable_seats(seats, visible_occupied, 5)

    print(f'Solution 1: {solution_one}')
    print(f'Solution 2: {solution_two}')


if __name__ == "__main__":
    main()
