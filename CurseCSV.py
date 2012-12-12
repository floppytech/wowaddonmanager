import csv

__author__ = 'Floppy'

class AddOnDB:

    db = {}
    instanced = False

    @staticmethod
    def insert(key, value):
        if key:
            AddOnDB.db[key] = value
        else : print "Empty key. Item not added."

    @staticmethod
    def value(key):
        try:
            return AddOnDB.db[key]
        except KeyError:
            return None

    @staticmethod
    def remove(key):
        try:
            AddOnDB.db.pop(key)
            return True
        except KeyError:
            return False

    @staticmethod
    def clear():
        AddOnDB.db.clear()

    @staticmethod
    def keys():
        return AddOnDB.db.keys()

    @staticmethod
    def values():
        return AddOnDB.db.values()

    @staticmethod
    def hasKey(key):
        try:
            AddOnDB.db[key]
            return True
        except KeyError:
            return False

    def __init__(self):
        if not AddOnDB.instanced:
            print "init DB called"
            AddOnDB.instanced = True
            dbReader = csv.reader(open('addonDB.csv', 'rb'))
            for row in dbReader:
                AddOnDB.db[row[0]] = row[1:]


class ClientData:

    data = {}
    instanced = False

    @staticmethod
    def insert(key, value):
        if key:
            ClientData.data[key] = value
        else : print "Empty key. Item not added."

    @staticmethod
    def value(key):
        try:
            return ClientData.data[key]
        except KeyError:
            return None

    @staticmethod
    def remove(key):
        try:
            ClientData.data.pop(key)
            return True
        except KeyError:
            return False

    @staticmethod
    def clear():
        ClientData.data.clear()

    @staticmethod
    def keys():
        return ClientData.data.keys()

    @staticmethod
    def values():
        return ClientData.data.values()

    @staticmethod
    def hasKey(key):
        try:
            ClientData.data[key]
            return True
        except KeyError:
            return False

    def __init__(self):
        if not ClientData.instanced:
            print "init data called"
            ClientData.instanced = True
            dataReader = csv.reader(open('clientData.csv', 'rb'))
            for row in dataReader:
                ClientData.data[row[0]] = row[1:]
