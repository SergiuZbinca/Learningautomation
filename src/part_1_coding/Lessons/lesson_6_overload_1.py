class Student:
    def hello(self, name=None, email=None):
        if name is not None:
            print(f'Hello: {name}')
            if email is not None:
                print(f'Email: {email}')
        else:
            print('No value provided')


s = Student()
s.hello('Pop', 'pop@')

