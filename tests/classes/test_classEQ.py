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
          }
        }

        class Rectangle: Shape {
            int test;
        }

        void main(void) {
            Rectangle r, r2;
            Shape s;
            r2 = new Rectangle;
            r = new Rectangle;
            r.test = 9999;
            s = r;

            if (r == s) {
                print("True");
            }
            else
            {
                print("False");
            }

            if (r == r2) {
                print("True");
            }
            else
            {
                print("False");
            }
        }
    """

    STDOUT = "TrueFalse"
