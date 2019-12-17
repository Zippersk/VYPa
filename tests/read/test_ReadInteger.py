"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class TestsReadInteger(TestBaseCases.TestBase):
    STDIN = "4"
    source_code = """
        void main(void) {
            int b;
            b = readInt();
            print(b);
        }
    """

    STDOUT = "4"
