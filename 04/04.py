import numpy as np
from copy import deepcopy

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
    
    instr = deepcopy(instr)
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


def test_two():
    data = open('test_input.txt', 'r').read().splitlines()
    boards, instr = parse_data(data)
    
    assert two(boards, instr) == 1924    

    
class Board():
    def __init__(self, config):
        self.config = config
        self.solved = False
        self.count = 0
        self.last_ins = None
        self.msk = np.zeros(config.shape).astype(bool)
        
    def update_count(self):
        self.count += 1
        
    def update(self, ins):
        idx = np.where(self.config == ins)
        self.msk[idx] = True
        self.last_ins = ins
        self.update_count()
            
    def check_win(self):
        solved = False
        sum_cols = (self.msk.sum(axis = 0) == self.config.shape[0])
        sum_rows = (self.msk.sum(axis = 1) == self.config.shape[0])
        
        if sum_cols.any():
            self.solved = True
        elif sum_rows.any():
            self.solved = True
        else:
            pass
        return self.solved
    
    def get_score(self):
        unmasked = self.config[~self.msk]
        return unmasked.sum()
    
    def return_last(self):
        return self.last_ins
    
    def return_count(self):
        return self.count

    
def two(boards, instr):
    bs = [Board(boards[i]) for i in range(len(boards))]
    for b in bs:
        for ins in instr:
            b.update(ins)
            solved = b.check_win()

            if solved:
                break
    
    # extract
    lasts = np.array([b.return_last() for b in bs])
    counts = np.array([b.return_count() for b in bs])
    scores = np.array([b.get_score() for b in bs])
    
    # last index
    last_idx = np.where(counts == np.max(counts))
    
    return (lasts[last_idx] * scores[last_idx])[0]


if __name__ == '__main__':
    data = open('input.txt', 'r').read().splitlines()
    boards, instr = parse_data(data)
    test_one()
    test_two()
    print(one(boards, instr))
    print(two(boards, instr))