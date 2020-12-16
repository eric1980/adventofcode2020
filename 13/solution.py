from math import prod


def find_solution_one(earliest_time, bus_ids):
    bus_departures = dict([((earliest_time // int(bus_id) + 1) * int(bus_id), int(bus_id)) for bus_id in bus_ids if bus_id != 'x'])

    best_time = min([key for key in bus_departures])
    best_bus = bus_departures[best_time]

    return best_bus * (best_time - earliest_time)


def find_solution_two(bus_ids):
    rests = [(int(v) - i) % int(v) for i, v in enumerate(bus_ids) if v != 'x']
    mods = [int(bus_id) for bus_id in bus_ids if bus_id != 'x']
    terms = [prod(mods) // bus_id for bus_id in mods]

    for i, term in enumerate(terms):
        multiplier = 1
        while (term * multiplier) % mods[i] != rests[i]:
            multiplier += 1
        terms[i] = term * multiplier

    return sum(terms) % prod(mods)


def main():
    with open('input.txt', 'r') as input_file:
        earliest_time = int(input_file.readline())
        bus_ids = [id for id in input_file.readline().split(',')]

    test_earliest_time = 939
    test_bus_ids = ['7', '13', 'x', 'x', '59', 'x', '31', '19']

    test_result_one = find_solution_one(test_earliest_time, test_bus_ids)
    test_result_two = find_solution_two(test_bus_ids)

    print(f'Test result 1: {test_result_one}')
    print(f'Test result 2: {test_result_two}')

    assert test_result_one == 295, 'Test 1 does not pass'
    assert test_result_two == 1068781, 'Test 2 does not pass'

    solution_one = find_solution_one(earliest_time, bus_ids)
    solution_two = find_solution_two(bus_ids)

    print(f'Solution 1: {solution_one}')
    print(f'Solution 2: {solution_two}')


if __name__ == "__main__":
    main()
