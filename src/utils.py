from operator import lt, ge


def day_3b_util(data, one_tie_breaker):
    compare = ge if one_tie_breaker else lt
    contenders = set(data)
    for i in range(len(data[0]) - 1):
        if len(contenders) == 1:
            return contenders.pop()
        ones, zeros = set(), set()
        for bin_num in contenders:
            if bin_num[i] == '1':
                ones.add(bin_num)
            else:
                zeros.add(bin_num)
        contenders = ones if compare(len(ones), len(zeros)) else zeros
    return max(contenders) if one_tie_breaker else min(contenders)
