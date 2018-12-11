from HttpRequest import hr
from info import data_false
import requests
import json
hr = hr()

r = hr.insert('add/panel', data_false['error_1'])
#info = json.dumps(data_false['error_1'])
#req = requests.post('http://127.0.0.1:5000/add/panel', info)
print(r)