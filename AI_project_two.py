import random
import itertools as it


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


def hill_climbing_v1(graph, node_list, init_loc, upp_lim):
    # choose the initial random path
    initial_path = list(node_list[0:node_list.index(init_loc)] + node_list[node_list.index(init_loc)+1:len(node_list)+1])
    random.shuffle(initial_path)
    initial_path.insert(0, init_loc)
    initial_path.append(init_loc)
    # print(initial_path)

    # set initial best values to the values of the initial path
    best_score = score(initial_path, graph)
    best_path = initial_path

    # keep track of stats
    total_paths_searched = 1

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
            return best_score, total_paths_searched


def hill_climbing_v2(graph, node_list, init_loc, upp_lim):
    # choose the initial random path
    initial_path = list(node_list[0:node_list.index(init_loc)] + node_list[node_list.index(init_loc)+1:len(node_list)+1])
    random.shuffle(initial_path)
    initial_path.insert(0, init_loc)
    initial_path.append(init_loc)
    # print(initial_path)

    # set initial best values to the values of the initial path
    best_score = score(initial_path, graph)
    best_path = initial_path

    # keep track of stats
    total_paths_searched = 1

    t = 0
    while t < 5:
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
                t += 1
                best_path = best_next_path
                break

    return best_score, total_paths_searched


def hill_climbing_test(graph, node_list, init_loc, upp_lim):
    is_v1_better = 0

    best_score = upp_lim*len(node_list)
    for i in range(0, 50):
        stats_v1 = hill_climbing_v1(graph, node_list, init_loc, upp_lim)
        stats_v2 = hill_climbing_v2(graph, node_list, init_loc, upp_lim)
        if stats_v1[0] < best_score:
            best_score = stats_v1[0]
        if stats_v2[0] < best_score:
            best_score = stats_v2[0]

        if stats_v1[0] < stats_v2[0]:
            is_v1_better += 1

        print(stats_v1[0], stats_v2[0])

    print(best_score, is_v1_better)


def sim_anneal():
    return False


def main():
    n = 10
    low_lim = 100
    upp_lim = 2500
    init_loc = '0'

    node_list = []
    for i in range(0, n):
        node_list.append('%s'%i)

    graph = gen_graph(node_list, low_lim, upp_lim)
    # print_graph(n, graph)

    hill_climbing_test(graph, node_list, init_loc, upp_lim)

    return True


main()
