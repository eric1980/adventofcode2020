import re

def main():
    with open('input.txt', 'r') as input_file:
        values = input_file.readlines()

    correct_passwords = 0

    for value in values:
        parts = re.findall(r"[\w']+", value)
        data = {'low': int(parts[0]), 'high': int(parts[1]), 'char': parts[2], 'password': parts[3]}
        char_count = data['password'].count(data['char'])
        if char_count >= data['low'] and char_count <= data['high']:
            correct_passwords += 1

    print(f'Solution 1: {correct_passwords}')


if __name__ == "__main__":
    main()
