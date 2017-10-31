import random
import itertools as it
import math


def gen_graph(node_list, low_lim, upp_lim):
    graph = dict()
    for edge in it.permutations(node_list, 2):
        graph[edge] = random.randint(low_lim, upp_lim)
    return graph


def print_graph(n, graph):
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                print('__ ', end=' ')

            else:
                print(str(graph[('%s' % i, '%s' % j)]) + ' ', end=' ')
        print()
    print()
    return True


def score(path, graph):
    total = 0
    for i in range(0, len(path)-1):
        total += graph[(path[i], path[i+1])]

    return total


def path_successors(path):
    paths = []
    for i in range(1, len(path)-2):
        for j in range(i+1, len(path)-1):
            new_path = list(path)
            new_path[i], new_path[j] = new_path[j], new_path[i]
            paths.append(new_path)
    return paths


def neighbor(path):
    i = 0
    j = 0
    while i == j:
        i = random.randint(1, len(path) - 2)
        j = random.randint(1, len(path) - 2)
    new_path = list(path)
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path


def hill_climbing(graph, upp_lim, restarts, node_list, init_loc):
    final_best_path_score = upp_lim*len(node_list)

    # keep track of stats
    total_paths_searched = 1

    for i in range(0, restarts):
        # choose the initial random path
        initial_path = list(node_list[0:node_list.index(init_loc)] +
                            node_list[node_list.index(init_loc)+1:len(node_list)+1])
        random.shuffle(initial_path)
        initial_path.insert(0, init_loc)
        initial_path.append(init_loc)
        # print(initial_path)

        # set initial best values to the values of the initial path
        best_score = score(initial_path, graph)
        best_path = initial_path

        while True:
            # set initial score higher than any possible path score
            best_next_path_score = upp_lim*len(node_list)
            best_next_path = []
            for next_path in path_successors(best_path):
                total_paths_searched += 1
                path_score = score(next_path, graph)
                if path_score < best_next_path_score:
                    best_next_path_score = path_score
                    best_next_path = next_path

            if best_next_path_score < best_score:
                best_score = best_next_path_score
                best_path = best_next_path
                # print(best_path)

            else:
                break

        if best_score < final_best_path_score:
            final_best_path_score = best_score

    return final_best_path_score, total_paths_searched


def hill_climbing_test(repeat, upp_lim, restarts, graph, node_list, init_loc):

    for i in range(0, repeat):
        stats = hill_climbing(graph, upp_lim, restarts, node_list, init_loc)
        print('Hill Climbing')
        print("Score of best state: ", stats[0])
        print("Number of states searched: ", stats[1])
        print()


def prob_accept(old_score, new_score, temperature):
    if new_score <= old_score:
        return 1
    else:
        delta_e = new_score - old_score
        return math.exp(1/(delta_e/temperature))


def sim_anneal(graph, node_list, init_loc, init_temp, lowest_temp, cooling_factor, tries_per_temp):
    temperature = init_temp
    total_paths_searched = 0

    # initial solution
    initial_path = list(node_list[0:node_list.index(init_loc)] +
                        node_list[node_list.index(init_loc) + 1:len(node_list) + 1])
    random.shuffle(initial_path)
    initial_path.insert(0, init_loc)
    initial_path.append(init_loc)

    best_score = score(initial_path, graph)
    # best_path = initial_path

    current_path = initial_path

    while temperature > lowest_temp:

        for i in range(0, tries_per_temp):
            # track num of paths searched
            total_paths_searched += 1

            new_path = neighbor(current_path)
            if prob_accept(score(current_path, graph), score(new_path, graph), temperature) > random.random():
                current_path = new_path
                if score(current_path, graph) < best_score:
                    # best_path = current_path
                    best_score = score(current_path, graph)

        temperature *= cooling_factor

    return best_score, total_paths_searched


def sim_anneal_test(repeat, graph, node_list, init_loc, init_temp, lowest_temp, cooling_factor, tries_per_temp):
    # best_score = upp_lim*len(node_list)

    for i in range(0, repeat):
        stats = sim_anneal(graph, node_list, init_loc, init_temp, lowest_temp, cooling_factor, tries_per_temp)
        print('Simulated Annealing')
        print("Score of best state: ", stats[0])
        print("Number of states searched: ", stats[1])
        print()


def main():
    n = 10
    repeat = 5
    low_lim = 100
    upp_lim = 2500
    init_loc = '0'

    restarts = 50

    init_temp = 100
    lowest_temp = 1
    cooling_factor = 0.999
    tries_per_temp = 50

    node_list = []
    for i in range(0, n):
        node_list.append('%s'%i)

    for i in range(0, 5):
        graph = gen_graph(node_list, low_lim, upp_lim)
        # print_graph(n, graph)

        hill_climbing_test(repeat, upp_lim, restarts, graph, node_list, init_loc)
        sim_anneal_test(repeat, graph, node_list, init_loc, init_temp, lowest_temp, cooling_factor, tries_per_temp)

    return True


main()
