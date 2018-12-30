import requests
import json

#a = {"user_name":"root","user_pw":"123456","time":1.1}
a = {"admin_name":"root","user_name":"huang","user_pw":"123456","time":1.1}
a = {"admin_name":"root","user_name":"huang","user_pw":"123456","admin_pw":"123456","time":1.1}
b = json.dumps(a)

r = requests.post("http://192.168.2.10:5000/test")
a = eval(r.text)
for i in a:
    print(i)


{"barcode":"str", "cell_type":"str","cell_size":"str","cell_amount":"int","el_no":"int","create_time":"float","ai_result":"int", "ai_defects":"dict","ai_time":"float","gui_result":"int","gui_defects":"dict","gui_time":"float"}