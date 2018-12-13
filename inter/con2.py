from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
#client = MongoClient('localhost')
#db = client.ttt
#task = db.i
#print(task.count())
def connect2():
    fd = open("./config")
    line = fd.readline()
    while line:
        ip = list(line.strip().split(':'))
        count = 0
        client = MongoClient(ip[0], int(ip[1]), serverSelectionTimeoutMS=5)
        while True:
            try:
                client.admin.command("ping")
            except ConnectionFailure:
                count = count + 1
            else:
                return client
            if count == 5:
                line = fd.readline()
                break
connect2()