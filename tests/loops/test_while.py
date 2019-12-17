"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class BasicWhile(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
    void main(void) {
        int a;
        a = 10;
        while (0 < a) {
            print(a);
            int c;
            a = a - 1;
        }
    }
    """

    STDOUT = "10987654321"
