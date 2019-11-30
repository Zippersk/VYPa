import unittest

from tests.testBase import TestBaseCases


class TestsPrint(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            int b = 4;
            print(b);
        }
    """

    STDOUT = "4"
