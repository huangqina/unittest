import requests
import json

class hr():
    host = 'http://127.0.0.1:5000/'


    def insert(self, c_url, data):
        try:
            url = self.host + c_url
            info = json.dumps(data)
            self.req = requests.post(url, info)
        except BaseException as e:
            print("插入失败",str(e))
        return self.req.text


    
    def get(self, c_url, data):
        try:
            url = self.host + c_url
            info = json.dumps(data)
            self.req = requests.get(url, info)
        except BaseException as e:
            print("查询失败", str(e))
        return self.req.text