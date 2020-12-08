from copy import deepcopy


class CPU:
    def __init__(self, mem):
        self.pc = 0
        self.acc = 0
        self.mem = mem
        self.is_processed = [False for _ in range(len(mem))]
        self.is_ok = True
        self.done = False

        while self.is_ok and not self.done:
            self.__process_next_instruction()

    def __process_next_instruction(self):
        if self.pc >= len(self.mem):
            # Invalid program counter detected
            self.is_ok = False
            return

        if self.is_processed[self.pc]:
            # Infinit loop detected
            self.is_ok = False
            return

        self.is_processed[self.pc] = True
        instruction = self.mem[self.pc][0]
        operand = int(self.mem[self.pc][1])

        if instruction == 'acc':
            self.acc += operand
            self.pc += 1
        elif instruction == 'jmp':
            self.pc += operand
        else:  # nop
            self.pc += 1

        self.done = self.pc >= len(self.mem)


def main():
    instructions = [i.split() for i in open('input.txt', 'r').readlines()]

    cpu1 = CPU(instructions)

    for i in range(len(instructions)):
        mod_instructions = deepcopy(instructions)

        if mod_instructions[i][0] == 'jmp':
            mod_instructions[i][0] = 'nop'
        elif mod_instructions[i][0] == 'nop':
            mod_instructions[i][0] = 'jmp'

        cpu2 = CPU(mod_instructions)

        if cpu2.is_ok:
            break

    print(f'Solution 1: {cpu1.acc} - Infinite loop detected at instruction {cpu1.pc}')
    print(f'Solution 2: {cpu2.acc} - Modified instruction at {i}')


if __name__ == "__main__":
    main()
