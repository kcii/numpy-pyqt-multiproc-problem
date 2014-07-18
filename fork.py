#!/usr/bin/env python

import PyQt4.QtCore # <- this line causes the error
from multiprocessing import Process

# a Process subclass
class PTask(Process):

    def __init__(self, func):
        Process.__init__(self)
        self._func = func

    def run(self):
        self._func()

def f():

    try:
        import numpy as np
        import numpy.linalg as npl

        for i in range(1000):
            print "i: ", i
            n = npl.pinv(np.random.rand(100,100))

        # Sometimes the segfault or malloc error doesn't occur 
        # on the first use of pinv.
        print "pinv success"
    except:
        # This just means the random matrix was not invertible
        # but that pinv executed correctly.
        print "exception success"


if __name__ == '__main__':
    p = PTask(f)
    print "start"
    p.start()
    print "wait"
    p.join()
    print "end"


    

