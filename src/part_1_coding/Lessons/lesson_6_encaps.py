class Encapsulation:
    def public(self):
        print('Everyone can see me')

    def _protected(self):
        print('Acces provided limited to my kids')

    def __private(self):
        print("no one can't touch me")


class MiniEncapsulation(Encapsulation):
    def test(self):
        self.public()
        self._protected()


obj = MiniEncapsulation()
obj.test()
