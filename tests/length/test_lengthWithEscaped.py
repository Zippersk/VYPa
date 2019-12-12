from tests.testBase import TestBaseCases


class TestsEscapedLength(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            print(length("x\nz"));
        }
    """

    STDOUT = "3"
