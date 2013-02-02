"""
Author: Ross Delinger (rossdylan)
Create Pipelines of Functions
"""
from functools import partial


def PipeLine(*funcs, **kwargs):
    """
    Given an arbitrary number of functions we create a pipeline where the output
    is piped between functions. you can also specify a tuple of arguments that
    should be passed to functions in the pipeline. The first arg is always the
    output of the previous function.
    """
    def wrapper(*data):
        if len(funcs) == 1:
            combinedArgs = data + kwargs.get(funcs[-1].__name__, tuple())
            return funcs[-1](combinedArgs)
        else:
            combinedArgs = kwargs.get(funcs[-1].__name__, tuple())
            if combinedArgs != ():
                del kwargs[funcs[-1].__name__]
            return funcs[-1](PipeLine(*funcs[:-1], **kwargs)(*data), *combinedArgs)
    return wrapper


def ReducePipeline(*funcs, **kwargs):
    """
    Given an arbitrary number of functions we create a pipeline where the output
    is piped between functions. You can also specify a tuple of arguments that
    should be passed to the functions in the pipeline. The first argument is
    always the output of the previous function. This version uses the reduce builtin
    instead of using recursion.
    """
    def accum(val, func):
        funcArgs = kwargs.get(func.__name__, tuple())
        if hasattr(val, "__call__"):
            return func(val(), *funcArgs)
        else:
            return func(val, *funcArgs)

    def wrapper(*data):
        newFuncs = (partial(funcs[0], *data),) + funcs[1:]
        return reduce(accum, newFuncs)
    return wrapper


class DotPipeline(object):
    """
    String together a series of functions using dot syntax.
    give DotPipeline's constructor the starting value, and the globals dict
    and then you can call string functions together
    addOne = lambda x: x+1
    subTwo = lambda x: x-2
    p = DotPipeline(1,globals())
    p.addOne.subTwo() -> 0
    """
    def __init__(self, val, topGlobals):
        self.val = val
        self.topGlobals = topGlobals
    def __getattr__(self, name):
        self.topGlobals.update(globals())
        return DotPipeline(self.topGlobals[name](self.val), self.topGlobals)
    def __call__(self):
        return self.val

def testPipelineWithArgs():
    """
    Test all the major functionality:
    multiple functions, initial arguments
    per function arguments stored in kwargs
    """
    def add1(input_):
        return input_ + 1

    def subX(input_, x):
        return input_ - x

    def stringify(input_):
        return str(input_)

    pipeline = PipeLine(
        add1,
        subX,
        stringify,
        subX=(2,),
        )
    print pipeline(10)
