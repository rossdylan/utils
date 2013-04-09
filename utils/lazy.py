magic_methods = [
    '__abs__',
    '__add__',
    '__and__',
    '__call__',
    '__cmp__',
    '__coerce__',
    '__contains__',
    '__delitem__',
    '__delslice__',
    '__div__',
    '__divmod__',
    '__eq__',
    '__float__',
    '__floordiv__',
    '__ge__',
    '__getitem__',
    '__getslice__',
    '__gt__',
    '__hash__',
    '__hex__',
    '__iadd__',
    '__iand__',
    '__idiv__',
    '__idivmod__',
    '__ifloordiv__',
    '__ilshift__',
    '__imod__',
    '__imul__',
    '__int__',
    '__invert__',
    '__ior__',
    '__ipow__',
    '__irshift__',
    '__isub__',
    '__iter__',
    '__itruediv__',
    '__ixor__',
    '__le__',
    '__len__',
    '__long__',
    '__lshift__',
    '__lt__',
    '__mod__',
    '__mul__',
    '__ne__',
    '__neg__',
    '__oct__',
    '__or__',
    '__pos__',
    '__pow__',
    '__radd__',
    '__rand__',
    '__rdiv__',
    '__rdivmod__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__reversed__',
    '__rfloorfiv__',
    '__rlshift__',
    '__rmod__',
    '__rmul__',
    '__ror__',
    '__rpow__',
    '__rrshift__',
    '__rshift__',
    '__rsub__',
    '__rtruediv__',
    '__rxor__',
    '__setitem__',
    '__setslice__',
    '__sub__',
    '__truediv__',
    '__xor__',
    'next',
]

class Lazy(object):
    def __init__(self, func, *args, **kwargs):
        self.result = None
        self.func = func
        self.args = args
        self.kwargs = kwargs
        for method in magic_methods:
            setattr(self, method, self.lazy_wrap(method))

    def __getattr__(self, name):
        if self.result == None:
            self.result = self.func(*self.args, **self.kwargs)
        attr = getattr(self.result, name)
        if hasattr(attr, "__call__"):
            return self.lazy_wrap(name)
        else:
            return attr


    def lazy_wrap(self, name):
        def wrapper(*args, **kwargs):
            if self.result == None:
                self.result = self.func(*self.args, **self.kwargs)
            attr = getattr(self.result, name)
            return attr(*args, **kwargs)
        return wrapper
