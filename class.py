import abc

class Person:
    kind = "human"

    def __init__(self, name):
        self.name = name
        print(self.name)
    
    def say(self):
        print('Hello, I am {}'.format(self.name))

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind
    
    def __del__(self):
        print('del')

class Man(Person):
    def __init__(self, name):
        super().__init__(name)
        
        print('man is created')
    
    def say(self):
        print('I am Man')

print(Person.what_is_your_kind())
man = Man('Bob')
man.say()