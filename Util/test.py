#!/usr/bin/env python
# -*- coding: utf-8 -*-

from info import data_false, data_true
import requests
import unittest
import time
import re
from run import run

def div(a, b):
    return a/b

class testclassone(unittest.TestCase):
    def setUp(self):
        pass
    #def test_raise_regexp(self):
        #self.assertRaisesRegexp(ZeroDivisionError, "division by zero", div, 2, 0)
    def test_true(self):
        #for k in data_true.keys():
            #run(k) # 执行脚本
        self.assertEqual(run(data_true['info2']), "OK")
        pass
        #pass       
    def test_false_barcode(self):
        #for k in data_false.keys():
        #self.assertRaisesRegexp(TypeError,"barcode should be str",run(data_false['error_1']))
        self.assertEqual(run(data_false['error_1']), "barcode should be str")
        pass
    def test_false_cell_type(self):
        self.assertEqual(run(data_false['error_2']), "cell_type wrong")
        pass
    def test_false_cell_size(self):
        self.assertEqual(run(data_false['error_3']), "cell_size wrong")
        pass
    def test_false_cell_amount(self):
        self.assertEqual(run(data_false['error_4']), "cell_amount wrong")
        pass
    def test_false_el_no(self):
        self.assertEqual(run(data_false['error_5']), "el_no should be str")
        pass
    def test_false_create_time(self):
        self.assertEqual(run(data_false['error_6']), "create_time should be float")
        pass
    def test_false_ai_result(self):
        self.assertEqual(run(data_false['error_7']), "ai_result should be 0 or 1 or 2")
        pass
    def test_false_ai_defects(self):
        self.assertEqual(run(data_false['error_8']), "ai_defects should be dict")
        pass
    def test_false_ai_time(self):
        self.assertEqual(run(data_false['error_9']), "ai_time should be float")
        pass
    def test_false_gui_result(self):
        self.assertEqual(run(data_false['error_10']), "gui_result should be 0 or 1")
        pass
    def test_false_gui_defects(self):
        self.assertEqual(run(data_false['error_11']), "gui_defects should be dict")
        pass
    def test_false_gui_time(self):
        self.assertEqual(run(data_false['error_12']), "gui_time should be float")
        pass
    def test_false_ai_type(self):
        self.assertEqual(run(data_false['error_13']), "ai_defects wrong")
        pass
    def test_false_gui_type(self):
        self.assertEqual(run(data_false['error_14']), "gui_defects wrong")
        pass
    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()