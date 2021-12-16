import numpy as np

def parse_data(data):
    instr = np.empty((len(data), 4)).astype('int')
    for i, dx in enumerate(data):
        d1, d2 = dx.split('->')
        instr[i] = np.array([int(d) for d in d1.split(',')] + [int(d) for d in d2.split(',')])
        
    return instr

def get_path(v1, v2):
    if v2 > v1:
        return [*range(v1, v2 + 1, 1)]
    elif v1 > v2:
        return [*range(v1, v2 - 1, -1)]
    else:
        return None
    
def add_coords(grid, coords):
    for (x, y) in coords:
        grid[x][y] += 1
    return grid

def solution(instr, diagonal = False):
    # initialize grid
    grid = np.zeros((instr.max() + 1, instr.max() + 1))
    for (x1, y1, x2, y2) in instr:

        dist_x = abs(x1 - x2)
        dist_y = abs(y1 - y2)

        # diagonal
        if dist_x == dist_y and diagonal:
            px = get_path(x1, x2)
            py = get_path(y1, y2)

            coords = list(zip(py, px))
            grid = add_coords(grid, coords)

        elif dist_y == 0:
            px = get_path(x1, x2)
            coords = list(zip((dist_x + 1) * [y1], px))
            grid = add_coords(grid, coords)
        elif dist_x == 0:
            py = get_path(y1, y2)
            coords = list(zip(py, (dist_y + 1) * [x1]))
            grid = add_coords(grid, coords)
        else:
            pass
        
    return len(grid[grid >= 2])

def test_one():
    with open('test_input.txt', 'r') as f:
        data = f.read().splitlines()

    instr = parse_data(data)
    
    assert solution(instr, diagonal = False) == 5
    
def test_two():
    with open('test_input.txt', 'r') as f:
        data = f.read().splitlines()

    instr = parse_data(data)
    
    assert solution(instr, diagonal = True) == 12

if __name__ == '__main__':
    test_one()
    test_two()
    
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        
    instr = parse_data(data)

    # part 1
    print(solution(instr, diagonal = False))
    
    # part 2
    print(solution(instr, diagonal = True))