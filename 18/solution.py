from collections import deque


def evaluate_line(expression, version):
    return evaluate_postfix(infix_to_postfix(expression, version))


def infix_to_postfix(infix, version):
    postfix = []
    stack = deque()
    precedence = {'+': 0 if version == 1 else 1, '*': 0, '(': -1}

    for item in list(infix.replace(" ", "")):
        if item == '(':
            stack.append(item)
        elif item == ')':
            while len(stack) > 0 and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif item in '+*':
            if len(stack) > 0 and precedence[stack[-1]] >= precedence[item]:
                postfix.append(stack.pop())
            stack.append(item)
        else:
            postfix.append(int(item))

    while len(stack) != 0:
        postfix.append(stack.pop())

    return postfix


def evaluate_postfix(postfix):
    stack = deque()
    for item in postfix:
        if item == '+':
            stack.append(stack.pop() + stack.pop())
        elif item == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(item)

    return stack.pop()


def main():
    data = open('input.txt', 'r').read().strip().split('\n')

    test_data_1 = [
        ('2 * 3 + (4 * 5)', 26),
        ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
        ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
        ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632)
    ]

    test_data_2 = [
        ('1 + (2 * 3) + (4 * (5 + 6))', 51),
        ('2 * 3 + (4 * 5)', 46),
        ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
        ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
        ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340)
    ]

    for expression, result in test_data_1:
        test_result = evaluate_line(expression, 1)
        print(f'Test result: {expression} = {test_result}')
        assert test_result == result, f'Test does not pass. Expected {result}, was {test_result}'

    solution_one = sum([evaluate_line(line, 1) for line in data])
    print(f'Solution 1: {solution_one}\n')

    for expression, result in test_data_2:
        test_result = evaluate_line(expression, 2)
        print(f'Test result: {expression} = {test_result}')
        assert test_result == result, f'Test does not pass. Expected {result}, was {test_result}'

    solution_two = sum([evaluate_line(line, 2) for line in data])
    print(f'Solution 2: {solution_two}\n')


if __name__ == "__main__":
    main()
