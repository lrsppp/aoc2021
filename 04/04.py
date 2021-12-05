import numpy as np

def parse_data(data):
    instr = list(np.array(data[0].split(',')).astype('int'))

    # parsing
    boards_ = np.array([d for d in data[1:] if d != ''])
    n = len(boards_)
    boards_ = boards_.reshape(int(n / 5), 5)

    boards = []
    for board_ in boards_:
        board = []
        for row in board_:
            row = np.array(row.strip().replace('  ', ' ').split(' ')).astype('int')
            board.append(row)
        boards.append(np.array(board))
        
    boards = np.array(boards)
    return boards, instr

def one(boards, instr):
    msk = np.zeros(boards.shape).astype(bool)
    nx = boards[0].shape[0]
    while len(instr) > 0:
        ins = instr.pop(0)
        idx = np.where(boards == ins)
        msk[idx] = True

        sum_cols = (msk.sum(axis = 1) == nx)
        sum_rows = (msk.sum(axis = 2) == nx)
        
        if sum_cols.any():
            winner = np.where(sum_cols)
            break
    
        elif sum_rows.any():
            winner = np.where(sum_rows)
            break
        else:
            pass
    
    msk_win = msk[winner[0]]
    board_win = boards[winner[0]]
    
    return board_win[~msk_win].sum() * ins

def test_one():
    data = open('test_input.txt', 'r').read().splitlines()
    boards, instr = parse_data(data)
    
    assert one(boards, instr) == 4512

if __name__ == '__main__':
    data = open('input.txt', 'r').read().splitlines()
    boards, instr = parse_data(data)
    test_one()
    print(one(boards, instr))