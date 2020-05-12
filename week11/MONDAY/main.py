from metaclass_example import MyType


class Base(metaclass=MyType):
    pass


class Bear(Base):
    age = 5

    def eat(self):
        pass


class Panda(Bear):
    age = 25

    def eat(self):
        pass


p = Panda()
p.eat()
