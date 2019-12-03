from tests.testBase import TestBaseCases


class TestsReadInteger(TestBaseCases.TestBase):
    STDIN = "4"
    source_code = """
        void main(void) {
            int b = readInt();
            print(b);
        }
    """

    STDOUT = "4"
