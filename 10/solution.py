
def find_solution_one(data):
    adapters = [0, *data, max(data) + 3]
    jolt_diff = [j - i for i, j in zip(adapters[:-1], adapters[1:])]

    return jolt_diff.count(1) * jolt_diff.count(3)


def main():
    data = [int(x) for x in open('input.txt', 'r').readlines()]
    data.sort()

    solution_one = find_solution_one(data)

    print(f'Solution 1: {solution_one}')
    # print(f'Solution 2: {}')


if __name__ == "__main__":
    main()
