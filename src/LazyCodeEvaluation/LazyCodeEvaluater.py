# For some cases when we can not evaluate code directly we use LazyCodeEvalueter and evaluate all code at the end
# Example:
#    void main(void) {
#        int a = GetInt();
#    }
#
#    int GetInt(void) {
#        return 5;
#    }
#
# When int a = GetInt(); is called,
# we dont know yet GetInt's return type (we dont know that GetInt exists...)
# so we can not check types directly


class LazyCodeEvaluater:
    def __init__(self):
        self.lazy_code = []

    def add(self, lazy):
        self.lazy_code.append(lazy)

    def run(self):
        for lazy in self.lazy_code:
            lazy.run()

        self.lazy_code = []


LazyCode = LazyCodeEvaluater()
