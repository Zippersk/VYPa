from tests.testBase import TestBaseCases


class TestsNoForwardDeclaration(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            int a = 8 - GetFive() + GetTen() + 3 - 20;
            print(a);
        }
    
    
        int GetFive(void) {
            return 5;
        }

        int GetTen(void) {
            return 10;
        }
    """

    STDOUT = "-4"
