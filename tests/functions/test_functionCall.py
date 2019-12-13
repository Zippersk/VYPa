from tests.testBase import TestBaseCases


class TestsMultipleFunctionsCall(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        int GetFive(void) {
            int five;
            five = 5;
            return five;
        }

        int GetTen(void) {
            return 10;
        }

        void main(void) {
            int a;
            a = GetFive() + GetTen();
            print(a);
        }
    """

    STDOUT = "15"
