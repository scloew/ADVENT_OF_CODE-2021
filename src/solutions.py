from src.utils import day_3b_util


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


def day_3a():
    gam, ep = '', ''
    data = get_input('3a')
    for i in range(len(data[0]) - 1):
        ones, zeros = 0, 0
        for bin_num in data:
            ones, zeros = (ones + 1, zeros) if bin_num[i] == '1' else (ones, zeros + 1)
        gam += '1' if zeros < ones else '0'
        ep += '0' if zeros < ones else '1'
    return int(gam, 2) * int(ep, 2)


def day_3b():
    data = get_input('3a')
    ox_rating = day_3b_util(data, True)
    scrubber = day_3b_util(data, False)
    return int(ox_rating, 2) * int(scrubber, 2)


def get_input(day, type_=None):
    f_name = f'..\\inputs\\day_{day}.txt'
    with open(f_name) as f:
        if type_ is None:
            print('tick')
            return f.readlines()
        else:
            return tuple(type_(i) for i in f.readlines())


solution = day_3b()
print(f'solution:={solution}')
