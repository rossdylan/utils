from functools import partial
"""
Decorator which takes a int which is the maximum number of args the decorated function can take
"""
class curryable(object):
    def __init__(self, numArgs):
        self.__delattr__numArgs = numArgs
    def __call__(self, func):
        if self.__delattr__numArgs > 0:
            @curryable(self.__delattr__numArgs-1)
            def wrapper(*args, **kwargs):
                if len(args) < self.__delattr__numArgs:
                    return partial(func, *args)
                else:
                    return partial(func, *args)(**kwargs)
            return wrapper
        else:
            return func
