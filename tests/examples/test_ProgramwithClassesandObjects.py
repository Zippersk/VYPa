﻿from tests.testBase import TestBaseCases


class IterativeFactorialComputation(TestBaseCases.TestBase):
    STDIN = "5"
    source_code = """
        /* Program 4: Program with Classes and Objects */
        class Shape: Object {
          int id;
          void Shape(void) {
            print("constructor of Shape");
          }
          string toString(void) {
            return "instance of Shape " + (string)(this.id);
          }
        }
        class Rectangle: Shape {
          int height, width;
          string toString(void) {
            return super.toString() +
              " - rectangle " + (string)(this.area());
          }
          int area() {
            return this.height * this.width;
          }
        }
        void main(void) {
          Rectangle r;
          r = new Rectangle;
          r.id = 42;
          r.width = readInt();
          r.height = readInt();
          Shape s;
          s = r;
          print(s.toString());
        } // end of main
    """

    STDOUT = """Enter an integer to compute its factorial:
The result is: 120
"""


