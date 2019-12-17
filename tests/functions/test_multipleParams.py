"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class TestsMultipleFunctionsCall(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        int sub(int a, int b) {
            return a -b;
        }

        void main(void) {
            print(sub(10,4));
        }
    """

    STDOUT = "6"
