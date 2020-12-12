
def main():
    data = [value for value in open('input.txt', 'r').readlines()]
    test_data = ['F10' 'N3', 'F7', 'R90', 'F11']

    test_result = 0
    print(f'Test result : {test_result}')
    assert test_result == 25, 'Test does not pass'

    solution_one = 0
    solution_two = 0

    print(f'Solution 1: {solution_one}')
    print(f'Solution 2: {solution_two}')


if __name__ == "__main__":
    main()
