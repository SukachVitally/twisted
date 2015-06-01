from twisted.internet import reactor
from twisted.enterprise import adbapi
import hashlib


dbpool = adbapi.ConnectionPool("sqlite3", "users.db", check_same_thread=False)


def _createUsersTable(transaction, users):
    transaction.execute("CREATE TABLE users (username TEXT, password TEXT)")
    for name, password in users:
        transaction.execute(
            "INSERT INTO users (username, password) VALUES(?, ?)",
            (name, hashlib.md5(password).hexdigest()))


def createUsersTable(users):
    return dbpool.runInteraction(_createUsersTable, users)


def finish():
    dbpool.close()
    reactor.stop()

users = [("user", "321"), ("kate", "123")]


createUsersTable(users)
reactor.callLater(1, finish)
reactor.run()