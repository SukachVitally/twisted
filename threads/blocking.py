import time
from twisted.internet import reactor, threads
from twisted.internet.task import LoopingCall


def blockingApiCall(arg):
    time.sleep(2)
    return arg


def nonblockingCall(arg):
    print arg


def printResult(result):
    print result


def finish():
    reactor.stop()


d = threads.deferToThread(blockingApiCall, "Goose")
d.addCallback(printResult)
LoopingCall(nonblockingCall, "Duck").start(1)

reactor.callLater(10, finish)
reactor.run()