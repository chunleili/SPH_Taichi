class Base:
    def __init__(self) -> None:
        print("I am Base")
    def func(self):
        print('I am func in Base')

class Derived(Base):
    def __init__(self) -> None:
        print("I am Derived")
    def func(self):
        print('I am the func in Derived')
        super().func()

a = Derived()
print('-------调用--------')
a.func()