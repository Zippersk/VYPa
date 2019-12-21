"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from tests.testBase import TestBaseCases


class CastingResultOfFunction(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        int GetTen(void) {
            return 10;
        }

        string GetWord(void) {
            return "Ahoj";
        }

        void main(void) {
            print(GetWord() + "test" + (string)(GetTen()));
        }
    """

    STDOUT = "Ahojtest10"
