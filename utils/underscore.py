"""
Author: Ross Delinger (rossdylan)
Really useless class that just makes _ equal whatever you throw at it
usage:
    from underscore import _
    if [_,_] == [1,"thing"]:
        print "Anything goes!"
    else:
        print "Apprently this doesn't work"
"""


class __underscore_class__(object):
    """
    Object that matches anything
    """
    def __eq__(self, other):
        return True

""" Actually make _ an importable object """
_ = __underscore_class__()
