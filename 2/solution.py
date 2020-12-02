import re


def find_solution_one(passwords):
    correct_passwords = 0

    for password in passwords:
        char_count = password['password'].count(password['char'])
        if password['low'] <= char_count <= password['high']:
            correct_passwords += 1

    print(f'Solution 1: {correct_passwords}')


def find_solution_two(passwords):
    correct_passwords = 0

    for password in passwords:
        req_one = password['password'][password['low']-1] == password['char']
        req_two = password['password'][password['high']-1] == password['char']
        if req_one != req_two:
            correct_passwords += 1

    print(f'Solution 2: {correct_passwords}')


def main():
    lines = open('input.txt', 'r').readlines()

    passwords = []

    for line in lines:
        parts = re.findall(r"[\w']+", line)
        passwords.append({'low': int(parts[0]), 'high': int(parts[1]), 'char': parts[2], 'password': parts[3]})

    find_solution_one(passwords)
    find_solution_two(passwords)


if __name__ == "__main__":
    main()
