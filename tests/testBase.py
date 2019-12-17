"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
import os
import unittest
import subprocess
import uuid
from subprocess import PIPE

from app import parser
import src.output as printer
from src.VYPcode.AST.AbstractSyntaxTree import AST, AbstractSyntaxTree
from src.instructionsTape import MAIN_INSTRUCTION_TAPE


class TestBaseCases:
    class TestBase(unittest.TestCase):

        STDIN = None
        STDOUT = None
        STDERR = None
        source_code = ""
        return_code = 0

        test_dir = os.path.dirname(os.path.realpath(__file__))
        interpreter_path = os.path.join(test_dir, "vypint-1.0.jar")

        def run_parser(self):
            printer.Output = printer.Printer(self.source_file_path)
            parser.parse(self.source_code, debug=True)
            printer.Output.print()
            printer.Output.file = None
            print("\n\nRunning test with source code: \n")
            printer.Output.print()
            AST.clear()
            MAIN_INSTRUCTION_TAPE.clear()

        def run_vypa_interpreter(self):
            process = subprocess.run(f"java -jar {self.interpreter_path} {self.source_file_path}", stdout=PIPE, input=self.STDIN, encoding='UTF-8')
            self.assertEqual(self.STDERR, process.stderr)
            self.assertEqual(self.STDOUT, process.stdout)
            self.assertEqual(self.return_code, process.returncode)

        def test_VYPa(self):
            self.run_parser()
            self.run_vypa_interpreter()

        def setUp(self):
            self.source_file_path = os.path.join(self.test_dir, "temp", str(uuid.uuid1()) + ".txt")

        def tearDown(self):
            os.remove(self.source_file_path)
