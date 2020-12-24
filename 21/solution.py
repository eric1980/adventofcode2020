from collections import defaultdict


def reduce_dict(the_dict):
    not_done = True
    while not_done:
        not_done = False
        for ingr, value in the_dict.items():
            if len(value) == 1:
                for i in the_dict:
                    if i != ingr and value.issubset(the_dict[i]):
                        not_done = True
                        the_dict[i].difference_update(value)


def find_solution_1(data):
    dishes, _, _, _, non_allergene_ingrediences = parse_data(data)

    count = 0
    for dish in dishes:
        for ingredience in dish['ingrediences']:
            if ingredience in non_allergene_ingrediences:
                count += 1

    return count


def find_solution_2(data):
    _, _, _, allergene_ingrediences, _ = parse_data(data)

    ingredience_list = []
    for key in sorted(allergene_ingrediences.keys()):
        ingredience_list.append(list(allergene_ingrediences[key])[0])

    return ','.join(ingredience_list)


def parse_data(data):
    dishes = []  # List of all parsed dishes
    a_list = []  # List of allergenes and all possible ingrediences

    for dish in data:
        ingrediences, allergenes = dish.split('(contains')
        ingrediences = set(ingrediences.strip().split(' '))
        allergenes = set(allergenes.strip()[:-1].split(', '))
        dishes.append({'allergenes': allergenes, 'ingrediences': ingrediences})
        for allergene in allergenes:
            a_list.append({'allergene': allergene, 'ingrediences': ingrediences})

    ingrediences = set.union(*[dish['ingrediences'] for dish in dishes])
    allergenes = set([dish['allergene'] for dish in a_list])

    allergene_ingrediences = {}
    for allergene in allergenes:
        allergene_ingrediences[allergene] = set.intersection(*[set(d['ingrediences']) for d in a_list if d['allergene'] == allergene])

    reduce_dict(allergene_ingrediences)
    non_allergene_ingrediences = set.difference(ingrediences, *[set(v) for _, v in allergene_ingrediences.items()])

    return dishes, allergenes, ingrediences, allergene_ingrediences, non_allergene_ingrediences


def main():
    data = open('input.txt', 'r').readlines()
    test_data = open('example.txt', 'r').readlines()

    test_result = find_solution_1(test_data)
    print(f'Test result 1: {test_result}')
    assert test_result == 5

    solution_one = find_solution_1(data)
    print(f'Solution 1: {solution_one}\n')

    test_result = find_solution_2(test_data)
    print(f'Test result 2: {test_result}')
    assert test_result == 'mxmxvkd,sqjhc,fvjkl'

    solution_two = find_solution_2(data)
    print(f'Solution 2: {solution_two}\n')

if __name__ == "__main__":
    main()
