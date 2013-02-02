"""
Some somewhat functional tools to make python more fun(ctional)
Author: Ross Delinger (rossdylan)
"""
from functools import partial


class curry(object):
    """
    Decorator which takes a int which is the maximum number of args the decorated function can take
    """
    def __init__(self, numArgs):
        self.__delattr__numArgs = numArgs

    def __call__(self, func):
        if self.__delattr__numArgs > 0:
            @curry(self.__delattr__numArgs-1)
            def wrapper(*args, **kwargs):
                if len(args) < self.__delattr__numArgs:
                    return partial(func, *args)
                else:
                    return partial(func, *args)(**kwargs)
            return wrapper
        else:
            return func


class __underscore_class__(object):
    """
    Object that matches anything
    """
    def __eq__(self, other):
        return True

""" Actually make _ an importable object """
_ = __underscore_class__()
