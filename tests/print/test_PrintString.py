from tests.testBase import TestBaseCases


class TestsPrintString(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            string b;
            b = "hello world!";
            print(b);
        }
    """

    STDOUT = "hello world!"
