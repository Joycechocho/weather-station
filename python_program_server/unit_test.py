#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 01:22:55 2017

@author: shuting
"""

import unittest
from PyQt5.QtCore import QCoreApplication
from authorize import Auth
import helper
import sys
#import Adafruit_DHT
import tinydb

# Unit test case for login
class TestCase01(unittest.TestCase):
    def test_Connect(self):
        qApp = QCoreApplication(sys.argv)
        self.assertTrue(helper.dbConnect())
    
    def test_Md5(self):
        self.assertEqual(helper.computeHash("password"),b'5f4dcc3b5aa765d61d8327deb882cf99')
    
    def test_Auth(self):
        qApp = QCoreApplication(sys.argv)
        helper.dbConnect()
        auth = Auth()
        self.assertEqual(auth.doLogin("eko", "password"), True)

# # Unit test case for sensor interaction
# class TestCase02(unittest.TestCase):
#     def test_SensorReading(self):
#         humidity, temperature = Adafruit_DHT.read(22, 4)
#         self.assertTrue(humidity is not None and temperature is not None)

# Unit test case for tinydb database utility
class TestCase03(unittest.TestCase):
    def test_Connect(self):
        testdb = helper.tinydb_create_db('test.json')
        self.assertEqual(helper.tinydb_write(testdb, [1,22,35]),1)



if __name__ == "__main__":
    unittest.main()
