from HttpRequest import hr


hr = hr()
#def run():
    #for k in data.keys():
        #r = hr.insert('add/panel',data[k])
        #print(r)
def run(data):
    r = hr.insert('add/panel',data)
    return r

