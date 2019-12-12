from tests.testBase import TestBaseCases


class TestsLength(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            string b;
            b = "hello world!";
            print(length(b));
        }
    """

    STDOUT = "12"
