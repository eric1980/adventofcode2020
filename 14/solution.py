import re


class CPU():
    def __init__(self, data):
        self.bitmask_set = 0
        self.bitmask_clear = 0xFFFFFFFFF
        self.memory = {}
        self.run_instructions(data)

    def run_instructions(self, data):
        for line in data:
            if line[:4] == 'mask':
                self.set_mask(line[7:])
            else:
                address, value = re.findall(r'\[(.*)\] = (.*)', line)[0]
                self.set_memory(int(address), int(value))


class CPU_v1(CPU):
    def set_mask(self, mask):
        self.bitmask_set   =   sum([2**(35-i) for i, e in enumerate(mask) if e == '1'])
        self.bitmask_clear = ~(sum([2**(35-i) for i, e in enumerate(mask) if e == '0']))

    def set_memory(self, address, value):
        self.memory[address] = (value | self.bitmask_set) & self.bitmask_clear


class CPU_v2(CPU):
    def set_mask(self, mask):
        pass

    def set_memory(self, address, value):
        pass


def find_solution(cpu_name, data):
    return sum([value for key, value in cpu_name(data).memory.items()])


def main():
    # Get data and add 'border'
    data = [line.strip() for line in open('input.txt', 'r').readlines()]

    test_data_1 = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 'mem[8] = 11', 'mem[7] = 101', 'mem[8] = 0']
    test_data_2 = ['mask = 000000000000000000000000000000X1001X', 'mem[42] = 100',
                   'mask = 00000000000000000000000000000000X0XX', 'mem[26] = 1']

    test_result = find_solution(CPU_v1, test_data_1)
    print(f'\nTest result 1: {test_result}')
    assert test_result == 165, 'Test 1 does not pass'
    print(f'Solution 1: {find_solution(CPU_v1, data)}')

    # test_result = find_solution(CPU_v2, test_data_2)
    # print(f'\nTest result 2: {test_result}')
    # assert test_result == 208, 'Test 2 does not pass'
    # print(f'Solution 2: {find_solution(CPU_v2, data)}')


if __name__ == "__main__":
    main()
