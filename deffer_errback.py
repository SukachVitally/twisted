__author__ = 'kent'

from twisted.internet.defer import Deferred
from twisted.python.failure import Failure


def myErrback(failure):
    print failure

d = Deferred()
d.addErrback(myErrback)
error = Failure(exc_value = "Triggering errback.")
d.errback(error)
