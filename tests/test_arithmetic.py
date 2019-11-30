import unittest

from tests.testBase import TestBaseCases


class TestsArithmetic(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
    void main(void) {
        int a = 5 + 10 + 15;
        int b = 4;
        print(b);
    }
    """

    STDOUT = "4"
