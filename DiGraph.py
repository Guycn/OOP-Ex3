from src.node_data import node_data
from src.GraphInterface import GraphInterface

class DiGraph(GraphInterface):
    def __init__(self):
        self.nodes = dict()
        self.Vin = dict()
        self.Vout = dict()
        self.Nodes = 0
        self.Edges = 0
        self.MC = 0

    def v_size(self) -> int:
        return self.Nodes

    def e_size(self) -> int:
        return self.Edges

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.Vin[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.Vout[id1]

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes and id2 not in self.Vout[id1]:
            self.Vout[id1][id2] = weight
            self.Vin[id2][id1] = weight
            self.MC += 1
            self.Edges += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.nodes:
            self.nodes[node_id] =  node_data(node_id, pos)
            self.Vin[node_id] = {}
            self.Vout[node_id] = {}
            self.MC += 1
            self.Nodes +=1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            return False

        self.Nodes -= 1
        self.Edges -= len(self.Vout[node_id])
        del self.Vout[node_id]

        self.Nodes -= 1
        self.Edges -= len(self.Vin[node_id])
        del self.Vin[node_id]

        for i in self.Vout:
            if node_id in self.Vout[i].keys():
                del self.Vout[i][node_id]

        for i in self.Vin.keys():
            if node_id in self.Vin[i].keys():
                del self.Vin[i][node_id]

        self.nodes.pop(node_id)
        self.Nodes -= 1
        self.MC += 1
        return True

    def get_key(self, n:node_data):
        return n.get_key()

    def get_pos(self, n:node_data):
        return n.get_pos()





    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.nodes or node_id2 not in self.nodes:
            return False
        if node_id1 not in self.Vin[node_id2] or node_id2 not in self.Vout[node_id1]:
            return False

        if node_id1 in self.Vin[node_id2] or node_id2 not in self.Vout[node_id1]:
            del self.Vout[node_id1][node_id2]
            del self.Vin[node_id2][node_id1]
            self.Edges -= 1
            self.MC -= 1
            return True


    def __repr__(self):
        s = "|V|={} , |E|={}\n".format(self.Nodes, self.Edges)
        j=0;
        for key in self.nodes.keys():
            for i in self.all_out_edges_of_node(key).keys():
                s += str(j) + ": " + str(j) +": "
                s += "|edges out| "
                s += str(key)
                s += " |edges in| "
                s += str(i) + "\t"
                j += 1
        return s

