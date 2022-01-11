class RO:
    def capital(self):
        print('Bucharest')

    def language(self):
        print('Romana')


class DE:
    def capital(self):
        print('Berlin')

    def limba(self):
        print('Germana')


romania = RO()
germania = DE()

for i in romania, germania:
    i.capital()
    i.language()
