# -*- coding:utf-8 -*-
'''
  Copyright (C) 2015 Eric Zhang, China
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as
  published by the Free Software Foundation, either version 3 of
  the License, or (at your option) any later version.
 
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Lesser General Public License for more details.
 
  You should have received a copy of the GNU Lesser General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
  Created on 2015-9-21
  @author: eric.zhang
  @contact: zgzczzw@163.com
  
'''
from permutation import Permutation
import variables
from lauar import Lauar 
import re
from const import const
    
def generateBirthDayList(yearStr, monthStr, dayStr):
    #以1949-10-01为例
    yearStr = str(yearStr)
    monthStr = "%02d" % (int(monthStr))
    dayStr = "%02d" % (int(dayStr))
    
    birthDayList = []
    birthDayList.append(yearStr)
    birthDayList.append(monthStr)
    birthDayList.append(dayStr)
    
    obj = Permutation()
    obj.words = birthDayList
    variables.birthday.extend(obj.permutationList())
    
    #只有月份和日期的全序列 10-01
    birthDayList.remove(yearStr)
    obj = Permutation()
    obj.words = birthDayList
    variables.birthday.extend(obj.permutationList())
    birthDayList.append(yearStr)
    
    #日期以单位数的全序列 1949-10-1
    if re.match(r"0\d", monthStr) or re.match(r"0\d", dayStr):
        birthDayList.remove(monthStr)
        birthDayList.append(str(int(monthStr)))
        birthDayList.remove(dayStr)
        birthDayList.append(str(int(dayStr)))
        obj.words = birthDayList
        variables.birthday.extend(obj.permutationList())
        
        #日期以单位数，没有年份的全序列 10-1
        birthDayList.remove(yearStr)
        obj = Permutation()
        obj.words = birthDayList
        variables.birthday.extend(obj.permutationList())
        birthDayList.append(yearStr)
        
    #年份是两位数的全序列 49-10-1
    if len(yearStr) == 4:
        sYear = yearStr[2:4]
        generateBirthDayList(sYear, monthStr, dayStr)
        
def afterGenerateNameList(f, l):
    nameList = []
    nameList.append(f)
    nameList.append(l)
    obj = Permutation()
    obj.words = nameList
    rst = obj.permutationList()
    if rst:
        variables.name.extend(rst)
        #字符串去重
        variables.name = list(set(variables.name))
        
def generateNameList(f, l):
    firstNameList = f.split(" ")
    lastNameList = l.split(" ")
    while '' in firstNameList:
        firstNameList.remove('')
    while '' in lastNameList:
        lastNameList.remove('')
        
    if(len(firstNameList) <= 0):
        firstNameList.append(" ")
        
    if(len(lastNameList) <= 0):
        lastNameList.append(" ")
        
    firstName = ""
    lastName = ""
    for s in firstNameList:
        firstName += s.lower()
    for s in lastNameList:
        lastName += s.lower()
    #姓，名全部小写
    afterGenerateNameList(firstName, lastName)
    #姓，名首字母大写
    afterGenerateNameList(firstName.capitalize(), lastName.capitalize())
    #名首字母大写
    afterGenerateNameList(firstName.capitalize(), lastName)
    #姓首字母大写
    afterGenerateNameList(firstName, lastName.capitalize())
    #只有名
    afterGenerateNameList(firstName, " ")
    afterGenerateNameList(firstName.capitalize(), " ")
    #只有姓
    afterGenerateNameList(" ", lastName)
    afterGenerateNameList(" ", lastName.capitalize())
    
    firstName = ""
    lastName = ""
    for s in firstNameList:
        firstName += s.upper()
    for s in lastNameList:
        lastName += s.upper()
    #姓，名全部大写
    afterGenerateNameList(firstName, lastName)
    
    #如果名和姓都只有一个字，那么所有单词首字母大写和只有一个首字母大写是同一种情况
    if len(firstNameList) > 1 or len(lastNameList) > 1:
        firstName = ""
        lastName = ""
        for s in firstNameList:
            firstName += s.capitalize()

        for s in lastNameList:
            lastName += s.capitalize()
        #姓，名所有单词首字母大写
        afterGenerateNameList(firstName, lastName)
        #只有名
        afterGenerateNameList(firstName, " ")
        #只有姓
        afterGenerateNameList(" ", lastName)
    
    #姓，名只有首字母
    firstName = ""
    lastName = ""
    for s in firstNameList:
        firstName += s[0].lower()
    if(len(lastNameList) > 0):
        for s in lastNameList:
            lastName += s[0].lower()
    else:
        lastName = " "
    afterGenerateNameList(firstName, lastName)
    afterGenerateNameList(firstName.capitalize(), lastName)
    afterGenerateNameList(firstName, lastName.capitalize())
    #只有名
    afterGenerateNameList(firstName, " ")
    afterGenerateNameList(firstName.capitalize(), " ")
    #只有姓
    afterGenerateNameList(" ", lastName)
    afterGenerateNameList(" ", lastName.capitalize())
    
    firstName = ""
    lastName = ""
    for s in firstNameList:
        firstName += s[0].upper()
    for s in lastNameList:
        lastName += s[0].upper()
    afterGenerateNameList(firstName, lastName)
    #只有名
    afterGenerateNameList(firstName, " ")
    #只有姓
    afterGenerateNameList(" ", lastName)

def generatePhoneList(p):
    p = str(p)
    variables.phoneNumer.append(p)
    variables.phoneNumer.append(p[-8:-4])
    variables.phoneNumer.append(p[-6:-2])
#    variables.phoneNumer.append(p[-2:])
    variables.phoneNumer.append(p[-4:])
    variables.phoneNumer.append(p[-6:])
    variables.phoneNumer.append(p[-8:])
    
    rp = list(p)
    rp = rp[::-1]
    n = 0
    s = ""
    while n < len(rp):
        s += rp[n]
        n += 1
    
    variables.phoneNumer.append(s[:4])
    variables.phoneNumer.append(s[2:6])
    variables.phoneNumer.append(s[4:8])
    variables.phoneNumer.append(s[:6])
    variables.phoneNumer.append(s[2:8])
#    variables.phoneNumer.append(s[-4:])
#    variables.phoneNumer.append(s[-6:])
#    variables.phoneNumer.append(s[-8:])
#    variables.phoneNumer.append(s[-8:-4])
#    variables.phoneNumer.append(s[-6:-2])

def generateNumberList(q):
    rst = []
    q = str(q)
    rst.append(q)
    rst.append(q[-4:])
    rst.append(q[-6:])
    rst.append(q[-8:])
    
    rq = list(q)
    rq = rq[::-1]
    n = 0
    s = ""
    while n < len(rq):
        s += rq[n]
        n += 1
    
    rst.append(s[:4])
    rst.append(s[:6])
    rst.append(s[:8])
    rst.append(s)
    return rst
    
    
def generateStringList(s):
    rst = []
    rst.append(s)
    rst.append(s.lower())
    rst.append(s.upper())
    rst.append(s.capitalize())
    return rst
    
def handleList(old_list):
    new_list = list(set(old_list))
    while '' in new_list:
        new_list.remove('')
    while ' ' in new_list:
        new_list.remove(' ')
    return new_list

def doGenerate():
    variables.name.append("")
    variables.birthday.append("")
    variables.extinfo.append("")
    variables.dict_max.append("")
    variables.tail.append("")
    variables.head.append("")
    variables.year.append("")
#    variables.lett.append("")
    variables.email.append("")
    variables.qq.append("")
    variables.phoneNumer.append("")
    
    f = open('./result.txt', 'w')
    for birstdayItem in variables.birthday:
        for nameItem in variables.name:
            for extinfoItem in variables.extinfo:
                for dictMaxItem in variables.dict_max:
                    for yearItem in variables.year:
                        for phoneItem in variables.phoneNumer:
                            for qqItem in variables.qq:
                                for emailItem in variables.email:
                                    obj = Permutation()
                                    obj.words = [birstdayItem, nameItem, extinfoItem, \
                                                 dictMaxItem, \
                                                 yearItem, phoneItem, qqItem, \
                                                 emailItem]
                                    obj.words = handleList(obj.words)
                                    rst = obj.permutationList()
                                    for s in rst:
                                        if len(s) < variables.minLen or len(s) > variables.maxLen:
                                            break
                                        for tailItem in variables.tail:
                                            for headItem in variables.head:
                                                s2 = headItem + s + tailItem
                                                if len(s2) >= variables.minLen and len(s2) <= variables.maxLen:
                                                    print s2
                                                    if not variables.isDebug:
                                                        f.write(s2);
                                                        f.write('\n')

    f.close()
    print "Done!"
    
    
if __name__ == '__main__':
    haveConfig = False
    birthdayStr = "" 
    fnStr = "" #first name of name
    lnStr = "" #last name of name
    fenStr = "" #first name of English name
    lenStr = "" #last name of English name
    nnStr = "" #nickname
    phoneStr = " " #phone number
    qqStr = " " #qq
    emailStr = " " #email
    extStr = " "
    extStrList = [] #ext info
    minLen = "";
    maxLen = "";
#=============================读取配置文件===========================================
    try:
        f = open('./config.txt', 'r')
        haveConfig = True
        birthdayStr = f.readline().strip('\n')
        fnStr = f.readline().strip('\n')
        lnStr = f.readline().strip('\n')
        fenStr = f.readline().strip('\n')
        lenStr = f.readline().strip('\n')
        nnStr = f.readline().strip('\n')
        phoneStr = f.readline().strip('\n')
        qqStr = f.readline().strip('\n')
        emailStr = f.readline().strip('\n')
        minLen = f.readline().strip('\n')
        maxLen = f.readline().strip('\n')
        extStr = f.readline().strip('\n')
        while extStr:
            extStrList.append(extStr)
            extStr = f.readline().strip('\n')
        f.close()
    except:
        haveConfig = False
        print "there is no config file found"
        
    if not haveConfig:
        while not re.match(r"[1,2]\d{3}-[0,1]\d{1}-[0,1,2,3]\d{1}", birthdayStr):
            birthdayStr = raw_input("Please enter birthday(YYYY-MM-DD):")
            
        fnStr = raw_input("Please enter name(first name):")
        
        lnStr = raw_input("Please enter name(last name):")
        
        fenStr = raw_input("Please enter English name(first name):")
        
        lenStr = raw_input("Please enter English name(last name):")
        
        nnStr = raw_input("Please enter nickname:")
        
        while not re.match(r"1\d{10}", phoneStr):
            phoneStr = raw_input("Please enter phone number:")
            
        emailStr = raw_input("Please enter email account:")
        
        while not re.match(r"\d+", qqStr):
            qqStr = raw_input("Please enter QQ number:")
            
        while extStr.lower() != "no" and extStr != '':
            extStr = raw_input("Please enter ext info (ext info or 'no'):")
            if(extStr.lower() != "no" and extStr != ''):
                extStrList.append(extStr)
            
        minLen = raw_input("Please enter min length of password:")
        
        maxLen = raw_input("Please enter max length of password:")
        
#===============================生产密码位数============================================
    try:
        variables.minLen = int(minLen)
    except:
        variables.minLen = const.MIN_LEN_PW
    
    try:
        variables.maxLen = int(maxLen)
    except:
        variables.maxLen = const.MAX_LEN_PW
        
    if(variables.maxLen < variables.minLen):
        tmp = variables.minLen
        variables.minLen = variables.maxLen
        variables.maxLen = tmp

#==============================输出信息===============================================
        
    print "BirthDay:" + birthdayStr 
    print "Name:" + fnStr + " " + lnStr
    print "English Name:" + fenStr + " " + lenStr
    print "Nickname:" + nnStr
    print "Phone Number:" + phoneStr
    print "QQ:" + qqStr
    print "Email:" + emailStr
    print "Ext Info:" + str(extStrList)
    print "Len of Password:" + str(variables.minLen) + "-" + str(variables.maxLen)
    raw_input("Confirm?(Press any key)")
    print "================Begin Generate Dictory================"
#==============================生日全序列============================================
   
    birthdayStr = birthdayStr.split("-");
    generateBirthDayList(birthdayStr[0], birthdayStr[1], birthdayStr[2])
    
    lauar = Lauar()
    lauar = lauar.getLunar(birthdayStr[0], birthdayStr[1], birthdayStr[2]);
    generateBirthDayList(str(lauar[0]) , "%02d" % (lauar[1]), "%02d" % (lauar[2]))
    variables.birthday = handleList(variables.birthday)
    if variables.isDebug:
        print variables.birthday
        
    
#===============================姓名全序列=============================================

    
    generateNameList(fnStr, lnStr)
    variables.name = handleList(variables.name)
    if variables.isDebug:
        print variables.name
    
#===============================英文名全序列============================================


    generateNameList(fenStr, lenStr)
    variables.name = handleList(variables.name)
    if variables.isDebug:
        print variables.name

#===============================昵称全序列=============================================

    
    generateNameList(nnStr, " ")
    
    #字符串去重
    variables.name = handleList(variables.name)
    if variables.isDebug:
        print variables.name

#===============================添加电话号码===========================================

    
    generatePhoneList(phoneStr)
    #字符串去重
    variables.phoneNumer = handleList(variables.phoneNumer)
    if variables.isDebug:
        print variables.phoneNumer

#===============================添加QQ号===========================================

    variables.qq.extend(generateNumberList(qqStr))
    #字符串去重
    variables.qq = handleList(variables.qq)
    if variables.isDebug:
        print variables.qq

#===============================添加Email号===========================================
    
    if(re.match(r"[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+", emailStr)):
        emailList = emailStr.split("@")
        emailStr = emailList[0]
        
    variables.email.extend(generateStringList(emailStr))
    #字符串去重
    variables.email = handleList(variables.email)
    if variables.isDebug:
        print variables.email
        
#===============================添加额外序列============================================

    if extStrList:
        for extStr in extStrList:
            if not(extStr == "no" or extStr == ''):
                variables.extinfo.extend(generateStringList(extStr))

        
    #字符串去重
    variables.extinfo = handleList(variables.extinfo)
    if variables.isDebug:
        print variables.extinfo
        

#===============================开始生成结果============================================
    
    doGenerate()
    

             
    
