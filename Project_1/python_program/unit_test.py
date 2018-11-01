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
import Adafruit_DHT

class TestCase01(unittest.TestCase):
    def testConnect(self):
        qApp = QCoreApplication(sys.argv)
        self.assertTrue(helper.dbConnect())
    
    def testMd5(self):
        self.assertEqual(helper.computeHash("password"),b'5f4dcc3b5aa765d61d8327deb882cf99')
    
    def testAuth(self):
        qApp = QCoreApplication(sys.argv)
        helper.dbConnect()
        auth = Auth()
        self.assertEqual(auth.doLogin("eko", "password"), True)
        
class TestCase02(unittest.TestCase):
    def testSensor(self):
        humidity, temperature = Adafruit_DHT.read(22, 4)
        self.assertTrue(humidity is not None and temperature is not None)
    
if __name__ == "__main__":
    unittest.main()
