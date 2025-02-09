﻿"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class RecursiveFactorialComputation(TestBaseCases.TestBase):
    STDIN = "5"
    source_code = """
    /* Program 2: Recursive Factorial Computation */
    void main(void) {
      int a;
      int res;
      print("Enter an integer to compute its factorial:");
      a = readInt();
      if (a < 0) {
        print("\nFactorial of a negative integer is undefined!\n");
      } else {
        print("\nThe result is: ", factorial(a), "\n");
      }
    }
    int factorial(int n) {
      int decremented_n, temp_result;
      if (n < 2) {
        return 1;
      } else {
        decremented_n = n - 1;
        temp_result = factorial(decremented_n);
      }
      return n * temp_result;
    } // end of factorial
    """

    STDOUT = """Enter an integer to compute its factorial:
The result is: 120
"""
