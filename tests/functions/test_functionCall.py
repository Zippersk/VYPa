from tests.testBase import TestBaseCases


class TestsMultipleFunctionsCall(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        int GetFive(void) {
            int five = 5;
            return five;
        }
        
        int GetTen(void) {
            return 10;
        }

        void main(void) {
            int a = 8 - GetFive() + GetTen() + 3 - 20;
            print(a);
        }
    """

    STDOUT = "-4"
