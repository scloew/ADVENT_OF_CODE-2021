def day_1a():
    data = get_input(r'..\inputs\day_1a.txt', int)
    return sum(1 for i, v in enumerate(data) if i and data[i-1] < v)


def day_1b():
    data = get_input(r'..\inputs\day_1a.txt', int)
    data = [sum(data[i:i+3]) for i in range(0, len(data))]
    return sum(1 for i, v in enumerate(data) if i and data[i - 1] < v)


def get_input(f_name, type_=None):
    with open(f_name) as f:
        if not type:
            return f.readlines()
        else:
            return tuple(type_(i) for i in f.readlines())


solution = day_1b()
print(f'solution:={solution}')
