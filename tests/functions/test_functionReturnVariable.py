from tests.testBase import TestBaseCases


class TestsFunctionReturnVariable(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        int GetFive(void) {
            return 5;
        }

        void main(void) {
            print(GetFive());
        }
    """

    STDOUT = "5"
