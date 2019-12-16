from tests.testBase import TestBaseCases


class TestsCastingToString(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            int a = 5;
            string b = (string) a;
            print(b);
        }
    """

    STDOUT = "5"
