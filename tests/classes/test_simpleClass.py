from tests.testBase import TestBaseCases


class IterativeFactorialComputation(TestBaseCases.TestBase):
    STDIN = "5"
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

    STDOUT = """Enter an integer to compute its factorial:
The result is: 120
"""


