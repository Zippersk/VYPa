from tests.testBase import TestBaseCases


class TestsReadString(TestBaseCases.TestBase):
    STDIN = "hello world!"
    source_code = """
        void main(void) {
            string b;
            b = readString();
            print(b);
        }
    """

    STDOUT = "hello world!"
