from collections import defaultdict
from copy import deepcopy


class PocketDimension():
    def __init__(self, initialisation, margin=10, use_forth_dimension=False):
        self.use_dimension = use_forth_dimension
        self.number_of_dimensions = 1 if not self.use_dimension else margin * 2 + 1

        self.dimension = [[[list([0] * (len(initialisation[0]) + margin * 2))
            for i in range((len(initialisation) + margin * 2))]
            for i in range(margin*2+1)]
            for i in range(self.number_of_dimensions)]

        self.origo = {'x': len(self.dimension[0][0][0]) // 2, 'y': len(self.dimension[0][0]) // 2,
                      'z': len(self.dimension[0]) // 2, 'w': len(self.dimension) // 2}

        plane_x = self.origo['x'] - len(initialisation[0]) // 2
        plane_y = self.origo['y'] - len(initialisation) // 2

        for y, row in enumerate(initialisation):
            for x, cell in enumerate(row):
                self.dimension[self.origo['w']][self.origo['z']][y + plane_y][x + plane_x] = cell

    def cycle(self):
        new_dimension = deepcopy(self.dimension)

        for w in range(1, len(self.dimension)) if self.use_dimension else [0]:
            for z in range(1, len(self.dimension[0])):
                for y in range(1, len(self.dimension[0][0])):
                    for x in range(1, len(self.dimension[0][0][0])):
                        active_cells = self.get_active_surrounding(x, y, z, w)
                        if new_dimension[w][z][y][x] == 1 and active_cells not in (3, 4):
                            new_dimension[w][z][y][x] = 0
                        elif new_dimension[w][z][y][x] == 0 and active_cells == 3:
                            new_dimension[w][z][y][x] = 1

        self.dimension = deepcopy(new_dimension)

    def get_active_surrounding(self, x, y, z, w):
        active = 0
        for dimension in self.dimension[w-1:w+2] if self.use_dimension else self.dimension:
            for plane in dimension[z-1:z+2]:
                for row in plane[y-1:y+2]:
                    active += row[x-1:x+2].count(1)

        return active

    def count_active_cubes(self):
        active = 0
        for dimension in self.dimension:
            for plane in dimension:
                active += sum([row.count(1) for row in plane])

        return active


def get_active_cubes(data, iterations, use_forth_dimension=False):
    pocket_dimension = PocketDimension(data, use_forth_dimension=use_forth_dimension)

    for _ in range(iterations):
        pocket_dimension.cycle()

    return pocket_dimension.count_active_cubes()


def main():
    data = open('input.txt', 'r').read().strip().split('\n')
    for i, row in enumerate(data):
        data[i] = [1 if v == '#' else 0 for _, v in enumerate(list(row))]

    test_data = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]

    test_result_one = get_active_cubes(test_data, 6)
    print(f'Test result 1: {test_result_one}')
    assert test_result_one == 112, 'Test 1 does not pass'

    test_result_two = get_active_cubes(test_data, 6, use_forth_dimension=True)
    print(f'Test result 2: {test_result_two}')
    assert test_result_two == 848, 'Test 2 does not pass'

    solution_one = get_active_cubes(data, 6)
    print(f'Solution 1: {solution_one}')

    solution_two = get_active_cubes(data, 6, use_forth_dimension=True)
    print(f'Solution 2: {solution_two}')


if __name__ == "__main__":
    main()
