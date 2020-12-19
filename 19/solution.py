def find_solution_1(data):
    return 0


def main():
    data = open('input.txt', 'r').read().strip().split('\n')
    test_data = open('example.txt', 'r').read().strip().split('\n')

    test_result = find_solution_1(test_data)
    print(f'Test result: {test_result}')

    solution_one = find_solution_1(data)
    print(f'Solution 1: {solution_one}\n')


if __name__ == "__main__":
    main()
