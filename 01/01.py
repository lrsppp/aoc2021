import numpy as np

def one(data):
    n = len(data)
    count = 0
    for i in range(n - 1):
        if data[i+1] > data[i]:
            count += 1

    return count

def two(data):
    data_roll = np.roll(data, -1) + np.roll(data, -2) + data
    return one(data_roll)

def test():
    data_test = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263
    ]
    
    assert one(data_test) == 7
    assert two(data_test) == 5

if __name__ == '__main__':
    
    # read, parse
    data = open('input.txt', 'r').readlines()
    data = np.array([int(d.strip()) for d in data])
    
    # result
    test()
    print(one(data))
    print(two(data))
