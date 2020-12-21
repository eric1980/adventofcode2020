
def match_rule(rules, rule_name, message):

    rule_sets = rules[rule_name]
    if rule_sets[0][0] in 'ab':
        if message[:1] == rule_sets[0][0]:
            return True, message[1:]
        else:
            return False, message

    for rule_set in rule_sets:
        set_ok = True
        rest = message
        for rule in rule_set:
            is_match, rest = match_rule(rules, rule, rest)
            if not is_match:
                set_ok = False
        if set_ok:
            return True, rest

    return False, message


def find_solution_1(data):
    rule_data, messages = data.replace('"', '').split('\n\n')
    messages = messages.split('\n')

    rules = {}
    for rule in rule_data.split('\n'):
        name, definition = rule.split(':')
        definition = [r.strip().split(' ') for r in definition.split('|')]
        rules[name] = definition

    count = 0
    for message in messages:
        is_match, rest = match_rule(rules, '0', message)
        if is_match and len(rest) == 0:
            count += 1

    return count


def modify_rules(rules):
    rules = rules.replace('8: 42\n', '8: 42 | 42 8\n')
    rules = rules.replace('11: 42 31\n', '11: 42 31 | 42 11 31\n')
    return rules


def main():
    data = open('input.txt', 'r').read().strip()
    test_data_1 = open('example1.txt', 'r').read().strip()
    test_data_2 = open('example2.txt', 'r').read().strip()

    test_result = find_solution_1(test_data_1)
    print(f'Test result: {test_result}')
    assert test_result == 2

    test_result = find_solution_1(test_data_2)
    print(f'Test result: {test_result}')
    assert test_result == 3

    solution_one = find_solution_1(data)
    print(f'Solution 1: {solution_one}\n')

    data = modify_rules(data)
    test_data_2 = modify_rules(test_data_2)

    # test_result = find_solution_1(test_data_2)
    # print(f'Test result: {test_result}')
    # assert test_result == 12


if __name__ == "__main__":
    main()
