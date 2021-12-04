def day_1a():
    data = get_input('1a', int)
    return sum(1 for i, v in enumerate(data) if i and data[i - 1] < v)


def day_1b():
    data = get_input('1a', int)
    data = (sum(data[i:i + 3]) for i in range(0, len(data)))
    return sum(1 for i, v in enumerate(data) if i and data[i - 1] < v)


def day_2a():
    depth, hor = 0, 0
    data = get_input('2a')
    for entry in data:
        direction, val = entry.split(' ')
        val = int(val)
        if direction == 'forward':
            hor += val
        else:
            depth += val if direction == 'down' else -val
    return depth * hor


def day_2b():
    aim, depth, hor = 0, 0, 0
    data = get_input('2a')
    for entry in data:
        direction, val = entry.split(' ')
        val = int(val)
        if direction == 'forward':
            hor += val
            depth += aim * val
        else:
            aim += val if direction == 'down' else -val
    return depth * hor


def get_input(day, type_=None):
    f_name = f'..\\inputs\\day_{day}.txt'
    with open(f_name) as f:
        if type_ is None:
            print('tick')
            return f.readlines()
        else:
            return tuple(type_(i) for i in f.readlines())


solution = day_2b()
print(f'solution:={solution}')
