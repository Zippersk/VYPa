from tests.testBase import TestBaseCases


class TestsArithmetic(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            int a = 1;
            int b = 2;
            int c = 3;
            int d = 4;
            int e = 5;
            int f = 6;
            int g = 7;
            print(a+b+c+d+e+f+g);
        }
    """

    STDOUT = "28"
