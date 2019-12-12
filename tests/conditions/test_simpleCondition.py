from tests.testBase import TestBaseCases


class BasicCondition(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
    void main(void) {
        if (0 < 0) {
            int a;
            a = 5;
            print("True");
            string b;
        }
        else
        {
            int skuska, raz,dva;
            print("False");
            raz = 42;
            print(raz);
        }
    }
    """

    STDOUT = "False42"
