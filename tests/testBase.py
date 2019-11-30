import os
import unittest
import subprocess
import uuid
from subprocess import PIPE

from app import parser
import src.output as printer


class TestBaseCases:
    class TestBase(unittest.TestCase):
        STDIN = ""
        source_code = ""
        STDOUT = ""
        return_code = 0
        test_dir = os.path.dirname(os.path.realpath(__file__))
        interpreter_path = os.path.join(test_dir, "vypint-1.0.jar")
        source_file_path = os.path.join(test_dir, "temp", str(uuid.uuid1()) + ".txt")

        def run_parser(self):
            printer.Output = printer.Printer(self.source_file_path)
            parser.parse(self.source_code)
            printer.Output.print()

        def run_vypa_interpreter(self):
            process = subprocess.run(["java", "-jar", self.interpreter_path, self.source_file_path], stdout=PIPE, input=self.STDIN, encoding='ascii')
            self.assertEqual(process.stdout, self.STDOUT)
            self.assertEqual(process.returncode, self.return_code)

        def test_VYPa(self):
            self.run_parser()
            self.run_vypa_interpreter()

        def tearDown(self):
            os.remove(self.source_file_path)


