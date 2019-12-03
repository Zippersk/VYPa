from tests.testBase import TestBaseCases


class TestsArithmetic(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            int a;
            a = 5 + 10 + 15;
            print(a);
        }
    """

    STDOUT = "30"
