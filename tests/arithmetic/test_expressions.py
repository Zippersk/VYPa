from tests.testBase import TestBaseCases


class TestsArithmetic(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {

            print(1*2 + 1*3);
        }
    """

    STDOUT = "5"
