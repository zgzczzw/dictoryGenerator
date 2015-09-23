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
import datetime

class Lauar:
    
    lunarInfo = [ 0x04bd8, 0x04ae0, 0x0a570, 0x054d5,

    0x0d260, 0x0d950, 0x16554, 0x056a0, 0x09ad0, 0x055d2, 0x04ae0,

    0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, 0x0b540, 0x0d6a0, 0x0ada2,

    0x095b0, 0x14977, 0x04970, 0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40,

    0x1ab54, 0x02b60, 0x09570, 0x052f2, 0x04970, 0x06566, 0x0d4a0,

    0x0ea50, 0x06e95, 0x05ad0, 0x02b60, 0x186e3, 0x092e0, 0x1c8d7,

    0x0c950, 0x0d4a0, 0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0,

    0x092d0, 0x0d2b2, 0x0a950, 0x0b557, 0x06ca0, 0x0b550, 0x15355,

    0x04da0, 0x0a5d0, 0x14573, 0x052d0, 0x0a9a8, 0x0e950, 0x06aa0,

    0x0aea6, 0x0ab50, 0x04b60, 0x0aae4, 0x0a570, 0x05260, 0x0f263,

    0x0d950, 0x05b57, 0x056a0, 0x096d0, 0x04dd5, 0x04ad0, 0x0a4d0,

    0x0d4d4, 0x0d250, 0x0d558, 0x0b540, 0x0b5a0, 0x195a6, 0x095b0,

    0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, 0x06a50, 0x06d40, 0x0af46,

    0x0ab60, 0x09570, 0x04af5, 0x04970, 0x064b0, 0x074a3, 0x0ea50,

    0x06b58, 0x055c0, 0x0ab60, 0x096d5, 0x092e0, 0x0c960, 0x0d954,

    0x0d4a0, 0x0da50, 0x07552, 0x056a0, 0x0abb7, 0x025d0, 0x092d0,

    0x0cab5, 0x0a950, 0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, 0x04ba0,

    0x0a5b0, 0x15176, 0x052b0, 0x0a930, 0x07954, 0x06aa0, 0x0ad50,

    0x05b52, 0x04b60, 0x0a6e6, 0x0a4e0, 0x0d260, 0x0ea65, 0x0d530,

    0x05aa0, 0x076a3, 0x096d0, 0x04bd7, 0x04ad0, 0x0a4d0, 0x1d0b6,

    0x0d250, 0x0d520, 0x0dd45, 0x0b5a0, 0x056d0, 0x055b2, 0x049b0,

    0x0a577, 0x0a4b0, 0x0aa50, 0x1b255, 0x06d20, 0x0ada0 ];
    
    year = 0;
    month = 0;
    day = 0;
    
    def leapDays(self, y):
        if (self.leapMonth(y) != 0):
#            print (str(y) + ":" + str((self.lunarInfo[y - 1900] & 0x10000) == 0 and 29 or 30))
            return ((self.lunarInfo[y - 1900] & 0x10000) == 0 and 29 or 30)
        else:
#            print str(y) + ":" + str(0)
            return (0);
    
    def lYearDays(self, y):
        sum = 348; #// 29*12
        i = 0x8000;
        while(i > 0x8):
            if (self.lunarInfo[y - 1900] & i) == 0:
                sum += 0
            else:
                sum += 1
            i >>= 1;

#        for (i = 0x8000; i > 0x8; i >>= 1)
#            sum += (lunarInfo[y - 1900] & i) == 0 ? 0 : 1; #// 大月+1�?
#        print str(y) + ":" + str(sum + self.leapDays(y))
        return (sum + self.leapDays(y)) #// +闰月的天�?
    
    
    #传回农历 y年闰哪个�?1-12 , 没闰传回 0
    def leapMonth(self, y):
        return (self.lunarInfo[y - 1900] & 0xf)
    
    def monthDays(self, y, m):
        return ((self.lunarInfo[y - 1900] & (0x10000 >> m)) == 0 and 29 or 30);

    
    def Lunar1(self, objDate): 
        global year
        date1 = datetime.datetime(1900, 1, 31)
       
#        // 1900 - 01 - 31是农�?900年正月初�?
        offset = (objDate - date1).days; 
#        // 天数(86400000=24 * 60 * 60 * 1000)
#        // 1899 - 12 - 21是农�?899年腊月甲子日
        monCyl = 14; 
#        // 1898 - 10 - 01是农历甲子月
#        // 得到年数
        for i in range(1900, 2050):
            if offset <= 0:
                break
            temp = self.lYearDays(i)
#            // 农历每年天数
            offset -= temp
            monCyl += 12

        if offset < 0:
            offset += temp
            i -= 1
            monCyl -= 12

        self.year = i
        leap = self.leapMonth(i) #// 闰哪个月
        isLeap = False;
        
        for i in range(1, 13):
            if (offset <= 0):
                break
            #// 闰月
            if (leap > 0 and i == (leap + 1) and isLeap == False):
                i -= 1
                isLeap = True
                temp = self.leapDays(self.year)
            else:
                temp = self.monthDays(self.year, i)
                
            #// 解除闰月
            if (isLeap == True and i == (leap + 1)):
                isLeap = False
            offset -= temp
            if (isLeap == False):
                monCyl += 1

        if (offset == 0 and leap > 0 and i == leap + 1):
            if (isLeap):
                isLeap = False
            else:
                isLeap = True
                i -= 1
                monCyl -= 1

        if (offset < 0):
            offset += temp
            i -= 1
            monCyl -= 1

        self.month = i #// 农历月份
        self.day = offset + 1 #// 农历天份
        
        
    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month
    
    def getDay(self):
        return self.day
        
        
    def getLunar(self, year, month, day):
        SY = int(year);
        SM = int(month);
        SD = int(day);
        sDObj = datetime.datetime(SY, SM, SD)
#        // 日期
        self.Lunar1(sDObj); #// 农历
#        s = str(self.getYear()) + "�?;
#        s += str(self.getMonth()) + "�?;
#        s += str(self.getDay()) + " ";

        return (self.getYear(), self.getMonth(), self.getDay());
    
#if __name__ == '__main__':
#    obj = Lauar();
#    print obj.getLunar("1992", "5", "27")
#    print obj.getLunar("2006", "8", "3")
#    print obj.getLunar("2008", "6", "8")
#    print obj.getLunar("2010", "8", "3")
#    print obj.getLunar("2010", "7", "18")

