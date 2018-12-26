# -*- coding: utf-8 -*- 
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

#logging.basicConfig(filename="./log",level = logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
 
# 文件日志
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
 
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值
 
# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)
 
# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)
 
# 输出不同级别的log
logger.debug('this is debug info')
#logger.info('this is information')
#logger.warn('this is warning message')
#logger.error('this is error message')
#logger.fatal('this is fatal message, it is same as logger.critical')
#logger.critical('this is critical message')
 
# 2016-10-08 21:59:19,493 INFO    : this is information
# 2016-10-08 21:59:19,493 WARNING : this is warning message
# 2016-10-08 21:59:19,493 ERROR   : this is error message
# 2016-10-08 21:59:19,493 CRITICAL: this is fatal message, it is same as logger.critical
# 2016-10-08 21:59:19,493 CRITICAL: this is critical message
 
# 移除一些日志处理器
#logger.removeHandler(file_handler)

c = connect2()
#connect('ttt', host='mongodb://database:27017,database2:27017', replicaSet='rs', read_preference=ReadPreference.SECONDARY_PREFERRED)

#c = MongoClient('mongodb://0.0.0.0:27017')
#mongo = c.ttt
#conn = MongoReplicaSetClient("192.168.2.25:27017,192.168.2.25:27018", replicaset='rs')
db = c['tttt']
app = Flask(__name__)
def re():
    global c 
    c = connect2()
    global db
    db = c['tttt']
#app.config.update(
    #MONGO_URI='mongodb://127.0.0.1:27017/ttt',
    #MONGO_USERNAME='bjhee',
    #MONGO_PASSWORD='111111',
    #MONGO_REPLICA_SET='rs',
    #MONGO_READ_PREFERENCE='SECONDARY_PREFERRED',
    #SCHEDULER_API_ENABLED = True
#)
app.config['SCHEDULER_API_ENABLED'] = True
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.add_job(id = '1',func = re, trigger='interval', seconds=5)
scheduler.start()
#app.config['MONGO_DBNAME'] = 'ttt'
#app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017'  #如果部署在本上，其中ip地址可填127.0.0.1
#app.config['MONGO_DBNAME'] = 'ttt'
#mongo = PyMongo(app)
#manager = Manager(app)
if c.is_primary:
    db.panel.create_index([("Barcode", 1)])
    db.panel.ensure_index([("Barcode",1),("create_time",1)],unique=True)
    #db.panel.ensure_index([("Barcode", 1)])
#mongo.db.el
    db.panel_status.create_index([("time", 1)])
    db.panel_status.create_index([("Panel_ID", 1)]) 
    db.defect.create_index([("time", 1)])
    db.panel_defect.create_index([("Panel_ID", 1)])
    db.panel_defect.create_index([("Defect_ID", 1)])
@app.route('/', methods=['GET'])
def show():
  #t = i['Defects'][0]['Defect']
  return  '<p>ip:5000/add/panel</p><p>ip:5000/find/barcode     #post barcode</p><p>ip:5000/find/NG      #post time</p><p>ip:5000/find/OK       #post time</p><p>ip:5000/find/missrate     #post time</p><p>ip:5000/find/overkillrate     #post time</p><p>ip:5000/find/defect     #post time</p>'


@app.route('/add/panel',methods=['POST'])
def add():
    PANEL = db.panel
    EL = db.el
    PANEL_STATUS = db.panel_status 
    DEFECT = db.defect 
    PANEL_DEFECT = db.panel_defect 
    #AI = mongo.db.ai 
    data = request.data
    info = json.loads(data.decode('utf-8'))
    try:
        if not isinstance(info['barcode'],str):
            logger.error('barcode should be str')
            #raise TypeError("barcode should be str")
            return 'barcode should be str'
        if info['cell_type'] not in ['mono','poly']:
            #   raise TypeError('cell_type wrong')
            logger.error('cell_type wrong')
            return 'cell_type wrong'
        if info['cell_size'] not in ['half','full']:
            #raise TypeError('cell_size wrong')
            logger.error('cell_size wrong')
            return 'cell_size wrong'
        if info['cell_amount'] not in [60,72,120,144]:
            #raise TypeError('cell_amount wrong')
            logger.error('cell_amount wrong')
            return 'cell_amount wrong'
        if not isinstance(info['el_no'],str):
            #raise TypeError('el_no should be str')
            logger.error('el_no should be str')
            return 'el_no should be str'
        if not isinstance(info['create_time'],float):
            logger.error('create_time should be float')
            return 'create_time should be float'
        if info['ai_result'] not in [0,1,2]:
            #raise TypeError('ai_result should be 0 or 1')
            logger.error('ai_result should be 0 or 1 or 2')
            return 'ai_result should be 0 or 1 or 2'
        if not isinstance(info['ai_defects'], dict):
            #raise TypeError('ai_defects should be list')
            return 'ai_defects should be dict'
        if info['ai_defects']:
            for k in info['ai_defects'].keys():
                if k not in ['cr','cs','bc','mr']:
                    #raise TypeError('ai_defects wrong')
                    logger.error('ai_defects wrong')
                    return 'ai_defects wrong'
        if not isinstance(info['ai_time'],float):
            logger.error('ai_time should be float')
            return 'ai_time should be float'
        if info['gui_result'] not in [0,1]:
            #raise TypeError('gui_result should be 0 or 1')
            logger.error('gui_result should be 0 or 1')
            return 'gui_result should be 0 or 1'
        if not isinstance(info['gui_defects'], dict):
            #raise TypeError('gui_defects should be list')
            return 'gui_defects should be dict'
        if info['gui_defects']:
            for k in info['gui_defects'].keys():
                if k not in ['cr','cs','bc','mr']:
                    #raise TypeError('gui_defects wrong')
                    logger.error('gui_defects wrong')
                    return 'gui_defects wrong'     
        if not isinstance(info['gui_time'],float):
            logger.error('gui_defects wrong')
            return 'gui_defects wrong'
    except BaseException as e:
        logger.error('json error  '+str(e))
        return str('json error  '+str(e))
    try:
        panel_id = PANEL.insert({'Barcode' : info['barcode'], 'cell_type': info['cell_type'],'cell_size': info['cell_size'],'cell_amount': info['cell_amount'],'EL_no':info['el_no'],'create_time':info['create_time']})
    except BaseException as e:
        logger.error('barcode already exits')
        return 'barcode already exits'
    EL.insert({'EL_no': info['el_no']})
    #panel = PANEL.find_one({'_id': panel_id })
    PANEL_STATUS.insert({'Panel_ID':panel_id,'time':info['create_time'],'result':info['ai_result'],'by':'AI'})
    PANEL_STATUS.insert({'Panel_ID':panel_id,'time':info['create_time'],'result':info['gui_result'],'by':'OP'})
    if info['ai_defects']:
        for k in info['ai_defects'].keys():
            for v in info['ai_defects'][k]:
                if info['gui_defects'][k] and v in info['gui_defects'][k]:
                    defect_id = DEFECT.insert({'Type':k,'Position':v,'by':'AI','time':info['ai_time']})
                    PANEL_DEFECT.insert({'Panel_ID':panel_id,'Defect_ID':defect_id,'by':'AI','Status':'true'})
                    info['gui_defects'][k].remove(v)
                elif info['gui_defects'][k] and v not in info['gui_defects'][k]:
                    defect_id = DEFECT.insert({'Type':k,'Position':v,'by':'AI','time':info['ai_time']})
                    PANEL_DEFECT.insert({'Panel_ID':panel_id,'Defect_ID':defect_id,'by':'AI','Status':'false'})
    if info['gui_defects']:
        for k in info['gui_defects'].keys():
            if info['gui_defects'][k]:
                for v in info['gui_defects'][k]:
                    defect_id = DEFECT.insert({'Type':k,'Position':v,'by':'OP','time':info['gui_time']})
                    PANEL_DEFECT.insert({'Panel_ID':panel_id,'Defect_ID':defect_id,'by':'OP','Status':'true'})
    logger.info('add panel')
    return 'OK'
@app.route('/find/barcode', methods=['GET','POST'])
def find(): 
    #user = db.users 
    collection = db.panel
    data = request.data
    Barcode = json.loads(data.decode('utf-8'))
    Barcode = Barcode["Barcode"]
    #Barcode = request.args['Barcode']
    I = list(db.panel.find({"Barcode" : Barcode}).limit(1).sort([("_id" , -1)]))
    if I:
        ID = I[0]['_id']
    else: 
        ID = -1
    #username = user.find_one({"username":username}) 
    #if username: 
    #    return "你查找的用户名：" + username["username"] + " 密码是：" + username["password"] 
    #else: 
    #    return "你查找的用户并不存在!" 
    k = list(collection.aggregate([
    
    {'$match':{"_id":ID}},
    {'$project':{"_id":0}},
    {'$lookup': {'from':"panel_defect","pipeline":[
         
         {'$match':{ "Panel_ID": ID }},
         
         {'$lookup':{'from':"defect","localField":"Defect_ID",   "foreignField":"_id","as":"Defect"}
         },{'$project':
         {"_id":0,"Defect_ID":0,"Panel_ID":0}},{'$project':{"Defect":{"_id":0}}}],"as": "Defects"}}]))
   # a=str('ID:'+str(k[0]['ID'])+'  '+'Barcode:' + str(k[0]['Barcode'])+'  '+'type:'+str(k[0]['type'])+'  '+ 'size:'+ str(k[0]['size']) +'  '+'EL_no:'+ str(k[0]['EL_no']))

    #return str(a)+'\n'+str(k[0]['Defects'])
    #return str(k[0]['Defects'])
    return jsonify(k)
    # for i in k['Defects']:
          #  print(i['Defect'])
@app.route('/find/OK', methods=['GET','POST']) 
def findOK(): 
    data = request.data
    time = json.loads(data.decode('utf-8'))
    #start = float(request.args['start'])
    #end = float(request.args['end'])
    #start = str(time[0])
    #end = str(time[1])
    start = time[0]
    end = time[1]
    a=list(db.panel_status.aggregate([
    {"$match":{'time':{"$gt":start,"$lt":end}}},
    {"$group":{
        '_id' : "$result"
            ,
        'count':{"$sum":1}}}
    ]
    ))
    return jsonify(a)
   # '''
    #if a:
   #     return str('OK'+':'+str(a[0]['count'])+' '+'Defect'+':'+str(a[1]['count']))
    #else:
   #     return 'False'
   # '''
@app.route('/find/NG', methods=['GET','POST']) 
def findNG(): 
    data = request.data
    time = json.loads(data.decode('utf-8'))
    #start = float(request.args['start'])
    #end = float(request.args['end'])
    #start = str(time[0])
    #end = str(time[1])
    start = time[0]
    end = time[1]
    #start = float(request.args['start'])
    #end = float(request.args['end'])
    a=list(db.panel_status.aggregate([
    {"$match":{'time':{"$gt":start,"$lt":end}}},
    {
    "$group":{
        '_id' : "$result"
            ,
        'count':{"$sum":1}}}
    ]
    ))
    return jsonify(a)
    '''
    if a:
        return str('OK'+':'+str(a[0]['count'])+' '+'Defect'+':'+str(a[1]['count']))
    else:
        return 'False'
    '''
@app.route('/find/missrate', methods=['GET','POST']) 
def missrate(): 
    data = request.data
    time = json.loads(data.decode('utf-8'))
   # start = int(request.args['start'])
   # end = int(request.args['end'])
    start = time[0]
    end = time[1]
    k = list(db.defect.aggregate([
    
    {"$match":{'time':{"$gt":start,"$lt":end}}},
    {'$project':{"_id":1}},
    {'$lookup':{'from':'panel_defect',"localField":"_id",   "foreignField":"Defect_ID","as":"Defect"}
         },{'$project':{"Defect":
         {"_id":0,"Defect_ID":0,"Panel_ID":0}}},{'$project':{"_id":0}},{
    "$group":{
        '_id' : "$Defect.by"
            ,
        'count':{"$sum":1}}}]))
    #a=list(mongo.db.panel_defect.aggregate([
    #{'$match':{'time':{'$gt':start,'$lt':end}}},
    #{
    #'$group':{
    #    '_id' : "$by"
    #        ,
    #    'count':{'$sum':1}}}
    #]
    #))
    return jsonify(k)
    #return jsonify(a[0]['count']/(a[1]['count']+a[0]['count']))

@app.route('/find/overkillrate', methods=['GET','POST']) 
def overkillrate(): 
   # start = int(request.args['start'])
   # end = int(request.args['end'])
    #{'$match':{'time':{'$gt':start,'$lt':end}}},
    #start = float(request.args['start'])
    #end = float(request.args['end'])
    data = request.data
    time = json.loads(data.decode('utf-8'))
   # start = int(request.args['start'])
   # end = int(request.args['end'])
    start = time[0]
    end = time[1]
    k = list(db.defect.aggregate([
    
    {"$match":{'time':{"$gt":start,"$lt":end}}},
    {'$project':{"_id":1}},
    {'$lookup':{'from':'panel_defect',"localField":"_id",   "foreignField":"Defect_ID","as":"Defect"}
         },{'$project':{"Defect":
         {"_id":0,"Defect_ID":0,"Panel_ID":0}}},{'$project':{"_id":0}},{
    "$group":{
        '_id' : "$Defect.Status"
            ,
        'count':{"$sum":1}}}]))
    '''
    if a:
        return str(a)
    else:
        return 'None'
    '''
    return jsonify(k)
    #return str(a[1]['count']/(a[1]['count']+a[0]['count']))
@app.route('/find/defect', methods=['GET','POST']) 
def defecttime(): 
   # start = int(request.args['start'])
   # end = int(request.args['end'])
    data = request.data
    time = json.loads(data.decode('utf-8'))
   # start = int(request.args['start'])
   # end = int(request.args['end'])
    start = time[0]
    end = time[1]
    k = list(db.defect.aggregate([
    
    {"$match":{'time':{"$gt":start,"$lt":end}}},
    {'$project':{"_id":1}},
    {'$lookup':{'from':'panel_defect',"localField":"_id",   "foreignField":"Defect_ID","as":"Defect"}
         },{'$project':{"Defect":
         {"_id":0,"Defect_ID":0,"Panel_ID":0}}},{'$project':{"_id":0}},{
    "$group":{
        '_id' : "$Defect.Status"
            ,
        'count':{"$sum":1}}}]))
    '''
    if a:
        return str(a)
    else:
        return 'None'
    '''
    return jsonify(k)
if __name__ == '__main__':
    # app.run(host = '0.0.0.0', por)t = 80, debug = True)
    app.run(host = '0.0.0.0', port = 5000, debug = True)
