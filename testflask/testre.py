from flask import Flask,abort
from flask import jsonify
#from flask import render_template
from flask import request
from flask_pymongo import PyMongo
#from flask_script import Manager
from con2 import connect2
import json
from flask_apscheduler import APScheduler
import logging
import sys

c = connect2()
#connect('ttt', host='mongodb://database:27017,database2:27017', replicaSet='rs', read_preference=ReadPreference.SECONDARY_PREFERRED)

#c = MongoClient('mongodb://0.0.0.0:27017')
#mongo = c.ttt
#conn = MongoReplicaSetClient("192.168.2.25:27017,192.168.2.25:27018", replicaset='rs')
db = c['tttt']
app = Flask(__name__)
user = db.user
log = db.user_log
a = user.find()
b = list(a)
b={'result':b}
print(b)