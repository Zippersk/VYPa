"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class IterativeFactorialComputation(TestBaseCases.TestBase):
    STDIN = "5"
    source_code = """
    /* Program 1: Iterative Factorial Computation */
    void main(void) { // Program Main function
        int a, res;
        print("Enter an integer to compute its factorial:");
        a = readInt();
        if (a < 0) {
            print("\nFactorial of a negative integer is undefined!\n"); }
        else {
            res = 1;
            while (a > 0) {
                res = res * a; a = a - 1;
            } // endwhile
            print("\nThe result is: ", res, "\n");
        } // endif
    } // main
    """

    STDOUT = """Enter an integer to compute its factorial:
The result is: 120
"""
