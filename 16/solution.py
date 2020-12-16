import re
from math import prod


def parse_file(filename):
    lines = open(filename, 'r').read()

    fields = {}
    field_data = re.findall(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', lines)
    for data in field_data:
        name, low1, high1, low2, high2 = data
        fields[name] = [i for i in range(int(low1), int(high1) + 1)] + [i for i in range(int(low2), int(high2) + 1)]

    tickets = dict(re.findall(r'(.*):\n((?:\d+[,\n]){1,})', lines))
    for key, value in tickets.items():
        tickets[key] = [[int(j) for j in i.split(',')] for i in value.strip().split('\n')]

    valid_fields = [int(i) for i in list(*tickets['your ticket'])]
    for field in fields:
        valid_fields.extend(fields[field])

    invalid_fields = []
    for i, ticket in reversed(list(enumerate(tickets['nearby tickets']))):
        for value in ticket:
            if value not in valid_fields:
                invalid_fields.append(value)
                del tickets['nearby tickets'][i]

    data = {'fields': fields}
    data.update(tickets)

    return invalid_fields, data


def sort_fields(data):
    tickets = data['your ticket'] + data['nearby tickets']
    field_possibilities = {r: list(range(len(tickets[0]))) for r in data['fields']}

    for field in data['fields']:
        for index in range(len(tickets[0])):
            for ticket in tickets:
                if ticket[index] not in data['fields'][field]:
                    field_possibilities[field].remove(index)
                    break

    done = False
    while not done:
        done = True
        for name, values in field_possibilities.items():
            if len(values) == 1:
                for field in field_possibilities:
                    if field != name:
                        try:
                            field_possibilities[field].remove(values[0])
                            done = False
                        except ValueError:
                            pass

    return field_possibilities


def find_solution_two(data):
    return prod([data['your ticket'][0][value[0]] for f, value in sort_fields(data).items() if 'departure' in f])


def main():
    invalid_fields, data = parse_file('input.txt')
    test_invalid_fields_1, _ = parse_file('example_1.txt')

    test_result_1 = sum(test_invalid_fields_1)
    print(f'Test result 1: {test_result_1}')
    assert test_result_1 == 71

    print(f'Solution 1: {sum(invalid_fields)}')
    print(f'Solution 2: {find_solution_two(data)}')


if __name__ == "__main__":
    main()
