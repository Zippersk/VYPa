from tests.testBase import TestBaseCases


class LogicalCondition(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
    int getFive(void) {
        return 12;
    }

    void main(void) {
        int a,b,c;
        a = 10;
        b = 10;
        c = 10;

        if (a < b && c < getFive()) {
            print("True");
        }
        else
        {
            print("False");
        }
    }
    """

    STDOUT = "False"
