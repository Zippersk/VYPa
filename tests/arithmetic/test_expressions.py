from tests.testBase import TestBaseCases


class TestsArithmetic(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {

            print(30);
        }
    """

    STDOUT = "30"
