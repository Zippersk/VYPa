from tests.testBase import TestBaseCases


class TestsUnicodeChars(TestBaseCases.TestBase):
    STDIN = ""
    source_code = """
        void main(void) {
            string b;
            b = "\\x01F601";
            print(b, " \\x00FDFD ", "\\x01F64F"); // escape
            print("🐬🐭🐮🐯🐰🐱🐲🐳🐴🐵🐶🐷🐸🐹🐺🐻🐼"); // printing utf-8 symbols
        }
    """

    STDOUT = "😁 ﷽ 🙏" + "🐬🐭🐮🐯🐰🐱🐲🐳🐴🐵🐶🐷🐸🐹🐺🐻🐼"
