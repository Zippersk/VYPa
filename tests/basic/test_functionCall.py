from tests.testBase import TestBaseCases


class TestsArithmetic(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        int GetInt(void) {
            return 5;
        }

        void main(void) {
            int a = GetInt() +20;
            print(a);
        }
    """

    STDOUT = "25"
