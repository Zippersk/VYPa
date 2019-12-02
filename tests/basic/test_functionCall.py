from tests.testBase import TestBaseCases


class TestsArithmetic(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        int GetInt(void) {
            return 5;
        }

        void main(void) {
            int a = GetInt();
        }
    """

    STDOUT = "5"
