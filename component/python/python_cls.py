# coding=utf-8

class Test(object):
    mpp = None

    @classmethod
    def setMpp(cls, mpp):
        cls.mpp = mpp
        cls.df = 1

    @classmethod
    def getMpp(cls):
        print(cls.mpp)
        print(cls.df)

    @classmethod
    def getDf(cls):
        if cls.df:
            return cls.df
        return 2


def testTest():
    Test.setMpp(123)
    Test.getMpp()
    print(Test.getDf())


class BBase(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("__init__:", a, b)

    def __call__(self, a, b):
        self.a = a
        self.b = b
        print("__call__:", a, b)

    def __repr__(self):
        """
        __repr__ 的返回结果应更准确。怎么说，__repr__ 存在的目的在于调试，便于开发者使用。
        将 __repr__ 返回的方式直接复制到命令行上，是可以直接执行的。
        """
        return "__repr__:" + "%s %s" % (self.a, self.b)

    def __str__(self):
        """
        __str__ 的返回结果可读性强。也就是说，__str__ 的意义是得到便于人们阅读的信息
        """
        return "__str__:" + "%s %s" % (self.a, self.b)


if __name__ == '__main__':
    ab = BBase(1, 2)
    ab(3, 4)
    print(ab)