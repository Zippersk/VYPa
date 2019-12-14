from tests.testBase import TestBaseCases


class StringEqual(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """


    void main(void) {
        if ("ahoj" == "ahoj") {
            print("True");
        }
        else
        {
            print("False");
        }
    }
    """

    STDOUT = "True"
