from tests.testBase import TestBaseCases


class TestsExpressions(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
          int a,b,c,d,e,f,g,h;
          a = 1;
          b = 2;
          c = 3;
          d = 4;
          e = 5;
          f = 6;
          g = 7;
          h = 8;
          print(a*b + c*d < e*f + g*h);

        }
    """

    STDOUT = "1"
