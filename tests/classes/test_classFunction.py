"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class ClassFunctionTest(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        class Shape: Object {
          int a;
          void setA(int value) {
            this.a = value;
          }
          int getA(void) {
            return this.a;
          }
        }
        void main(void) {
            Shape s;
            s = new Shape;
            s.setA(5);
            print(s.getA());
        }
    """

    STDOUT = "5"
