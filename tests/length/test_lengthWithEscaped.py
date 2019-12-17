"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class TestsEscapedLength(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            print(length("x\nz"));
        }
    """

    STDOUT = "3"
