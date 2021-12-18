import numpy as np

def one(state):
    min_pos, max_pos = np.min(state), np.max(state)
    costs = []
    for i in range(min_pos, max_pos):
        cost = np.sum(np.abs(state - i))
        costs.append(cost)

    idx = np.where(costs == np.min(costs))[0][0]
    return costs[idx]

def test():
    state = np.array([16,1,2,0,4,2,7,1,2,14])
    one(state) == 37
    two(state) == 168
    
def two(state):
    min_pos, max_pos = np.min(state), np.max(state)

    costs = []
    for i in range(min_pos, max_pos):
        distances = np.abs(state - i)
        
        # gaussian sum
        fuel = np.sum((distances**2 + distances) / 2)
        costs.append(fuel)
    
    costs = np.array(costs)
    idx = np.where(costs == np.min(costs))[0][0]
    return costs[idx].astype('int')

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        state = f.read().split(',')
        state = np.array([int(s) for s in state])
    
    test()
    
    # part 1
    print(one(state))
    
    # part 2
    print(two(state))