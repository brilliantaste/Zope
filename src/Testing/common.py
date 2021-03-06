# Default test runner
import unittest
TestRunner = unittest.TextTestRunner


def debug():
    test_suite().debug()

def pdebug():
    import pdb
    pdb.run('debug()')

def test_suite():
    # The default test suite includes every subclass of TestCase in
    # the module, with 'test' as the test method prefix.
    ClassType = type(unittest.TestCase)
    tests = []
    for v in globals().values():
        if isinstance(v, ClassType) and issubclass(v, unittest.TestCase):
            tests.append(unittest.makeSuite(v))
    if len(tests) > 1:
        return unittest.TestSuite(tests)
    if len(tests) == 1:
        return tests[0]
    return

class Dummy:
    '''Utility class for quick & dirty instances'''
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __str__( self ):
        return 'Dummy(%s)' % `self.__dict__`

    __repr__ = __str__
