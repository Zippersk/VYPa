from tests.testBase import TestBaseCases


class BasicCondition(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
    void main(void) {
        if (0 < 0) {
            print("True");
        }
        else
        {
            print("False");
        }
    }
    """

    STDOUT = "False"
