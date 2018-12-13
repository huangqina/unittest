from mongoengine import connect
from pymongo import ReadPreference

connect('ttt', host='mongodb://10.42.220.171:27017,10.42.133.88:27017', replicaSet='rs', read_preference=ReadPreference.SECONDARY_PREFERRED)