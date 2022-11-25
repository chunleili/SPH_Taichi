import taichi as ti
ti.init()

@ti.data_oriented
class test_data_oriented():
    @ti.func
    def func1(self):
        print("I am func1")

    @ti.kernel
    def kernel(self):
        print("I am kernel")
        self.func1()

def test():
    a = test_data_oriented()
    a.kernel()

if __name__ == '__main__':
    test()