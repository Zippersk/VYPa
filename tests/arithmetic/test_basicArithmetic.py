from tests.testBase import TestBaseCases


class TestsExpressions(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            print(1 && 1);
        }
    """

    STDOUT = "1"
