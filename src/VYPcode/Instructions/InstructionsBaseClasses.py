"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
class OperationBase:
    def get_name_or_value(self, operand):
        if hasattr(operand, 'value'):
            return operand.value
        if hasattr(operand, 'name'):
            return operand.name
        return str(operand)


class NoArgsInstruction(OperationBase):
    def __init__(self, operation):
        self.operation = operation

    def __str__(self):
        return f'{self.operation}'


class OneArgsInstruction(OperationBase):
    def __init__(self, operation, first):
        self.operation = operation
        self.first_str = str(first)
        self.first = first

    def __str__(self):
        return f'{self.operation} {self.first_str}' \
               f' # {self.get_name_or_value(self.first)}'


class TwoArgsInstruction(OperationBase):
    def __init__(self, operation, first, second):
        self.operation = operation
        self.first_str = str(first)
        self.second_str = str(second)
        self.first = first
        self.second = second

    def __str__(self):
        return f'{self.operation} {self.first_str} {self.second_str} ' \
               f' # {self.get_name_or_value(self.first)} {self.get_name_or_value(self.second)}'


class ThreeArgsInstruction(OperationBase):
    def __init__(self, operation, first, second, third):
        self.operation = operation
        self.first_str = str(first)
        self.second_str = str(second)
        self.third_str = str(third)
        self.first = first
        self.second = second
        self.third = third

    def __str__(self):
        return f'{self.operation} {self.first_str} {self.second_str} {self.third_str}' \
               f' # {self.get_name_or_value(self.first)} {self.get_name_or_value(self.second)} {self.get_name_or_value(self.third)}'
