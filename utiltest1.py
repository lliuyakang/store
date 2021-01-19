import unittest
from demo.calc import Calculator


class testCalc1(unittest.TestCase):
    def testSub(self):  # 测试方法必须是TEST开头
        c = Calculator()
        # 测试数据
        a = 19
        b = 10
        s = 9  # 期望结果
        sum = c.sub(a, b)  # 实际结果
        self.assertEquals(s, sum)

    def testSub1(self):  # 测试方法必须是TEST开头
        c = Calculator()
        # 测试数据
        a = -19
        b = -10
        s = -9  # 期望结果
        sum = c.sub(a, b)  # 实际结果
        self.assertEquals(s, sum)

    def testSub2(self):  # 测试方法必须是TEST开头
        c = Calculator()
        # 测试数据
        a = -19
        b = 10
        s = -29  # 期望结果
        sum = c.sub(a, b)  # 实际结果
        self.assertEquals(s, sum)

    def testSub3(self):  # 测试方法必须是TEST开头
        c = Calculator()
        # 测试数据
        a = 19
        b = -10
        s = 29  # 期望结果
        sum = c.sub(a, b)  # 实际结果
        self.assertEquals(s, sum)


''' def testSub(self):#测试方法必须是TEST开头
        c=Calculator()
        #测试数据
        a=19
        b=10
        s=9#期望结果
        sum=c.sub(a,b)#实际结果
        self.assertEquals(s,sum)

    def testMul(self):#测试方法必须是TEST开头
        c=Calculator()
        #测试数据
        a=19
        b=10
        s=190#期望结果
        sum=c.mul(a,b)#实际结果
        self.assertEquals(s,sum)

    def testDiv(self):#测试方法必须是TEST开头
        c=Calculator()
        #测试数据
        a=19
        b=10
        s=1.9#期望结果
        sum=c.div(a,b)#实际结果
        self.assertEquals(s,sum)
'''