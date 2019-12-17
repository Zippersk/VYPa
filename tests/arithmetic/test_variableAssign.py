"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class TestsVariableAssign(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
          int a,b,c,d,e,f,g,h;
          a = 1;
          b = a;
          c = b;
          d = c;
          e = d;
          f = e;
          g = f;
          h = g;
          print(h);

        }
    """

    STDOUT = "1"
