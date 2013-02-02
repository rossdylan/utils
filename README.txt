utils.fun
    @curry(int)
        A decorator that lets your functions support function currying by default with out have to explicitly 
        wrap them using funtools.partial
    _ (underscore)
        A class that equals whatever you compare it to
            _ == 3 -> True
            _ == "Test" -> True
            [_] == [1] -> True

utils.pipelines
    PipeLine(*funcs, **kwargs)
        Create a pipeline out of the given functions, and give them extra arguments using kwargs
    ReducePipeline(*funcs, **kwargs)
        Does the same thing as PipeLine only instead of building the pipeline recursively it does it using reduce()
