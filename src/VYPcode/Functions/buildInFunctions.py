"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.assigment import AST_assigment
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.binaryOperations.ADD import AST_ADD
from src.VYPcode.AST.blocks.binaryOperations.AND import AST_AND
from src.VYPcode.AST.blocks.binaryOperations.EQ import AST_EQ
from src.VYPcode.AST.blocks.binaryOperations.GT import AST_GT
from src.VYPcode.AST.blocks.binaryOperations.LT import AST_LT
from src.VYPcode.AST.blocks.binaryOperations.NOT import AST_NOT
from src.VYPcode.AST.blocks.binaryOperations.OR import AST_OR
from src.VYPcode.AST.blocks.binaryOperations.SUB import AST_SUBI
from src.VYPcode.AST.blocks.class_block import AST_class
from src.VYPcode.AST.blocks.declaration import AST_declaration
from src.VYPcode.AST.blocks.expression import AST_expression
from src.VYPcode.AST.blocks.function import AST_function
from src.VYPcode.AST.blocks.function_call import AST_function_call
from src.VYPcode.AST.blocks.function_return import AST_return
from src.VYPcode.AST.blocks.ifelse import AST_ifelse, AST_condition_body
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
from src.VYPcode.AST.blocks.while_loop import AST_while
from src.VYPcode.AST.blocks.word import AST_GETWORD, AST_SETWORD, AST_RESIZE, AST_COPY
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Instructions.Instructions import WRITEI, WRITES, READI, GETSIZE, READS, GETWORD, RESIZE, DUMPSTACK, \
    DUMPREGS, DUMPHEAP, SETWORD, COPY, CREATE, SET, ADDI
from src.VYPcode.Types.VYPaClass import VYPaClass
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid


class VYPaBuildInFunctionClass(AST_function):
    def __init__(self, type, name, params):
        super().__init__(type, name, params)
        self.return_expression = None
        self.function = AST.get_root().add_function(self)
        self.label = f"buildIn_{name}"


class ObjectVYPa(AST_class):
    def __init__(self):
        super().__init__("Object", None)
        to_string_function = AST_function(VYPaString(), "Object_toString", [AST_variable(VYPaClass("Object"), "this")])
        to_string_function.set_label(f"class_Object_func_toString")
        AST.get_root().add_function(to_string_function)

        get_class_function = AST_function(VYPaString(), "Object_getClass", [AST_variable(VYPaClass("Object"), "this")])
        get_class_function.set_label(f"class_Object_func_getClass")
        AST.get_root().add_function(get_class_function)

        AST.root.add_class(self)


class PrintIntVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printInt", [AST_variable(VYPaInt(), "number")])
        block = AST_block()
        block.add_instruction(WRITEI(self.function.stack.top()))
        self.add_block(block)


class PrintStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printString", [AST_variable(VYPaString(), "string")])
        block = AST_block()
        block.add_instruction(WRITES(self.function.stack.top()))
        self.add_block(block)


class ReadIntVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaInt(), "readInt", [])
        self.add_block(AST_declaration(VYPaInt(), ["number"]))

        readi_block = AST_block()
        readi_block.add_instruction(READI(VYPaRegister.DestinationReg))
        readi_block.stack.set(VYPaRegister.DestinationReg)
        self.add_block(readi_block)

        self.add_block(AST_return(AST_value(VYPaInt(), self.stack.top())))


class ReadStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "readString", [])
        self.add_block(AST_declaration(VYPaString(), ["string"]))

        reads_block = AST_block()
        reads_block.add_instruction(READS(VYPaRegister.DestinationReg))
        reads_block.stack.set(VYPaRegister.DestinationReg)
        self.add_block(reads_block)

        self.add_block(AST_return(AST_value(VYPaString(), self.stack.top())))


class LengthVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaInt(), "length", [AST_variable(VYPaString(), "string")])

        getsize_block = AST_block()
        getsize_block.add_instruction(GETSIZE(VYPaRegister.DestinationReg, self.function.stack.top()))
        getsize_block.stack.set(VYPaRegister.DestinationReg)
        self.add_block(getsize_block)

        self.add_block(AST_return(AST_value(VYPaInt(), self.stack.top())))


class StringsConcat(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "stringConcat", [AST_variable(VYPaString(), "s1"),
                                                        AST_variable(VYPaString(), "s2")])
        self.add_block(
            AST_condition_body([
                AST_declaration(VYPaString(), ["new_string"]),
                AST_COPY(AST_value(VYPaString(), VYPaRegister.DestinationReg), AST_variable_call("s1")),
                AST_assigment(AST_variable_call("new_string"), AST_value(VYPaString(), VYPaRegister.DestinationReg)),
                AST_RESIZE(AST_variable_call("new_string"),
                           AST_expression(AST_ADD(
                               AST_function_call("length", [AST_variable_call("s1")]),
                               AST_function_call("length", [AST_variable_call("s2")])
                           ))),
                AST_declaration(VYPaInt(), ["i"]),
                AST_while(
                    AST_expression(
                        AST_LT(
                            AST_variable_call("i"),
                            AST_function_call("length", [AST_variable_call("s2")])
                        )
                    ),
                    [
                        AST_GETWORD(
                            AST_value(VYPaInt(), str("$3")),
                            AST_variable_call("s2"),
                            AST_variable_call("i")),
                        AST_SETWORD(AST_variable_call("new_string"),
                                    AST_expression(
                                        AST_ADD(
                                            AST_variable_call("i"),
                                            AST_function_call("length", [AST_variable_call("s1")])),
                                    ), AST_value(VYPaInt(), str("$3"))),
                        AST_assigment(AST_variable_call("i"), AST_expression(
                            AST_ADD(AST_variable_call("i"), AST_value(VYPaInt(), 1))
                        ))
                    ]
                ),
                AST_return(AST_variable_call("new_string"))
            ])
        )


class SubStrVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "subStr", [AST_variable(VYPaString(), "s"),
                                                  AST_variable(VYPaInt(), "i"),
                                                  AST_variable(VYPaInt(), "n")])
        self.add_block(
            AST_ifelse(
                AST_expression(
                    AST_OR(
                        AST_LT(
                            AST_variable_call("n"),
                            AST_value(VYPaInt(), 0)
                        ),
                        AST_OR(
                            AST_LT(
                                AST_variable_call("i"),
                                AST_value(VYPaInt(), 0)
                            ),
                            AST_OR(
                                AST_GT(
                                    AST_variable_call("i"),
                                    AST_function_call("length", [AST_variable_call("s")])
                                ),
                                AST_EQ(
                                    AST_variable_call("i"),
                                    AST_function_call("length", [AST_variable_call("s")])
                                )
                            )
                        )
                    )
                ),
                [
                    AST_return(
                        AST_expression(AST_value(VYPaString(), '""'))
                    )
                ],
                [
                    AST_declaration(VYPaString(), ["new_substr"]),
                    AST_declaration(VYPaInt(), ["j"]),
                    AST_RESIZE(AST_variable_call("new_substr"), AST_variable_call("n")),
                    AST_while(
                        AST_expression(
                            AST_AND(
                                AST_LT(
                                    AST_variable_call("j"),
                                    AST_variable_call("n")
                                ),
                                AST_LT(
                                    AST_variable_call("j"),
                                    AST_function_call("length", [AST_variable_call("s")])
                                )
                            )
                        ),
                        [
                            AST_GETWORD(VYPaRegister.DestinationReg, AST_variable_call("s"), AST_expression(
                                AST_ADD(
                                    AST_variable_call("i"),
                                    AST_variable_call("j")
                                )
                            )),
                            AST_SETWORD(AST_variable_call("new_substr"), AST_variable_call("j"), VYPaRegister.DestinationReg),
                            AST_assigment(AST_variable_call("j"), AST_expression(
                                AST_ADD(AST_variable_call("j"), AST_value(VYPaInt(), 1))
                            ))
                        ]
                    ),
                    AST_return(AST_expression(AST_variable_call("new_substr")))
                ]
            )
        )
