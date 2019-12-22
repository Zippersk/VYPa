from collections import OrderedDict


class VariablesStore(OrderedDict):
    def __len__(self):
        size = 0
        for variable in self.values():
            size += variable.get_size()
        return size