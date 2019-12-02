class VYPaBaseType:
    def __init__(self, name, default):
        self.default = default
        self.name = name

    def get_name(self):
        return self.name

    def get_default(self):
        return self.default

    def __eq__(self, other):
        return self.name == other.name
