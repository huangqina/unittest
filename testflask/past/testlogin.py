import requests
import json

#a = {"user_name":"root","user_pw":"123456","time":1.1}
a = {"admin_name":"root","user_name":"huang","user_pw":"123456","time":1.1}
a = {"admin_name":"root","user_name":"esdrtgfsdf","user_pw":"123456","admin_pw":"123456","time":1.1}
b = json.dumps(a)

#r = requests.get("http://192.168.2.133:5000")
r = requests.post("http://192.168.2.10:5000/user/add",b)
print(r)
