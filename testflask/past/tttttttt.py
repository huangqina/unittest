from flask import Flask,abort
import requests
app = Flask(__name__)
@app.route('/', methods=['GET'])
def show():
  #t = i['Defects'][0]['Defect']
  #r=requests.get("http://192.168.2.26:8091/hello")
  #return r.text
  return 'd',401
  return  '<p>ip:5000/user/add {"admin_name": str, "user_name": str, "user_pw": str, "time": float}</p><p>ip:5000/user/del {"admin_name": str, "user_name": str, "admin_pw": str, "time": float}</p><p>ip:5000/user/login {"type": int, "user_name": str, "user_pw": str, "time": float}</p><p>ip:5000/user/logout {"user_name": str, "time": float}</p><p>ip:5000/panel/add {"barcode": str, "cell_type": str, "cell_amount": int, "el_no": str, "display_mode": int, "module_no": int, "thresholds": dict, "create_time": float, "ai_result": int, "ai_defects": dict, "gui_result": int, "gui_defects": dict}</p><p>ip:5000/barcode/find {"barcode": str}    #post barcode</p><p>ip:5000/NG/find   [float, float]  #post time</p><p>ip:5000/OK/find  [float, float]     #post time</p><p>ip:5000/missrate/find   [float, float] #post time</p><p>ip:5000/overkillrate/find   [float, float]  #post time</p><p>ip:5000/defect/find   [float, float]  #post time</p>'
if __name__ == '__main__':

    # app.run(host = '0.0.0.0', por)t = 80, debug = True)
    app.run(host = '0.0.0.0', port = 5000, debug = True)