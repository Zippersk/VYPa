"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class TestsPrintMultipleVariables(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            string b;
            b = "hello";
            int c;
            c = 4;
            print(b, 9 , "Ahoj", c);
        }
    """

    STDOUT = "hello9Ahoj4"
