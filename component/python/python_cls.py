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


if __name__ == '__main__':
    Test.setMpp(123)
    Test.getMpp()