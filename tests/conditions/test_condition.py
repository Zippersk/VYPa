"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
﻿from tests.testBase import TestBaseCases


class ConditionTest(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
    void main(void) {
        int j, n;
        string s;
        j = 0;
        n = 10;
        s = "hello world!";

        if (1-1 && 3-1 ) {
            print("True");
        }
        else
        {
            print("False");
        }
    }
    """

    STDOUT = "False"
