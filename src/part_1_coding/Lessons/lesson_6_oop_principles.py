from abc import ABC, abstractmethod


class MainModule(ABC):
    @abstractmethod
    def test_definition(self):
        raise NotImplemented

    @abstractmethod
    def test_execution(self):
        raise NotImplemented

    @abstractmethod
    def report(self):
        raise NotImplemented


class SecondModule(MainModule):
    def test_definition(self):
        print('Test definition result: ')

    def test_execution(self):
        print('Test execution result: ')

    def report(self):
        print('Test report result: ')

    def html_report(self):
        print('This is the second module')


class ThirdModule(MainModule):

    def test_definition(self):
        print('Define test number 2: ')

    def test_execution(self):
        print('Define test number 2 report: ')

    def report(self):
        print('Define report: ')


t_m = ThirdModule()

module = SecondModule()

for p in t_m, module:
    p.test_definition()
    p.test_execution()
    p.report()

# m = MainModule()
# m.test_definition()
