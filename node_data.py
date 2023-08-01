

#GuyC

class node_data:

    def __init__(self, key, pos = None, weight = 0, tag = 0, info = 0):
        self.key = key
        self.weight = weight
        if pos is not None:
            self.pos = pos
        else:
            self.pos = None
        self.tag = tag
        self.info = info

    def get_key(self) ->int:
        return self.key

    def get_weight(self) ->float:
        return self.weight

    def get_pos(self):
        return self.pos

    def get_tag(self):
        return self.tag

    def get_info(self):
        return self.info


    def set_key(self, key):
        self.key = key

    def set_weight(self, weight):
        self.weight = weight

    def set_pos(self, pos):
        self.pos = pos

    def set_tag(self,tag):
        self.tag = tag

    def set_info(self,info):
        self.info = info

    def __repr__(self):
        return " {}".format(self.key)





