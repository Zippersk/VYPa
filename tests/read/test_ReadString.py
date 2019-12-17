"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class TestsReadString(TestBaseCases.TestBase):
    STDIN = "hello world!"
    source_code = """
        void main(void) {
            string b;
            b = readString();
            print(b);
        }
    """

    STDOUT = "hello world!"
