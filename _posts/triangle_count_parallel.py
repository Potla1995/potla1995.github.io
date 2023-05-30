import networkx as nx
from matplotlib import pyplot as plt
from itertools import combinations
import multiprocessing
from joblib import Parallel, delayed

num_vertices = 7
num_triangles = 8


def total_triangles(host_graph: nx.Graph):
    total_triangles = 0
    for v in list(host_graph.nodes()):
        nbr = list(host_graph.neighbors(v))
        N_v = nx.Graph()
        N_v.add_edges_from([(i, j) for i in nbr for j in nbr if i < j and i in host_graph[j]])
        total_triangles += N_v.number_of_edges()
    return total_triangles / 3


def is_p3_hat_free(host_graph: nx.Graph):
    for v in list(host_graph.nodes()):
        nbr = list(host_graph.neighbors(v))
        N_v = nx.Graph()
        N_v.add_edges_from([(i, j) for i in nbr for j in nbr if i < j and i in host_graph[j]])
        # If N_v is P_3-free, it must have <= deg(v) many edges.
        if N_v.number_of_edges() > N_v.number_of_nodes():
            return False
        # Search for a P_3
        for v_0, v_1 in N_v.edges():
            for v_2 in N_v[v_1]:
                for v_3 in N_v[v_2]:
                    if len({v_0, v_1, v_2, v_3}) == 4:
                        return False
    # If no P_3 was found in any neighborhood, host graph is \hat{P_3}-free
    return True


def calculate_hat_p3_free(graph_list_triangles):
    test_graph = nx.Graph()
    for triangle in graph_list_triangles:
        test_graph.add_edges_from(
            ((triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[0], triangle[2])))
    if total_triangles(test_graph) == num_triangles:
        if is_p3_hat_free(test_graph):
            print(
                f'Found a P3-hat-free graph on at least {num_triangles} triangles and {num_vertices} vertices')
            nx.draw_networkx(test_graph)
            print(graph_list_triangles)
            plt.savefig(f'{num_vertices}-vertex-{num_triangles}-triangles-P3-hat-free.png')
            return -1
    return 0


def __main__():
    # Generate all graphs with n = num_vertices and t = num_triangles where first triangle is [0,1,2]
    vertex_set = range(num_vertices)
    all_triangles = set(combinations(vertex_set, 3))
    # Assume the triangles 012 and 013 are always triangles in the generated graph
    # (otherwise all triangles cannot be edge-disjoint for n = 8 and t = 9)
    first_triangles = ((0, 1, 2), (0, 1, 3))
    all_triangles.remove(first_triangles[0])
    all_triangles.remove(first_triangles[1])
    all_triangles_copy = list(all_triangles)
    removed_triangles = ''
    # Remove all triangles that intersect with the edges (0,2), (0,3), (1,2) and (1,3) and have an external vertex as
    # these form \hat{P_3}'s
    for triangle in all_triangles_copy:
        if len({(triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[0], triangle[2])}.
                       intersection(((0, 2), (0, 3), (1, 2), (1, 3)))) > 0:
            if len(set(triangle).intersection({0, 1, 2, 3})) < 3:
                all_triangles.remove(triangle)
                removed_triangles += str(triangle) + ' '
    print(f'Removed triangles: {{{removed_triangles}}}')
    print(f'Available triangles: {all_triangles}')
    graph_triangles = list(combinations(list(all_triangles), num_triangles - 2))
    for i in range(len(graph_triangles)):
        graph_triangles[i] = first_triangles + graph_triangles[i]

    print(f'Generated {len(graph_triangles)} many graphs.')

    # For each combination, generate a graph and evaluate if it is \hat{P_3}-free
    # Set n_jobs to however many CPU threads are available
    num_cores = multiprocessing.cpu_count()
    Parallel(n_jobs=num_cores - 1)(
        delayed(calculate_hat_p3_free)(graph_triangles[i]) for i in range(len(graph_triangles))
    )

    print('Finished iteration.')


__main__()
