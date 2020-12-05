def get_seat(code):
    row = list(range(0, 128))
    col = list(range(0, 8))

    for direction in code[:7]:
        row = row[:len(row)//2] if direction == 'F' else row[len(row)//2:]

    for direction in code[7:]:
        col = col[:len(col)//2] if direction == 'L' else col[len(col)//2:]

    return {'row': row[0], 'col': col[0], 'id': row[0] * 8 + col[0]}


def main():
    data = open('input.txt', 'r').readlines()

    seats = [get_seat(code) for code in data]
    ids = [seat['id'] for seat in seats]
    my_seat = set(range(min(ids), max(ids))) - set(ids)

    print(f'Solution 1: {max(ids)}')
    print(f'Solution 2: {next(iter(my_seat))}')


if __name__ == "__main__":
    main()
