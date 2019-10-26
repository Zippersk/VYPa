import sys


class Printer:
    file = None

    def __init__(self, file):
        if file is not None:
            self.file = open(file, "w")

    def print(self, s):
        print(str(s), file=(self.file if self.file else sys.stdout))

    def error(self, s):
        print(str(s), file=sys.stderr)

    def close(self):
        if self.file:
            self.file.close()


Output = Printer(sys.argv[2] if len(sys.argv) > 2 else None)
