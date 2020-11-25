## user story 02
## Maithili Deshmukh

import datetime
import unittest

# individual list
def individualList():
    indiList = [0 for i in range(7)]
    indiList[5] = []
    return indiList

	
# family list
def familyList():
    famList = [0 for i in range(6)]
    famList[5] = []
    return famList

#get last name
def lastName(s):
    temp=''
    for i in s:
        if(i != '/'):
            temp += i
    return temp


# get today's date
def currentDate():
    currDate = str(datetime.date.today())
    return currDate

# converting date into a standard format
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
		
def getMarriedDateUsingID(famListData, id):
    for i in famListData:
        if(i[0] == id):
            return i[3]

# us02			
def birthBeforeMarriage(indiListData, famListData):
    for indi in indiListData:
        birthDate = indi[3]
        if(indi[5] != []):
            for j in indi[5]:
                if(birthDate > getMarriedDateUsingID(famListData, j)):
                    dateList.append(indi[1])
                    print("ERROR: INDIVIDUAL: US02: " + indi[1] + " birth date " + indi[3] + " after marriage date " + getMarriedDateUsingID(famListData, j))
                    break
    return dateList
		
# parsing the gedcom file 
def gedcomParse(file_name):
    f = open(file_name,'r')
    indiValue = 0
    famValue = 0
    indindiListData = []
    famListData = []
    indiData = individualList()
    famData = familyList()
    for line in f:
        s = line.split()
        if(s != []):
            if(s[0] == '0'):
                if(indiValue == 1):
                    indindiListData.append(indiData)
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
    return indindiListData, famListData

class TestBirthBeforeMarriage(unittest.TestCase):
    
    def test_birth_marriage(self):
        indiListData, famListData = gedcomParse("project02_copy.ged")
        indiListData.sort()
        famListData.sort()
        outputList = birthBeforeMarriage(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertEqual(lenOutput, 0, "Should be 0")
        
    def test_birth_marriage_2(self):
        indiListData, famListData = gedcomParse("project02_copy.ged")
        indiListData.sort()
        famListData.sort()
        outputList = birthBeforeMarriage(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertTrue((lenOutput==0), "Should be True")
        
    def test_birth_marriage_3(self):
        indiListData, famListData = gedcomParse("project02_copy.ged")
        indiListData.sort()
        famListData.sort()
        outputList = birthBeforeMarriage(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertFalse((lenOutput>0), "Should be False")
        
    def test_birth_marriage_4(self):
        indiListData, famListData = gedcomParse("project02_copy.ged")
        indiListData.sort()
        famListData.sort()
        outputList = birthBeforeMarriage(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertIs(lenOutput, 0, "Should be 0")

def main(file_name):
    indiListData, famListData = gedcomParse(file_name)
    indiListData.sort()
    famListData.sort()
    birthBeforeMarriage(indiListData, famListData)
    # unittest.main()

   
fileInput = 'project02_gedcom.ged'
main(fileInput)