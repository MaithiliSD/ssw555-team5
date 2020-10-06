## user story 01
## Saish Sankhe

#importing packages
import datetime
import unittest

dateList=[]

#For the individual list

def individualList():
    ilist = [0 for i in range(7)]
    ilist[5] = []
    return ilist

	
#For the family list
def familyList():
    flist = [0 for i in range(6)]
    flist[5] = []
    return flist

#get last name
def lastName(s):
    temp=''
    for i in s:
        if(i != '/'):
            temp += i
    return temp


#get today's date
def currentDate():
    currDate = str(datetime.date.today())
    return currDate

#Converting date into a standard format
def convertDateFormat(date):
    temp = date.split()
    if(temp[1] == 'JAN'): temp[1] = '01';
    if(temp[1] == 'FEB'): temp[1] = '02';
    if(temp[1] == 'MAR'): temp[1] = '03';
    if(temp[1] == 'APR'): temp[1] = '04';
    if(temp[1] == 'MAY'): temp[1] = '05';
    if(temp[1] == 'JUN'): temp[1] = '06';
    if(temp[1] == 'JUL'): temp[1] = '07';
    if(temp[1] == 'AUG'): temp[1] = '08';
    if(temp[1] == 'SEP'): temp[1] = '09';
    if(temp[1] == 'OCT'): temp[1] = '10';
    if(temp[1] == 'NOV'): temp[1] = '11';
    if(temp[1] == 'DEC'): temp[1] = '12';
    if(temp[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        temp[2] = '0' + temp[2]
    return (temp[0] + '-' + temp[1] + '-' + temp[2])

dateList = []
todayDate = currentDate()

#User Story 1
def DatesBeforeCurrentDate(indiListData, famListData):
  
  #for individual
    for indi in indiListData:
        if(indi[3] > todayDate):
            dateList.append(indi[3])
            print("ERROR: INDIVIDUAL: US01: " + indi[0] + ": Birhtday " + indi[3] + " occurs in future.")
        if(indi[4] != 0):
            if(indi[4] > todayDate):
                dateList.append(indi[4])
                print("ERROR: INDIVIDUAL: US01: " + indi[0] + ": Death " + indi[4] + " occurs in future.")
	#for family
    for fam in famListData:
        if(fam[3] > todayDate):
            dateList.append(fam[3])
            print("ERROR: Family: US01: " + fam[0] + ": Marriage " + fam[3] + " occurs in future.")
        if(fam[4] != 0):
            if(fam[4] > todayDate):
                dateList.append(fam[4])
                print("ERROR: Family: US01: " + fam[0] + ": Divorce " + fam[4] + " occurs in future.")
    return dateList

#parsing the gedcom file 
def gedcomParse(file_name):
    f = open(file_name,'r')
    indiValue = 0
    famValue = 0
    indiListData = []
    famListData = []
    indiData = individualList()
    famData = familyList()
    for line in f:
        s = line.split()
        if(s != []):
            if(s[0] == '0'):
                if(indiValue == 1):
                    indiListData.append(indiData)
                    indiData = individualList()
                    indiValue = 0
                if(famValue == 1):
                    famListData.append(famData)
                    famData = familyList()
                    famValue = 0
                if(s[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(s[2] == 'INDI'):
                        indiValue = 1
                        indiData[0] = (s[1])
                    if(s[2] == 'FAM'):
                        famValue = 1
                        famData[0] = (s[1])
            if(s[0] == '1'):
                if(s[1] == 'NAME'):
                    indiData[1] = s[2] + " " + lastName(s[3])
                if(s[1] == 'SEX'):
                    indiData[2] = s[2]
                if(s[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = s[1]
                if(s[1] == 'FAMS'):
                    indiData[5].append(s[2])
                if(s[1] == 'FAMC'):
                    indiData[6] = s[2]
                if(s[1] == 'HUSB'):
                    famData[1] = s[2]
                if(s[1] == 'WIFE'):
                    famData[2] = s[2]
                if(s[1] == 'CHIL'):
                    famData[5].append(s[2])
            if(s[0] == '2'):
                if(s[1] == 'DATE'):
                    date = s[4] + " " + s[3] + " " + s[2]
                    if(date_id == 'BIRT'):
                        indiData[3] = convertDateFormat(date)
                    if(date_id == 'DEAT'):
                        indiData[4] = convertDateFormat(date)
                    if(date_id == 'MARR'):
                        famData[3] = convertDateFormat(date)
                    if(date_id == 'DIV'):
                        famData[4] = convertDateFormat(date)
    return indiListData, famListData
    

class TestDateBeforeCurrentDate(unittest.TestCase):
    
    def test_current_date(self):
        indiList, famList = gedcomParse("project02_gedcom.ged")
        dateList = DatesBeforeCurrentDate(indiList, famList)
        lenOfList = len(dateList)
        self.assertEqual(lenOfList, 0, "Should be 0")
        
    def test2_divorce_marriage(self):
        indiList, famList = gedcomParse("project02_gedcom.ged")
        dateList = DatesBeforeCurrentDate(indiList, famList)
        lenOfList = len(dateList)
        self.assertTrue((lenOfList==0), "Should be True")
        
    def test3_divorce_marriage(self):
        indiList, famList = gedcomParse("project02_gedcom.ged")
        dateList = DatesBeforeCurrentDate(indiList, famList)
        lenOfList = len(dateList)
        self.assertFalse((lenOfList>0), "Should be False")
        
    def test4_divorce_marriage(self):
        indiList, famList = gedcomParse("project02_gedcom.ged")
        dateList = DatesBeforeCurrentDate(indiList, famList)
        lenOfList = len(dateList)
        self.assertIs(lenOfList, 0, "Should be 0")
        
def main(file_name):
    # indiListData, famListData = gedcomParse(file_name)
    # indiListData.sort()
    # famListData.sort()
    # DatesBeforeCurrentDate(indiListData, famListData)
    unittest.main()

   
fileInput= 'project02_gedcom.ged'
main(fileInput)