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
          int a, b;
        }
        void main(void) {
            Shape s;
            s = new Shape;
            s.a = 42;
            s.b = 43;
            print(s.a);
        }
    """

    STDOUT = "42"
