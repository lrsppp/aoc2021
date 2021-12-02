def test_one():
    test_data = [
        'forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2',
    ]   
    
    assert one(test_data) == 150
    
def test_two():
    data = [
        'forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2',
    ]

    assert two(data) == 900


def one(data):
    h, d = 0, 0
    for i in range(len(data)):
        cmd, val = data[i].split(' ')
        val = int(val)
        
        if cmd == 'forward':
            h += val
        elif cmd == 'down':
            d += val
        elif cmd == 'up':
            d -= val
        else:
            pass

    return h * d

def two(data):
    h, d, aim = 0, 0, 0
    for i in range(len(data)):
        cmd, val = data[i].split(' ')
        val = int(val)

        if cmd == 'forward':
            if aim != 0:
                d += val * aim

            h += val

        elif cmd == 'down':
            aim += val

        elif cmd == 'up':
            aim -= val
        else:
            pass
        
    return h * d

if __name__ == '__main__':
    data = open('input.txt', 'r').read().splitlines()
    test_one()
    test_two()
    print(one(data))
    print(two(data))