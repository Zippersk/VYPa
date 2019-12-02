from src.LazyCodeEvaluation.LazyCodeEvaluater import LazyCode
from src.VYPcode.VYPaTypes.VYPaInt import VYPaInt
from src.VYPcode.VYPaTypes.VYPaString import VYPaString
from src.VYPcode.VYPaTypes.VYPaVoid import VYPaVoid
from src.VYPcode.VYPaTypes.baseType import VYPaBaseType
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
from src.error import Error, Exit
from enum import Enum


class TypeCheckerPolicy(Enum):
    ExactMatch = 1
    OneOf = 2
    NoneOf = 3


class LazyTypeChecker:
    def __init__(self, variable, types, policy=TypeCheckerPolicy.ExactMatch):
        self.policy = policy
        self.types : VYPaBaseType or [VYPaBaseType] = types  # types is one type or array of types
        self.variable = variable
        LazyCode.add(self)

    def exact_match_policy(self):
        if self.variable.get_type() != self.types:
            Exit(Error.SemanticError, "Wrong types")

    def one_of_policy(self):
        if self.variable.get_type() not in self.types:
            Exit(Error.SemanticError, "Wrong types")

    def none_of_policy(self):
        if self.variable.get_type() in self.types:
            Exit(Error.SemanticError, "Wrong types")

    def run(self):
        if self.policy == TypeCheckerPolicy.ExactMatch:
            self.exact_match_policy()
        elif self.policy == TypeCheckerPolicy.OneOf:
            self.one_of_policy()
        elif self.policy.NoneOf:
            self.none_of_policy()

    @staticmethod
    def plus(variable1: VYPaVariable, variable2: VYPaVariable):
        LazyTypeChecker(variable1, [VYPaInt(), VYPaString()], TypeCheckerPolicy.OneOf)
        LazyTypeChecker(variable2, [VYPaInt(), VYPaString()], TypeCheckerPolicy.OneOf)

    @staticmethod
    def subtract(variable1: VYPaVariable, variable2: VYPaVariable):
        LazyTypeChecker(variable1, VYPaInt())
        LazyTypeChecker(variable2, VYPaInt())

    @staticmethod
    def multiply(variable1: VYPaVariable, variable2: VYPaVariable):
        LazyTypeChecker(variable1, VYPaInt())
        LazyTypeChecker(variable2, VYPaInt())

    @staticmethod
    def divide(variable1: VYPaVariable, variable2: VYPaVariable):
        LazyTypeChecker(variable1, VYPaInt())
        LazyTypeChecker(variable2, VYPaInt())

    @staticmethod
    def is_int(variable):
        LazyTypeChecker(variable, VYPaInt())

    @staticmethod
    def is_string(variable):
        LazyTypeChecker(variable, VYPaString())

    @staticmethod
    def is_void(variable):
        LazyTypeChecker(variable, VYPaVoid())
