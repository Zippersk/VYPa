"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class TestsArithmeticMultipleVariables(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            int a,b,c,d,e,f,g;
            a = 1;
            b = 2;
            c = 3;
            d = 4;
            e = 5;
            f = 6;
            g = 7;
            print(a+b+c+d+e+f+g);
        }
    """

    STDOUT = "28"
