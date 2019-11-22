from src.VYPcode.instructions import CREATE
from src.VYPcode.scopes import add_scope_variable
from src.instructionsTape import MAIN_INSTRUCTION_TAPE


class VYPaVariable:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    @staticmethod
    def declare(type, name):
        return add_scope_variable(VYPaVariable(type, name))

    @staticmethod
    def declare_anonym_variable(type):
        """
        Used when variable does not have name. For example function calling parameters or in expresion
        :param type: string
        :return: VYPaVariable
        """
        return add_scope_variable(VYPaVariable(type))