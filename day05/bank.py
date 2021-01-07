import random
#银行库
bank={}
#银行名称
bank_name="中国工商银行昌平支行"

#欢迎模板
welcome='''
*****************************
*  中国工商银行账户管理系统   *
*****************************
*1.开户                     *
*2.存钱                     *
*3.取钱                     *
*4.转账                     *
*5.查询                     *
*6.退出                     *
*****************************
'''

#随机取号8位
def getRandom():
    li=['1','2','3','4','5','6','7','8','9','0']
    string=""
    for i in range(8):
        index=int(random.random()*len(li))#0-10随机获取角标
        string=string+li[index]
    return string

#银行开户逻辑
def bank_addUser(username,password,country,province,street,door,money,account):
    if len(bank)  >= 100:
        return 3
    elif account in bank:
        return 2
    else: # account : {username:username,password:password,.....}
        bank[account] = {
            "username":username,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":money,
            "bank_name":bank_name
        }
        return 1

#开户逻辑
def addUser():
    username=input("请输入您的姓名：")
    password=input("请输入您的密码：")
    print("接下来要输入您的地址信息：")
    country=input("国家：")
    province=input("省份：")
    street=input("街道：")
    door=input("门牌号：")
    money=int(input("请输入您的余额："))
    account=getRandom()#账号随机获取
    # 将上述数据传输给银行开户逻辑
    status = bank_addUser(username, password, country, province, street, door, money, account)
    if status == 3:
        print("对不起，本银行用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，您的个人信息已存在！请稍后再试！")
    elif status == 1:
        print("恭喜！开户成功！以下是您的开户信息：")
        info = '''
                ----------------开户信息----------------
                账号：{account},
                姓名：{username},
                密码：{password},
                地址信息：
                    国家：{country},
                    省份：{province},
                    街道：{street},
                    门牌号：{door}
                余额：{money},
                开户行名称：{bank_name}
                ----------------------------------------
            '''
        # 获取银行的个人信息
        user = bank[account]
        print(info.format(account=account,
                          username=user["username"],
                          password=user["password"],
                          country=user["country"],
                          province=user["province"],
                          street=user["street"],
                          door=user["door"],
                          money=user["money"],
                          bank_name=user["bank_name"]))
#存款函数
def putmoney():
    account = input("请输入您的账号：")
    if account in bank:
        putmoney = int(input("请输入您要存款的金额："))
        if putmoney >=0:
            bank[account]["money"] = bank[account]["money"]+putmoney
            print("存款后的余额为：", bank[account]["money"])

        else:
            print("您输入的存款金额不合法")
    else:
        print("账号错误！")

#取款函数
def getmoney():
    account = input("请输入您的账号：")
    password=input("请输入您的密码:")
    if account in bank and password in bank[account]["password"]:
        getmoney=int(input("请输入您所取款的金额："))
        if getmoney<=bank[account]["money"]:
            bank[account]["money"]=bank[account]["money"]-getmoney
            print("当前余额为：",bank[account]["money"])
            return 0
        elif getmoney>bank[account]["money"]:
            print("账户余额不足！")
            return 3
        else:
            print("输入非法！")
    elif account not in bank:
        print("账号不存在！")
        return 1
    elif password not in bank[account]["password"]:
        print("密码错误！")
        return 2

#银行转账函数
def bank_transfer(account1, account2,password, money):

    if account1 or account2 not in bank:
        return 1
    elif password not in bank[account2]["password"]:
        return 2
    elif money > bank[account2]["money"]:
        return 3
    else:
        bank[account2]["money"] = bank[account2]["money"] - money
        bank[account1]["money"] = bank[account1]["money"] + money
        return 0
#转账函数
def transfer():
    account1 = input("请输入转入账号：")
    account2 = input("请输入转出账号：")
    password = input("请输入转出账号的密码：")
    money = int(input("请输入转出的金额："))
    status1 = bank_transfer(account1, account2,password, money)
    if status1 == 3:
        print("转出的金额不足")
    elif status1 == 2:
        print("密码错误")
    elif status1 == 1:
        print("对不起，您输入的账号错误！")
    else:
        print("恭喜！转账成功！转账后转的账户的余额为：",bank[account1]["money"],"转出账户余额为：",bank[account2]["money"])


#查询函数
def query():
    account=input("请输入您的账号：")
    password=input("请输入您的密码：")
    info = '''
                ----------------开户信息----------------
                账号：{account}
                密码：{password}
                余额：{money}
                用户居住地址：{country},{province},{street},{door}
                开户行名称：{bank_name}
                ----------------------------------------
            '''
    if account not in bank:
        print("该用户不存在！")
    elif password not in bank[account]["password"]:
        print("密码错误！")
    else:
        bank1 = bank[account]
        print(info.format(account=account,
                          password=bank1["password"],
                          country=bank1["country"],
                          province=bank1["province"],
                          street=bank1["street"],
                          door=bank1["door"],
                          money=bank1["money"],
                          bank_name=bank1["bank_name"]))
#入口程序
while True:
    print(welcome)
    chose = input("请选择您要办的业务：")
    if chose =="1":
        addUser() #调用开户方法完成开户addUser()
    elif chose=="2":
        putmoney()
    elif chose=="3":
        getmoney()
    elif chose=="4":
        transfer()
    elif chose=="5":
        query()
    elif chose=="6":
        print("再见")
        break
    else:
        print("您选择的业务不存在！")

