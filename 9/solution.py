from itertools import combinations


def is_valid(data, number, preamble_size):
    return data[number] in [sum(pair) for pair in combinations(data[number - preamble_size:number], 2)]


def find_first_invalid(data, preamble_size=25):
    for i in range(1 + preamble_size, len(data)):
        if not is_valid(data, i, preamble_size):
            break

    return data[i]


def find_sum(data, number):
    for i in range(len(data)):
        value = data[i]
        for j in range(i + 1, len(data)):
            value += data[j]
            if value > number:
                continue
            if value == number:
                return min(data[i:j + 1]) + max(data[i:j + 1])


def main():
    data = [int(x) for x in open('input.txt', 'r').readlines()]

    first_invalid = find_first_invalid(data)
    the_sum = find_sum(data, first_invalid)

    print(f'Solution 1: {first_invalid}')
    print(f'Solution 2: {the_sum}')


if __name__ == "__main__":
    main()
