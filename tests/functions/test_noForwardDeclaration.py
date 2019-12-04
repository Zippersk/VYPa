from tests.testBase import TestBaseCases


class TestsNoForwardDeclaration(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            print(GetFive());
        }
    
    
        int GetFive(void) {
            return 5;
        }

    """

    STDOUT = "5"
