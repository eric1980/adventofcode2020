# Find the two values where x + y = 2020, and provide x * y.
# Find the three values where x + y + z = 2020, and provide x * y * z.
import itertools


def main():
    with open('input.txt', 'r') as input_file:
        values = input_file.readlines()
        values = [int(value) for value in values]

    for item in itertools.combinations(values, 2):
        if sum(item) == 2020:
            print(f'Solution 1: {item[0] * item[1]} {item}')

    for item in itertools.combinations(values, 3):
        if sum(item) == 2020:
            print(f'Solution 2: {item[0] * item[1] * item[2]} {item}')


if __name__ == "__main__":
    main()
