def main():
    data = open('input.txt', 'r').read().strip()

    all_yes = sum([len(yes) for yes in [set(group.replace('\n', '')) for group in data.split('\n\n')]])

    common_yes = 0
    for group in [group.split('\n') for group in data.split('\n\n')]:
        common_yes += (len(set.intersection(*[set(person) for person in group])))

    print(f'Solution 1: {all_yes}')
    print(f'Solution 2: {common_yes}')


if __name__ == "__main__":
    main()
