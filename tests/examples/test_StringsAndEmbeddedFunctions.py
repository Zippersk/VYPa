﻿"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class StringsAndEmbeddedFunctions(TestBaseCases.TestBase):
    STDIN = "ahoj"
    source_code = """
    /* Program 3: Program using Strings and Embedded Functions */
    void main(void) {
      string str1, str2;
      int p;
      str1 = "This is some text";
      str2 = str1 + " that can be a little longer.";
      print(str1, length(str2), str2, "\n");
      str1 = readString();
      while ((subStr(str1, p, 1)) != "") {
        p = p + 1;
      } // end of while
      print("\nThe length of ", str1, " is ", p, " characters.\n");
    } // end of main
    """

    STDOUT = """This is some text46This is some text that can be a little longer.

The length of ahoj is 4 characters.
"""
