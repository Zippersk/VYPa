from tests.testBase import TestBaseCases


class TestsMultipleFunctionsCall(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        int sub(int a, int b) {
            return a -b;
        }

        void main(void) {
            print(sub(10,4));
        }
    """

    STDOUT = "6"
