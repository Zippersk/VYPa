from tests.testBase import TestBaseCases


class StringsAndEmbeddedFunctions(TestBaseCases.TestBase):
    STDIN = "ahoj"
    source_code = """
    /* Program 3: Program using Strings and Embedded Functions */
    void main(void) {
      string str1, str2;
      int p;
      str1 = "This is some text";
      while ((subStr(str1, p, 1)) != "") {
        p = p + 1;
      } // end of while
      print("\nThe length of ", str1, ", is ", p, " characters.\n");
    } // end of main
    """

    STDOUT = """4
"""
