from tests.testBase import TestBaseCases


class TestsCastingToString(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            print((string)5);
        }
    """

    STDOUT = "5"
