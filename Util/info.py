import time 
import random
barcode = random.randint(1,1000)
ai_d = {}
gui_d = {}
for k in ['cr','cs','bc','mr']:
    ai_d[k] = []
    for j in range(random.randint(0,50)):
        l = [random.randint(0,100),random.randint(0,100)]
        ai_d[k].append(l)
for k in ['cr','cs','bc','mr']:
    gui_d[k] = []
    for i in range(random.randint(0,50)):
        l = [random.randint(0,100),random.randint(0,100)]
        gui_d[k].append(l)
end = time.time()
info = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':ai_d,'ai_time':end,'gui_result':0,'gui_defects':gui_d,'gui_time':end}
barcode = random.randint(1,1000)
ai_d = {}
gui_d = {}
for k in ['cr','cs','bc','mr']:
    ai_d[k] = []
    for j in range(random.randint(0,50)):
        l = [random.randint(0,100),random.randint(0,100)]
        ai_d[k].append(l)
for k in ['cr','cs','bc','mr']:
    gui_d[k] = []
    for i in range(random.randint(0,50)):
        l = [random.randint(0,100),random.randint(0,100)]
        gui_d[k].append(l)
end = time.time()
info2 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'1','create_time':end,'ai_result': 0, 'ai_defects':{'cr':[]},'ai_time':end,'gui_result':0,'gui_defects':gui_d,'gui_time':end}
error_1 = {'barcode':123, 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':ai_d,'ai_time':end,'gui_result':0,'gui_defects':gui_d,'gui_time':end}
error_2 = {'barcode':str(barcode), 'cell_type':123,'cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':ai_d,'ai_time':end,'gui_result':0,'gui_defects':gui_d,'gui_time':end}
error_3 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'qwe', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':ai_d,'ai_time':end,'gui_result':0,'gui_defects':gui_d,'gui_time':end}
error_4 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':123,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':ai_d,'ai_time':end,'gui_result':0,'gui_defects':gui_d,'gui_time':end}
error_5 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':131,'create_time':end,'ai_result': 0, 'ai_defects':ai_d,'ai_time':end,'gui_result':0,'gui_defects':gui_d,'gui_time':end}
error_6 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':'2','ai_result': 0, 'ai_defects':ai_d,'ai_time':end,'gui_result':0,'gui_defects':gui_d,'gui_time':end}
error_7 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 4, 'ai_defects':ai_d,'ai_time':end,'gui_result':0,'gui_defects':gui_d,'gui_time':end}
error_8 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':0,'ai_time':end,'gui_result':0,'gui_defects':0,'gui_time':end}
error_9 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':ai_d,'ai_time':'end','gui_result':0,'gui_defects':gui_d,'gui_time':end}
error_10 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':ai_d,'ai_time':end,'gui_result':4,'gui_defects':gui_d,'gui_time':end}
error_11 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':ai_d,'ai_time':end,'gui_result':0,'gui_defects':0,'gui_time':end}
error_12 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':ai_d,'ai_time':end,'gui_result':0,'gui_defects':gui_d,'gui_time':'end'}
error_13 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':{'ct':[0]},'ai_time':end,'gui_result':0,'gui_defects':{'ct':[0]},'gui_time':'end'}

error_14 = {'barcode':str(barcode), 'cell_type':'mono','cell_size':'half', 'cell_amount':60,'el_no':'131','create_time':end,'ai_result': 0, 'ai_defects':ai_d,'ai_time':end,'gui_result':0,'gui_defects':{'ct':[0]},'gui_time':'end'}

data_true = {
        'info' : info,
        'info2' : info2,
}
data_false = {
        'error_1' : error_1,
        'error_2' : error_2,
        'error_3' : error_3,
        'error_4' : error_4,
        'error_5' : error_5,
        'error_6' : error_6,
        'error_7' : error_7,
        'error_8' : error_8,
        'error_9' : error_9,
        'error_10' : error_10,
        'error_11' : error_11,
        'error_12' : error_12,
        'error_13' : error_13,
        'error_14' : error_14,
}