import numpy as np
from collections import Counter

def find_solution_one(data):
    jolt_diff = Counter(np.diff(data))
    return jolt_diff[1] * jolt_diff[3]


def find_solution_two(data):
    # Find the borders between modifiable chunks
    border_indices = [i+1 for i, value in enumerate(np.diff(data)) if value == 3]
    # Create index tuples for each chunk
    chunk_indices = zip([None] + border_indices, border_indices + [None])
    # Create list of chunks. Chunks with less than 3 numbers are not modifiable
    modifiable_chunks = [chunk for chunk in [data[i:j] for i, j in chunk_indices] if len(chunk) > 2]

    distinct_combinations = 1
    for chunk in modifiable_chunks:
        combinations = list(np.unique(get_valid_combinations(chunk)))
        distinct_combinations *= len(combinations)

    return distinct_combinations


def is_valid(chain):
    jolt_diff = np.diff(chain)
    return max(jolt_diff) <= 3


def get_valid_combinations(chain):
    valid_combinations = []

    if is_valid(chain):
        valid_combinations.append(chain)

        for i in range(1, len(chain) - 1):
            new_chain = chain.copy()
            del new_chain[i]
            valid_combinations.extend(get_valid_combinations(new_chain))

    return valid_combinations


def main():
    data = [int(value) for value in open('input.txt', 'r').readlines()]
    data.sort()
    adapter_chain = [0, *data, max(data) + 3]

    solution_one = find_solution_one(adapter_chain)
    solution_two = find_solution_two(adapter_chain)

    print(f'Solution 1: {solution_one}')
    print(f'Solution 2: {solution_two}')


if __name__ == "__main__":
    main()
