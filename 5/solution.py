
def get_seat(code):
    row = list(range(0, 128))
    col = list(range(0, 8))

    for direction in code[:7]:
        row = row[:len(row)//2] if direction == 'F' else row[len(row)//2:]

    for direction in code[7:]:
        col = col[:len(col)//2] if direction == 'L' else col[len(col)//2:]

    return {'row': row[0], 'col': col[0], 'id': row[0] * 8 + col[0]}


def find_my_seat(seats):
    ids = [id['id'] for id in seats]
    ids.sort()

    for i in range(1, len(ids)):
        if ids[i] != ids[i-1] + 1:
            my_id = ids[i-1] + 1
            break

    return my_id


def main():
    data = open('input.txt', 'r').readlines()

    seats = [get_seat(code) for code in data]
    highest_id = max([id['id'] for id in seats])
    my_seat = find_my_seat(seats)

    print(f'Solution 1: {highest_id}')
    print(f'Solution 2: {my_seat}')


if __name__ == "__main__":
    main()
