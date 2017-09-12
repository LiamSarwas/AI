import queue
from collections import namedtuple
import heapq
import math

State = namedtuple('State', ['cost', 'state_list'])


def state_cmp(a, b):
    if a[1] == b[1]:
        return 0
    elif a[1] <= b[1]:
        return -1
    else:
        return 1


def get_init_state(goal):
    test = '12345678_'
    while True:
        start = input('Enter the starting configuration:')
        if test == ''.join(sorted(start)):
            if not is_solvable(start, goal):
                print('This puzzle isn\'t solvable, please try again.')
                continue
            return start
        else:
            print('Invalid Configuration. Please try again.')


def get_goal():
    test = '12345678_'
    while True:
        start = input('Enter the goal configuration:')
        if test == ''.join(sorted(start)):
            return start
        else:
            print('Invalid Configuration. Please try again.')


def print_state(n):
    print(n[0] + ' ' + n[1] + ' ' + n[2])
    print(n[3] + ' ' + n[4] + ' ' + n[5])
    print(n[6] + ' ' + n[7] + ' ' + n[8])
    print()


def is_solvable(init_state, goal):
    if parity(init_state) == parity(goal):
        return True
    return False


def parity(state):
    pairs = 0
    nums = state.replace('_', '')
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                pairs += 1
                
    if pairs % 2 == 0:
        return True
    return False


def get_successors(state):
    # defines movement at the corners
    # Upper Left
    if state[0] == '_':
        right = state[1]+state[0]+state[2:9]
        down = state[3]+state[1:3]+state[0]+state[4:9]
        return [right, down]

    # Upper Right
    if state[2] == '_':
        left = state[0]+state[2]+state[1]+state[3:9]
        down = state[0:2]+state[5]+state[3:5]+state[2]+state[6:9]
        return [left, down]

    # Lower Left
    if state[6] == '_':
        up = state[0:3]+state[6]+state[4:6]+state[3]+state[7:9]
        right = state[0:6]+state[7]+state[6]+state[8]
        return [up, right]

    # Lower Right
    if state[8] == '_':
        up = state[0:5]+state[8]+state[6:8]+state[5]
        left = state[0:7]+state[8]+state[7]
        return [up, left]
   
    # defining movement on the sides
    # Top
    if state[1] == '_':
        left = state[1]+state[0]+state[2:9]
        right = state[0]+state[2]+state[1]+state[3:9]
        down = state[0]+state[4]+state[2:4]+state[1]+state[5:9]
        return [left, right, down]

    # Left
    if state[3] == '_':
        up = state[3]+state[1:3]+state[0]+state[4:9]
        right = state[0:3]+state[4]+state[3]+state[5:9]
        down = state[0:3]+state[6]+state[4:6]+state[3]+state[7:9]
        return [up, right, down]

    # Right
    if state[5] == '_':
        up = state[0:2]+state[5]+state[3:5]+state[2]+state[6:9]
        left = state[0:4]+state[5]+state[4]+state[6:9]
        down = state[0:5]+state[8]+state[6:8]+state[5]
        return [up, left, down]

    # Bottom
    if state[7] == '_':
        left = state[0:6]+state[7]+state[6]+state[8]
        right = state[0:7]+state[8]+state[7]
        up = state[0:4]+state[7]+state[5:7]+state[4]+state[8]
        return [left, right, up]

    # defining movement from the middle
    # Middle
    if state[4] == '_':
        up = state[0]+state[4]+state[2:4]+state[1]+state[5:9]
        left = state[0:3]+state[4]+state[3]+state[5:9]
        down = state[0:4]+state[7]+state[5:7]+state[4]+state[8]
        right = state[0:4]+state[5]+state[4]+state[6:9]
        return [left, right, up, down]


def manhattan_dist(state, goal):
    score = 0
    for i in range(0, len(state)):
        if state[i] == goal[i]:
            continue
        if state[i] == '_':
            continue
        score += math.fabs(i % 3 - goal.index(state[i]) % 3) + math.fabs(i // 3 - goal.index(state[i]) // 3)
    return score


def out_of_place(state, goal):
    count = 0
    for i in range(0, len(state)):
        if state[i] == '_':
            continue
        if state[i] != goal[i]:
            count += 1
    return count


def depth_first(init_state, goal_state):
    q = queue.Queue()
    q.put(State(0, [init_state]))

    closed = set()
    max_nodes = 0
    count = 0

    while True:
        current = q.get()
        count += 1

        if q.qsize() + len(closed) > max_nodes:
            max_nodes = q.qsize() + len(closed)

        if current.state_list[-1] in closed:
            continue

        if current.state_list[-1] == goal_state:
            return current, count, max_nodes

        for successor in get_successors(current.state_list[-1]):
            new_list = list(current.state_list)
            new_list.append(successor)
            q.put(State(current.cost + 1, new_list))
        closed.add(current.state_list[-1])


def greedy_best_first(init_state, goal_state):
    heap = []
    heapq.heappush(heap, State(manhattan_dist(init_state, goal_state), [init_state]))

    closed = set()
    max_nodes = 0
    count = 0

    while True:
        current = heapq.heappop(heap)
        current_state = current.state_list[-1]
        count += 1

        if len(heap) + len(closed) > max_nodes:
            max_nodes = len(heap) + len(closed)

        if current_state in closed:
            continue

        if current_state == goal_state:
            return current, count, max_nodes

        for successor in get_successors(current_state):
            new_list = list(current.state_list)
            new_list.append(successor)
            heapq.heappush(heap, State(manhattan_dist(current_state, goal_state), new_list))
        closed.add(current_state)


def a_star_oop(init_state, goal_state):
    heap = []
    heapq.heappush(heap, State(manhattan_dist(init_state, goal_state), [init_state]))

    closed = set()
    max_nodes = 0
    count = 0

    while True:
        current = heapq.heappop(heap)
        current_state = current.state_list[-1]
        count += 1

        if len(heap) + len(closed) > max_nodes:
            max_nodes = len(heap) + len(closed)

        if current_state in closed:
            continue

        if current_state == goal_state:
            return current, count, max_nodes

        for successor in get_successors(current_state):
            new_list = list(current.state_list)
            new_list.append(successor)
            heapq.heappush(heap, State(out_of_place(current_state, goal_state) + len(current.state_list), new_list))

        closed.add(current_state)


def a_star_md(init_state, goal_state):
    heap = []
    heapq.heappush(heap, State(manhattan_dist(init_state, goal_state), [init_state]))

    closed = set()
    max_nodes = 0
    count = 0

    while True:
        current = heapq.heappop(heap)
        current_state = current.state_list[-1]
        count += 1

        if len(heap) + len(closed) > max_nodes:
            max_nodes = len(heap) + len(closed)

        if current_state in closed:
            continue

        if current_state == goal_state:
            return current, count, max_nodes

        for successor in get_successors(current_state):
            new_list = list(current.state_list)
            new_list.append(successor)
            heapq.heappush(heap, State(manhattan_dist(current_state, goal_state) + len(current.state_list), new_list))

        closed.add(current_state)


def main():
    print('A configuration is a blah blah blah.')
    
    goal = get_goal()
    init = get_init_state(goal)

    stats = depth_first(init, goal)
    print('Solution: \n')
    for state in stats[0].state_list:
        print_state(state)
    print('Max nodes in search space is: ', stats[2])
    print('Number of nodes searched is: ', stats[1])
    print('Solution depth is: ', len(stats[0].state_list))

    stats = greedy_best_first(init, goal)
    print('Solution: \n')
    for state in stats[0].state_list:
        print_state(state)
    print('Max nodes in search space is: ', stats[2])
    print('Number of nodes searched is: ', stats[1])
    print('Solution depth is: ', len(stats[0].state_list))

    stats = a_star_oop(init, goal)
    print('Solution: \n')
    for state in stats[0].state_list:
        print_state(state)
    print('Max nodes in search space is: ', stats[2])
    print('Number of nodes searched is: ', stats[1])
    print('Solution depth is: ', len(stats[0].state_list))

    stats = a_star_md(init, goal)
    print('Solution: \n')
    for state in stats[0].state_list:
        print_state(state)
    print('Max nodes in search space is: ', stats[2])
    print('Number of nodes searched is: ', stats[1])
    print('Solution depth is: ', len(stats[0].state_list))

main()
