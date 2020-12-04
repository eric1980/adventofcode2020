import re


def parse_passports(data):
    passports = []

    for passport in data.split('\n\n'):
        passports.append(create_passport(re.findall(r'\S+:\S+', passport)))

    return passports


def create_passport(values):
    password = {}
    for value in values:
        password[value.split(':')[0]] = value.split(':')[1]
    return password


def has_reqiured_fields(passport):
    return all(key in passport for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


def has_correct_data(passport):
    return is_within_years(passport['byr'], 1920, 2002) and \
           is_within_years(passport['iyr'], 2010, 2020) and \
           is_within_years(passport['eyr'], 2020, 2030) and \
           is_height(passport['hgt']) and \
           is_hair_color(passport['hcl']) and \
           is_eye_color(passport['ecl']) and \
           is_pid(passport['pid'])


def is_within_years(value, min_year, max_year):
    return min_year <= int(value) <= max_year


def is_height(value):
    if value[-2:] == 'cm':
        return 150 <= int(value[:-2]) <= 193
    elif value[-2:] == 'in':
        return 59 <= int(value[:-2]) <= 76
    else:
        return False


def is_hair_color(value):
    return re.search(r'^#(?:[0-9a-fA-F]{6})$', value)


def is_eye_color(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_pid(value):
    return re.search(r'^(?:[0-9]{9})$', value)


def main():
    data = open('input.txt', 'r').read()

    passports_all = parse_passports(data)
    passports_fields_ok = list(filter(has_reqiured_fields, passports_all))
    passports_data_ok = list(filter(has_correct_data, passports_fields_ok))

    print(f'Solution 1: {len(passports_fields_ok)}')
    print(f'Solution 2: {len(passports_data_ok)}')


if __name__ == "__main__":
    main()
