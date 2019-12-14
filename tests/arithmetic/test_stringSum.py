from tests.testBase import TestBaseCases


class StringSum(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            string b;
            b = "abcd" + "efghijk";
            print(b);
        }
    """

    STDOUT = "abcdefghijk"
