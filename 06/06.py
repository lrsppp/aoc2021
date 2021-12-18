import numpy as np # np.roll very useful for this puzzle

def solution(states, n_days):
    # initialize counter
    count = np.zeros(9)
    for state in states:
        count[state] += 1
        
    for t in range(n_days):
        next_count = np.roll(count, -1)
        next_count[6] += count[0]
        count = next_count
        
    return np.sum(count).astype('int')

def test_one():
    states = np.array([3,4,3,1,2])
    assert solution(states, 80) == 5934
    
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        states = f.read().split(',')
        states = [int(s) for s in states]
        
    # test
    test_one()
    
    # part 1
    print(solution(states, 80))

    # part 2
    print(solution(states, 256))