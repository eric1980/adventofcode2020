from collections import defaultdict


def get_spoken_number(data, number):
    memory = defaultdict(lambda: (0, True))
    memory.update(zip(data, [i + 1 for i in range(len(data))]))

    for i in range(len(data), number):
        value = data[-1]
        data.append(0 if not value in memory else i - memory[value])
        memory[value] = i

    return data[-1]


def main():
    data = [int(i) for i in open('input.txt', 'r').readline().split(',')]

    test_data = [[0, 3, 6], [1, 3, 2], [2, 1, 3], [1, 2, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    test_result = [436, 1, 10, 27, 78, 438, 1836]

    for numbers, result in zip(test_data, test_result):
        print(f'Check {numbers} -> {result}')
        assert get_spoken_number(numbers, 2020) == result


    print(f'Solution 1: {get_spoken_number(data, 2020)}')
    print(f'Solution 2: {get_spoken_number(data, 30000000)}')


if __name__ == "__main__":
    main()
