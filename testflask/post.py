import requests
import json

a = { 'barcode':str(1231214564), 'cell_type':'poly','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':1.1,'ai_result': 0, 'ai_defects':{},'ai_time':1.1,'gui_result':0,'gui_defects':{},'gui_time':1}
a = { 'barcode':'gfgfgfgfdg', 'cell_type':'poly', 'cell_amount':60,'el_no':'131','create_time':1.105577000451901,'ai_result': 0, 'ai_defects':{},'gui_result':0,'gui_defects':{},'display_mode':0,'module_no':1}
a = {'admin_name':'root','time':46.22545,'el_no':'no.3','cell_type':'mono','cell_amount':100,'display_mode':1,'module_no':1,'thresholds':{'a':5,'b':5,'c':3}}
a = {'admin_name':'root','time':46.22545,'el_no':'no.3','cell_type':'mono','cell_amount':100,'display_mode':1,'module_no':1,'thresholds':{'a':5,'b':5,'c':3},'user_name':'test','user_pw':"987654321"}
a = {"user_name":"user2","user_pw":"123456","time":1.1,"gui_no" : '2',"el_no":"line1"}
a = {'admin_name':'root','time':46.22545,"gui_no" : '2',"el_no":"line1",'changed_items':{'cell_type':'poly',"display_mode":2}}
a = {'admin_name':'root','time':46.22545,"gui_no" : '2',"el_no":"line1",'changed_items':{'manual_time':3,"gui_url":'192.168.1.1:1000'}}
#a = {"admin_name":"root","user_name":"test","user_pw":"987654321","admin_pw":"123456","time":1.1,'type':5}
b = json.dumps(a)

#r = requests.post('http://192.168.2.31:5000/panel/add', b)
#r = requests.post('http://192.168.2.10:5000/el/config/change', b)
r = requests.post('http://192.168.2.10:5000/gui/config/modify', b)
#r = requests.post('http://192.168.2.10:5000/el/config/display')
#r = requests.post('http://192.168.2.10:5000/gui/config/check',b)
#r = requests.post('http://192.168.2.10:5000/el/config/check',b)
#r = requests.post('http://192.168.2.31:5000/user/add',b)
#r = requests.post('http://192.168.2.10:5000/user/login/admin',b)
#r = requests.post('http://192.168.2.10:5000/user/password/change',b)
#r = requests.post('http://192.168.2.10:5000/user/show')
print(r.text)