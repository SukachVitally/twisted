__author__ = 'kent'

from twisted.internet import protocol, reactor


class Echo(protocol.Protocol):

    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(8008, EchoFactory())
reactor.run()
