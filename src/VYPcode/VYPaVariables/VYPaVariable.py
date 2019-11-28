from src.VYPcode.scopes.scopes import get_current_scope


class VYPaVariable:
    def __init__(self, type, name):
        self.stack_offset = None
        self.type = type
        self.name = name

    def call(self):
        return self

    def assign(self, source):
        return self

    def compute_stack_offset(self):
        self.stack_offset = len(get_current_scope().variables) - get_current_scope().get_variable_index(self.name)
        return self.stack_offset

