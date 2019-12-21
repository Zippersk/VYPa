"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class ProgramwithClassesandObjects(TestBaseCases.TestBase):
    STDIN = "5"
    source_code = """
        /* Program 4: Program with Classes and Objects */
        class Shape: Object {
          int id;
          void Shape(void) {
            // print("constructor of Shape");
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
          int area(void) {
            return this.height * this.width;
          }
        }
        void main(void) {
          Rectangle r;
          r = new Rectangle;
          r.height = 10;
          r.width = 5;
          r.id = 42;


          print(r.toString());
        } // end of main
    """

    STDOUT = """instance of Shape 5 - rectangle 25"""


