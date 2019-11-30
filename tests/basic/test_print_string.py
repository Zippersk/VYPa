from tests.testBase import TestBaseCases


class TestsPrintInteger(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            string b = "hello world!";
            print(b);
        }
    """

    STDOUT = "hello world!"
