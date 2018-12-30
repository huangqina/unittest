import requests
import json

a = { 'barcode':str(1231214564), 'cell_type':'poly','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':1.1,'ai_result': 0, 'ai_defects':{},'ai_time':1.1,'gui_result':0,'gui_defects':{},'gui_time':1}
a = [1.1,2.2]
b = json.dumps(a)

r = requests.post('http://192.168.2.10:5000/OK/find', b)

print(r)