from tests.testBase import TestBaseCases


class TestsParensArithmetic(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            print(2 * (4 + 2) * 3);
        }
    """

    STDOUT = "36"
