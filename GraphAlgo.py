import json
import math
import random
import matplotlib as plt
import matplotlib.pyplot as plt

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph = DiGraph):
        self.graph = graph


    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        Graph = DiGraph()
        try:
            with open(file_name, 'r+') as file:
                load_f = json.load(file)

            for tmp in load_f["Nodes"]:
                if "pos" in tmp:
                    pos = tuple(map(float, tmp["pos"].split(',')))
                    Graph.add_node(tmp["id"],pos)
                else:
                    Graph.add_node(tmp["id"])

            for edge in load_f["Edges"]:
                Graph.add_edge(edge["src"], edge["dest"], edge["w"])

            self.graph = Graph
            file.close()
            return True

        except Exception as ex:
            print("Attempt to load from file", ex)
            return False
        finally:
            file.close()



    def save_to_json(self, file_name: str) -> bool:
        try:
            data = {"Nodes":[], "Edges":[]}
            for node in self.graph.get_all_v().values():
                if node.get_pos() is None:
                    data["Nodes"].append({"id": node.key})
                else:
                    data["Nodes"].append({"pos": str(node.get_pos()), "id": node.key})

            for src in self.graph.Vout.keys():
                for dest, weight in self.graph.all_out_edges_of_node(src).items():
                    data["Edges"].append({"src": src, "w": weight, "dest": dest})

            with open(file_name, 'w') as file:
                json.dump(data, file, ensure_ascii = False, indent = 4)
                return True
        except Exception as ex:
            print("Attempt to save failed", ex)
            return False
        finally:
            file.close()


    def short_way(self, id1: int, value: dict, prev: dict):
        j = len(self.graph.all_out_edges_of_node(id1))
        if j == 0 :
            return 1

        for y, w in self.graph.all_out_edges_of_node(id1).items():
            if value[y] > value[id1] + w:
                value[y] = value[id1] + w
                prev[y] = id1
                self.short_way(y, value, prev)
        return 1


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        gkeys = []
        for i in self.graph.get_all_v():
            gkeys.append(i)
        if id1 not in gkeys or id2 not in gkeys:
            return (float('inf'), [])
        value = {j: math.inf for j in gkeys}
        prev = {}
        value[id1] = 0
        self.short_way(id1, value, prev)
        if value[id2] == 'inf':
            return (float('inf'), [])
        list = []
        t = id2
        nodes = []
        for r in self.graph.get_all_v():
            nodes.append(r)

        while 1:
            list.append(nodes[t])
            try:
                t = prev[t]
            except:
                return (float('inf'), [])
            if t == id1:
                list.append(nodes[t])
                break
        list.reverse()
        return value[id2], list

    def connected_component(self, id1: int) -> list:
        if self.graph is None or id1 not in self.graph.get_all_v().keys():
            return []

        nodes = self.graph.get_all_v()
        list = []
        list_out = []
        list_out.append(nodes.get(id1))
        temp = [id1]

        while temp:
            curr = temp.pop()
            nei_out = self.graph.all_out_edges_of_node(curr).keys()
            for i in nei_out:
                if nodes[i] not in list_out :
                    list_out.append(nodes.get(i))
                    temp.append(i)

        list_in = []
        list_in.append(nodes.get(id1))
        tmp = [id1]

        while tmp:
            cur = tmp.pop()
            nei_in = self.graph.all_in_edges_of_node(cur).keys()
            for i in nei_in:
                if nodes[i] not in list_in:
                        list_in.append(nodes.get(i))
                        tmp.append(i)
        for j in nodes.keys():
            if nodes[j] in list_out and nodes[j] in list_in:
                list.append(nodes[j])
        return list


    def connected_components(self) -> list[list]:
        if self.graph is None:
            return []
        list = []
        nodes = []
        y = self.graph.get_all_v()
        for k in y:
            nodes.append(k)

        while len(nodes) > 0:
            j = self.connected_component(nodes[0])
            list.append(j)

            for i in j:
                u = self.graph.get_key(i)
                nodes.remove(u)
        return list


    def plot_graph(self) -> None:
        g = []
        for r in self.graph.get_all_v():
            g.append(r)
        l = {}
        l = self.graph.get_all_v()

        for node in l:
            if not l[node].get_pos():
                l[node].pos = (random.uniform(0, 5), random.uniform(0, 5), 0)

            _p1 = l[node].get_pos()
            plt.plot(_p1[0], _p1[1], 'ro')


        for key in g:

            for k, w in self.graph.all_out_edges_of_node(key).items():

                p1 = l[key].get_pos()
                p2 = l[k].get_pos()
                x1 = p1[0]
                y1 = p1[1]
                x2 = p2[0]
                y2 = p2[1]

                plt.arrow(x1, y1, (x2 - x1), (y2 - y1), length_includes_head=True, width=0.000003, head_width=0.0002)

        plt.tight_layout()
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Graph Result")
        plt.show()
