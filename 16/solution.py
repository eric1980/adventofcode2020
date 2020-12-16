import re


def parse_file(filename):
    lines = open(filename, 'r').read()

    fields = {}
    field_data = re.findall(r'(\w+): (\d+)-(\d+) or (\d+)-(\d+)', lines)
    for data in field_data:
        name, low1, high1, low2, high2 = data
        fields[name] = [i for i in range(int(low1), int(high1) + 1)] + [i for i in range(int(low2), int(high2) + 1)]

    tickets = dict(re.findall(r'(.*):\n((?:\d+[,\n]){1,})', lines))
    for key, value in tickets.items():
        tickets[key] = [int(i) for i in re.split(',|\n', value.strip())]

    data = {'fields': fields}
    data.update(tickets)

    return data


def find_solution_one(data):
    valid_fields = data['your ticket']
    for field in data['fields']:
        valid_fields.extend(data['fields'][field])

    invalid_tickets = []
    for ticket in data['nearby tickets']:
        if ticket not in valid_fields:
            invalid_tickets.append(ticket)

    return sum(invalid_tickets)


def main():
    data = parse_file('input.txt')
    test_data = parse_file('example.txt')

    test_result = find_solution_one(test_data)
    print(f'Test result: {test_result}')
    assert test_result == 71

    print(f'Solution 1: {find_solution_one(data)}')


if __name__ == "__main__":
    main()
