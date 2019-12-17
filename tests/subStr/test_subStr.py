"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class TestsLength(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            string b;
            b = "abcdefghijklmnopr";
            print(subStr(b,3,7));
        }
    """

    STDOUT = "defghij"
