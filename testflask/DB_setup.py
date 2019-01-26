from con2 import connect2
c = connect2()
db = c['tttt']
try:
    db.permission.insert_one({
    "type" : "super admin",
    "level_mng" : 1,
    "user_mng" : 1,
    "display_mode" : 1,
    "ai_module" : 1,
    "threshold" : 1,
    "el_gui" : 1,
    "auto_manual" : 1,
    "shift_mng" : 1,
    "pic_upload" : 1})
    db.permission.insert_one({
    "type" : "YC admin",
    "level_mng" : 1,
    "user_mng" : 1,
    "display_mode" : 1,
    "ai_module" : 1,
    "threshold" : 1,
    "el_gui" : 1,
    "auto_manual" : 1,
    "shift_mng" : 1,
    "pic_upload" : 1})
    db.permission.insert_one({
    "type" : "quality admin",
    "level_mng" : 0,
    "user_mng" : 0,
    "display_mode" : 1,
    "ai_module" : 0,
    "threshold" : 1,
    "el_gui" : 0,
    "auto_manual" : 1,
    "shift_mng" : 0,
    "pic_upload" : 1})
    db.permission.insert_one({
    "type" : "production admin",
    "level_mng" : 0,
    "user_mng" : 1,
    "display_mode" : 1,
    "ai_module" : 1,
    "threshold" : 0,
    "el_gui" : 1,
    "auto_manual" : 1,
    "shift_mng" : 1,
    "pic_upload" : 1})
    db.permission.insert_one({
    "type" : "quality engineer",
    "level_mng" : 0,
    "user_mng" : 0,
    "display_mode" : 0,
    "ai_module" : 0,
    "threshold" : 0,
    "el_gui" : 0,
    "auto_manual" : 0,
    "shift_mng" : 0,
    "pic_upload" : 0
    })
    db.permission.insert_one({
    "type" : "production engineer",
    "level_mng" : 0,
    "user_mng" : 0,
    "display_mode" : 0,
    "ai_module" : 0,
    "threshold" : 0,
    "el_gui" : 0,
    "auto_manual" : 0,
    "shift_mng" : 0,
    "pic_upload" : 0 
    })
except BaseException:
    pass
while True:
    a = db.permission.aggregate([
    {"$group":{
        '_id' : "$type"}}
    ]
    )
    a = list(a)
    b = []
    for i in a:
        b.append(i["_id"])
    print("input [user, el_config, gui_config,exit]")
    name = input()
    dic = {}
    a = db.permission.aggregate([
    {"$group":{
        '_id' : "$type"}}
    ]
    )
    print(a)
    if name == "user":
        print("input name")
        dic['user_name'] = input()
        print("input password")
        dic['user_pw'] = input()
        print("input type in (%s)"%(', '.join(b)))
        dic['type'] = input()
        if dic['type']  not in b:
            print("type error")
            break
        dic['activate'] = 1
        db.user.insert_one(dic)
    if name == "el_config":    
        print("input el_no")
        dic['el_no'] = input()
        print("input pre_wd_url")
        dic['pre_wd_url'] = input()
        print("input cell_type")
        dic['cell_type'] = input()
        print("input cell_amount")
        dic['cell_amount'] = input()
        print("input cell_shape")
        dic['cell_shape'] = input()
        print("input display_mode")
        dic['display_mode'] = input()
        print("input gui_no")
        dic['gui_no'] = input()
        print("input gui_url")
        dic['gui_url'] = input()
        print("input threshold_module")
        dic['threshold_module'] = input()
        db.el_config.insert_one(dic)
    if name == "gui_config":    
        print("input gui_no")
        dic['gui_no'] = input()
        print("input mode")
        dic['mode'] = input()
        print("input auto_time")
        dic['auto_time'] = input()
        print("input manual_time")
        dic['manual_time'] = input()
        print("input el_limit")
        dic['el_limit'] = input()
        print("input gui_url")
        dic['gui_url'] = input()
        db.gui_setting.insert_one(dic)
    if name == "exit":
        break   
