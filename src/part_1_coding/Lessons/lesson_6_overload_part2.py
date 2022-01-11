from overload import overload


class TestCase:
    @overload
    def run(self, a):
        return a
    @run.add
    def run(self, a, b):
        return a, b
    @run.add
    def run(self, a, b, c):
        return a, b, c


obj = TestCase()
output = obj.run(3)
print(output)

