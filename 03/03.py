def test_one():
    data = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    
    assert one(data) == 198

def test_two():
    data = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    
    assert two(data) == 230

def one(data):
    datat = list(map(list, zip(*data)))
    n = len(datat[0])
    bg = []
    for row in datat:
        if row.count('1') > int(n / 2):
            bg.append(1)
        else:
            bg.append(0)

    be = [abs(b - 1) for b in bg]

    gamma = int(''.join(list(map(str, bg))), 2)
    epsilon = int(''.join(list(map(str, be))), 2)

    return gamma * epsilon

def search(data, k = 0, oxy = True):
    if len(data) == 1:
        return int(data[0], 2)

    else:
        n = len(data)
        select = []
        datat = list(map(list, zip(*data)))

        col = datat[k]
        if oxy:
            cond = col.count('0') > int(n / 2)
        else:
            cond = col.count('0') <= int(n / 2)
            
        if cond:
            bit = '0'
        else:
            bit = '1'

        for row in data:
            if row[k] == bit:
                select.append(row)

        return search(select, k = k + 1, oxy = oxy)

def two(data):
    oxy = search(data, oxy = True)
    carbon = search(data, oxy = False)
    
    return oxy * carbon

if __name__ == '__main__':
    
    data = open('input.txt', 'r').read().splitlines()

    test_one()
    test_two()
    print(one(data))
    print(two(data))