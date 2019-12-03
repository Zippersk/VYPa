from tests.testBase import TestBaseCases


class TestsPrintMultipleVariables(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            string b = "hello";
            print(b, "Ahoj");
        }
    """

    STDOUT = "helloAhoj"
