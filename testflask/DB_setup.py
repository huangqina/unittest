from con2 import connect2
c = connect2()
db = c['tttt']
while True:
    print("input [user, el_config, exit]")
    name = input()
    dic = {}
    if name == "user":
        print("input name")
        dic['name'] = input()
        print("input password")
        dic['pw'] = input()
        print("input type")
        dic['type'] = input()
        dic['activate'] = 1
        db.user.insert_one(dic)
    if name == "el_config":    
        print("input el_no")
        dic['el_no'] = input()
        print("input cell_type")
        dic['cell_type'] = input()
        print("input cell_amount")
        dic['cell_amount'] = input()
        print("input display_mode")
        dic['display_mode'] = input()
        print("input module_no")
        dic['module_no'] = input()
        db.el_config.insert_one(dic)
    if name == "exit":
        break   
