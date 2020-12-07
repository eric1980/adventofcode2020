import re


def create_bags(definitions):
    bags = {}
    for definition in definitions:
        bags[' '.join(definition.split()[:2])] = \
            [{'count': int(d.split()[0]), 'name': ' '.join(d.split()[1:])} for d in re.findall(r'\d\s\w+\s\w+', definition)]

    return bags


def get_bags_with(bags, name):
    result = []
    for bag, content in bags.items():
        for inner_bag in content:
            if name in inner_bag['name']:
                result.append(bag)
                result.extend(get_bags_with(bags, bag))

    return result


def count_bags_within(bags, name):
    count = 0
    for bag in bags[name]:
        count += bag['count'] + bag['count'] * count_bags_within(bags, bag['name'])

    return count


def main():
    data = open('input.txt', 'r').readlines()

    bag_definitions = create_bags(data)
    bags_with_shiny_gold = len(set(get_bags_with(bag_definitions, 'shiny gold')))
    bags_in_shiny_gold = count_bags_within(bag_definitions, 'shiny gold')

    print(f'Solution 1: {bags_with_shiny_gold}')
    print(f'Solution 2: {bags_in_shiny_gold}')


if __name__ == "__main__":
    main()
