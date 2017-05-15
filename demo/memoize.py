# -*- coding: utf-8 -*-
class memoize(object):
    def __init__(self, func):
        print("__init__")
        self.__name__ = func.__name__
        self.__module__ = func.__module__
        self.__doc__ = func.__doc__
        self.func = func

    def __get__(self, obj, type=None):
        print("__get__")
        if obj is None:
            return self
        d, n = vars(obj), self.__name__
        if n not in d:
            value = self.func(obj)
            d[n] = value
        value = d[n]
        return value

class A(object):
    def __init__(self):
        self.a = 2

    @memoize
    def func(self):
        return 'foo'
    # func = memoize(func)
    a = 1

    @memoize
    def func2(self):
        return 'bar'

# class RevealAccess(object):
#     """A data descriptor that sets and returns values
#        normally and prints a message logging their access.
#     """
#     def __init__(self, initval=None, name='var'):
#         self.val = initval
#         self.name = name
#
#     def __get__(self, obj, objtype):
#         print('Retrieving', self.name)
#         return self.val
#
#     def __set__(self, obj, val):
#         print('Updating', self.name)
#         self.val = val
#
# class MyClass(object):
#     x = RevealAccess(10, 'var "x"')
#     y = 5

if __name__ == "__main__":
    a = A()
    print(a.a)
    print(a.func)
    print(a.func2)
    print(a.func)
    # m = MyClass()
    # print(m.x)
    # m.x = 20
    # print(m.x)
    # print(m.y)
