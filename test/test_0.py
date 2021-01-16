from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
import matplotlib.pyplot as plt






def check():
    check0()
    check1()
    check2()

def check0():
    g = DiGraph()  # creates an empty directed graph
    for n in range(7):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(1, 3, 1.1)
    g.add_edge(1, 4, 1.9)
    g.add_edge(1, 5, 1.1)
    g.add_edge(2, 7, 1.3)
    g.add_edge(2, 6, 1.1)
    g.add_edge(1, 3, 1.9)
    g.add_edge(3, 2, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(0, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g.remove_edge(1, 3)
    g.add_edge(7, 3, 10)
    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    g_algo = GraphAlgo(g)
    print(g_algo.shortest_path(0, 3))
    g_algo.save_to_json('test0_saved')
    g_algo.plot_graph()


def check1():
    g = DiGraph()
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(1, 3, 1.1)
    g.remove_edge(0, 3)
    g.remove_edge(1, 3)
    g.add_edge(7, 3, 2)
    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    g_algo = GraphAlgo(g)
    print(g_algo.shortest_path(0, 3))
    g_algo.save_to_json('test1_saved')
    g_algo.plot_graph()


def check2():

    g_algo = GraphAlgo()
    file = 'data/A2'
    g_algo.load_from_json(file)
    g_algo.get_graph().remove_edge(13, 14)
    g_algo.save_to_json("test3_saved")
    dist, path = g_algo.shortest_path(1, 7)
    print(dist, path)
    dist, path = g_algo.shortest_path(47, 19)
    print(dist, path)
    dist, path = g_algo.shortest_path(20, 2)
    print(dist, path)
    dist, path = g_algo.shortest_path(2, 20)
    print(dist, path)
    print(g_algo.connected_component(0))
    print(g_algo.connected_components())
    g_algo.plot_graph()


if __name__ == '__main__':
    check()
