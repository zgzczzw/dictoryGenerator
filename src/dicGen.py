# -*- coding:utf-8 -*-
'''
    Created on 2015-9-22
    
    @author: eric.zhang
'''
from permutation import Permutation
import variables
from lauar import Lauar 
import re
    
def generateBirthDayList(year, month, day):
    #以1949-10-01为例
    year = str(year)
    month = "%02d" % (int(month))
    day = "%02d" % (int(day))
    
    birthDayList = []
    birthDayList.append(year)
    birthDayList.append(month)
    birthDayList.append(day)
    
    obj = Permutation()
    obj.words = birthDayList
    variables.birthday.extend(obj.permutationList())
    
    #只有月份和日期的全序列 10-01
    birthDayList.remove(year)
    obj = Permutation()
    obj.words = birthDayList
    variables.birthday.extend(obj.permutationList())
    birthDayList.append(year)
    
    #日期以单位数的全序列 1949-10-1
    if re.match(r"0\d", month) or re.match(r"0\d", day):
        birthDayList.remove(month)
        birthDayList.append(str(int(month)))
        birthDayList.remove(day)
        birthDayList.append(str(int(day)))
        obj.words = birthDayList
        variables.birthday.extend(obj.permutationList())
        
        #日期以单位数，没有年份的全序列 10-1
        birthDayList.remove(year)
        obj = Permutation()
        obj.words = birthDayList
        variables.birthday.extend(obj.permutationList())
        birthDayList.append(year)
        
    #年份是两位数的全序列 49-10-1
    if len(year) == 4:
        sYear = year[2:4]
        generateBirthDayList(sYear, month, day)
        
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
    
    
if __name__ == '__main__':
    
#==============================生日全序列============================================

#    birthday = ""
#    while not re.match(r"[1,2]\d{3}-[0,1]\d{1}-[0,1,2,3]\d{1}", birthday):
#        birthday = raw_input("Please enter birthday(YYYY-MM-DD):")
#    
#    birthday = birthday.split("-");
#    generateBirthDayList(birthday[0], birthday[1], birthday[2])
#    
#    lauar = Lauar()
#    lauar = lauar.getLunar(birthday[0], birthday[1], birthday[2]);
#    generateBirthDayList(str(lauar[0]) , "%02d" % (lauar[1]), "%02d" % (lauar[2]))
#    variables.birthday = handleList(variables.birthday)
#    if variables.isDebug:
#        print variables.birthday
    
#===============================姓名全序列=============================================

#    f = raw_input("Please enter name(first name):")
#    l = raw_input("Please enter name(last name):")
#    generateNameList(f, l)
#    variables.name = handleList(variables.name)
#    if variables.isDebug:
#        print variables.name
    
#===============================英文名全序列============================================

#    f = raw_input("Please enter English name(first name):")
#    l = raw_input("Please enter English name(last name):")
#    generateNameList(f, l)
#    variables.name = handleList(variables.name)
#    if variables.isDebug:
#        print variables.name

#===============================昵称全序列=============================================

#    f = raw_input("Please enter nickname:")
#    generateNameList(f, " ")
#    
#    #字符串去重
#    variables.name = handleList(variables.name)
#    if variables.isDebug:
#        print variables.name

#===============================添加额外序列============================================
    ext = " ";
    while ext.lower() != "no" and ext != '':
        ext = raw_input("Please enter ext info (ext info or 'no'):")
        if not(ext == "no" or ext == ''):
            variables.extinfo.extend(generateStringList(ext))
        
    #字符串去重
    variables.extinfo = handleList(variables.extinfo)
    if variables.isDebug:
        print variables.extinfo

#===============================开始生成结果============================================
#    variables.name.append("")
#    variables.birthday.append("")
#    variables.extinfo.append("")
#    variables.dict_max.append("")
#    variables.tail.append("")
#    variables.head.append("")
#    variables.year.append("")
##    variables.lett.append("")
#    
#    f = open('./result.txt', 'w')
#    for s1 in variables.birthday:
#        for s2 in variables.name:
#            for s3 in variables.extinfo:
#                for s4 in variables.dict_max:
#                    for s5 in variables.tail:
#                        for s6 in variables.head:
#                            for s7 in variables.year:
#                                obj = Permutation()
#                                obj.words = [s1, s2, s3, s4, s5, s6, s7]
#                                obj.words = handleList(obj.words)
#                                rst = obj.permutationList()
#                                for s in rst:
#                                    print s
#                                    if not variables.isDebug:
#                                        f.write(s);
#                                        f.write('\n')
#    f.close()
#    print "Done!"
             
    
