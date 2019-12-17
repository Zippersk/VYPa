"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class TestsFunctionReturnVariable(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        int GetFive(void) {
            return 5;
        }

        void main(void) {
            print(GetFive());
        }
    """

    STDOUT = "5"
