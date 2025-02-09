﻿"""
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
          int a;
          void Shape(void) {
            this.a = 16;
          }
        }

        class Rectangle: Shape {
            int a;
            void Rectangle(void) {
                this.a = 17;
            }
        }

        void main(void) {
            Rectangle r;
            r = new Rectangle;
            print(r.a);
        }
    """

    STDOUT = "17"
