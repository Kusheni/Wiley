# -*- coding: utf-8 -*-


"""
Created on Tue Dec 17 11:48:24 2019

@author: ktharushik
"""
import unittest
from hello import HelloClass

class TestHello(unittest.TestCase):
    def test_sayhello(self):
        test=HelloClass()
    
        assert(test.sayhello()==True)

if __name__ == '__main__':
    unittest.main()

