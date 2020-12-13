def find_solution_one(earliest_time, bus_ids):
    bus_departures = dict([((earliest_time // bus_id + 1) * bus_id, bus_id) for bus_id in bus_ids])

    best_time = min([key for key in bus_departures])
    best_bus = bus_departures[best_time]

    return best_bus * (best_time - earliest_time)


def main():
    with open('input.txt', 'r') as input_file:
        earliest_time = int(input_file.readline())
        bus_ids = [int(id) for id in input_file.readline().split(',') if id != 'x']

    test_earliest_time = 939
    test_bus_ids = [7, 13, 59, 31, 19]

    test_result_one = find_solution_one(test_earliest_time, test_bus_ids)
    # test_result_two = find_solution_two(data)

    print(f'Test result 1: {test_result_one}')
    # print(f'Test result 2: {test_result_two}')

    assert test_result_one == 295, 'Test 1 does not pass'
    # assert test_result_two == 26, 'Test 2 does not pass'

    solution_one = find_solution_one(earliest_time, bus_ids)
    # solution_two = find_solution_two(data)

    print(f'Solution 1: {solution_one}')
    # print(f'Solution 2: {solution_two}')


if __name__ == "__main__":
    main()
