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


if __name__ == '__main__':
    Test.setMpp(123)
    Test.getMpp()
    print(Test.getDf())