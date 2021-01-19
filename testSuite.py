import unittest
import os
'''from demo.utiltest import testCalc
from demo.utiltest1 import testCalc1
from demo.utiltest2 import testCalc2
from demo.utiltest3 import testCalc3'''
from HTMLTestRunner import HTMLTestRunner
suite=unittest.TestSuite()#获取一个测试集
'''suite.addTest(testCalc("testAdd"))#添加一个测试用例
suite.addTest(testCalc("testAdd1"))#添加一个测试用例
suite.addTest(testCalc("testAdd2"))#添加一个测试用例
suite.addTest(testCalc("testAdd3"))#添加一个测试用例
suite.addTest(testCalc1("testSub"))#添加一个测试用例
suite.addTest(testCalc1("testSub1"))#添加一个测试用例
suite.addTest(testCalc1("testSub2"))#添加一个测试用例
suite.addTest(testCalc1("testSub3"))#添加一个测试用例'''
tests=unittest.defaultTestLoader.discover(os.getcwd(),"util*.py")
suite.addTest(tests)
#使用html运行器，生成以html结果报告
f=open("计算器测试报告.html","w+",encoding="utf-8")
runner=HTMLTestRunner.HTMLTestRunner(
    stream=f,
    verbosity=1,
    title="计算器的测试报告"
)
#使用运行器来运行测试集
runner.run(suite)