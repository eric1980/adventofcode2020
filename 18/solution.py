def evaluate_line(expression):
    return 0


def main():
    data = open('input.txt', 'r').read().strip().split('\n')

    test_data = [
        ('2 * 3 + (4 * 5)', 26),
        ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
        ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
        ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632)
    ]

    for expression, result in test_data:
        test_result = evaluate_line(expression)
        print(f'Test result: {expression} = {test_result}')
        assert test_result == result, f'Test 1 does not pass. Expected {result}, was {test_result}'

    solution_one = sum([evaluate_line(line) for line in data])
    print(f'Solution 1: {solution_one}')

    # solution_two = get_active_cubes(data, 6, use_forth_dimension=True)
    # print(f'Solution 2: {solution_two}')


if __name__ == "__main__":
    main()
