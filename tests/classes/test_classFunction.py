"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class SimpleClassTest(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        class Shape: Object {
          int a, b;
          void Shape(void) {
            this.a = 42;
          }
        }
        void main(void) {
            Shape s;
            s = new Shape;
            print(s.a);
        }
    """

    STDOUT = "42"
