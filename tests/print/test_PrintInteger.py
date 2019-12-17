"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class TestsPrintInteger(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            int b;
            b = 4;
            print(b);
        }
    """

    STDOUT = "4"
