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
          int id;
          void Shape(void) {
            print("constructor of Shape");
          }
          string toString(void) {
            return "instance of Shape " + (string)(this.id);
          }
        }
        void main(void) {
            Shape s;
            s = new Shape;
        }
    """

    STDOUT = "False"
