## user story 13
## Maithili Deshmukh

import datetime
import itertools as iter


dateList = []

# individual list
def individualList():
    individualList = [0 for i in range(7)]
    individualList[5] = []
    return individualList
	
# get last name
def lastName(s):
    data=''
    for i in s:
        if(i != '/'):
            data += i
    return data
	
# family list
def familyList():
    familyList = [0 for i in range(6)]
    familyList[5] = []
    return familyList
	
# get the birth date
def getBirthDateByID(indiListData, id):
    for i in indiListData:
        if(i[0] == id):
            return i[3]
				
# converting date into a standard format
def convertDateFormat(date):
    m = date.split()
    dt = datetime.datetime.strptime(m[1], "%b")
    m[1] = str(dt.month)
    return (m[0] + '-' + m[1] + '-' + m[2])

def getMonth(monthStr):
    full_date = datetime.datetime.strptime(monthStr, "%b")
    return full_date.month

# us13
def SiblingsSpacing(famListData, indiListData):
    for i in famListData:
        if(i[5] != [] and len(i[5]) > 1):
            siblingPairs = list(iter.combinations(i[5], 2))
            for j in siblingPairs:
                siblings_months = abs(difference_months(getBirthDateByID(indiListData, j[0]), getBirthDateByID(indiListData, j[1])))
                siblings_days = abs(difference_days(getBirthDateByID(indiListData, j[0]), getBirthDateByID(indiListData, j[1])))
                if(siblings_months <= 8 and siblings_days >= 3):
                    dateList.append(j)
                    print("ERROR: FAMILY: US13: Siblings " + j[0] + " and " + j[1] + " have their birth dates eight months apart")
                if(siblings_months == 0 and siblings_days >= 2):
                    dateList.append(j)
                    print("ERROR: FAMILY: US13: Siblings " + j[0] + " and " + j[1] + " have their birth days 2 or more days apart")
    return dateList

# calculate difference in months
def difference_months(dateData1, dateData2):
    temp1 = dateData1.split('-')
    temp2 = dateData2.split('-')
    ndateData1 = datetime.date(int(temp1[0]), int(getMonth(temp1[1])), int(temp1[2]))
    ndateData2 = datetime.date(int(temp2[0]), int(getMonth(temp2[1])), int(temp2[2]))
    return int((ndateData1 - ndateData2).days / 30.4)

# calculate difference in days
def difference_days(dateData1, dateData2):
    temp1 = dateData1.split('-')
    temp2 = dateData2.split('-')
    ndateData1 = datetime.date(int(temp1[0]), int(getMonth(temp1[1])), int(temp1[2]))
    ndateData2 = datetime.date(int(temp2[0]), int(getMonth(temp2[1])), int(temp2[2]))
    return abs(int((ndateData1 - ndateData2).days))

# parsing the gedcom file 
def gedcomParse(file_name):
    fileData = open(file_name,'r')
    indiValue = 0
    famValue = 0
    indiListData = []
    famListData = []
    indiData = individualList()
    famData = familyList()
    for line in fileData:
        inputData = line.split()
        if(inputData != []):
            if(inputData[0] == '0'):
                if(indiValue == 1):
                    indiListData.append(indiData)
                    indiData = individualList()
                    indiValue = 0
                if(famValue == 1):
                    famListData.append(famData)
                    famData = familyList()
                    famValue = 0
                if(inputData[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(inputData[2] == 'INDI'):
                        indiValue = 1
                        indiData[0] = (inputData[1])
                    if(inputData[2] == 'FAM'):
                        famValue = 1
                        famData[0] = (inputData[1])
            if(inputData[0] == '1'):
                if(inputData[1] == 'NAME'):
                    indiData[1] = inputData[2] + " " + lastName(inputData[3])
                if(inputData[1] == 'SEX'):
                    indiData[2] = inputData[2]
                if(inputData[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = inputData[1]
                if(inputData[1] == 'FAMS'):
                    indiData[5].append(inputData[2])
                if(inputData[1] == 'FAMC'):
                    indiData[6] = inputData[2]
                if(inputData[1] == 'HUSB'):
                    famData[1] = inputData[2]
                if(inputData[1] == 'WIFE'):
                    famData[2] = inputData[2]
                if(inputData[1] == 'CHIL'):
                    famData[5].append(inputData[2])
            if(inputData[0] == '2'):
                if(inputData[1] == 'DATE'):
                    date = inputData[4] + " " + inputData[3] + " " + inputData[2]
                    if(date_id == 'BIRT'):
                        indiData[3] = convertDateFormat(date)
                    if(date_id == 'DEAT'):
                        indiData[4] = convertDateFormat(date)
                    if(date_id == 'MARR'):
                        famData[3] = convertDateFormat(date)
                    if(date_id == 'DIV'):
                        famData[4] = convertDateFormat(date)
    return indiListData, famListData


def main(file_name):
    indiListData, famListData = gedcomParse(file_name)
    indiListData.sort()
    famListData.sort()
    SiblingsSpacing(famListData, indiListData)  

fileInput= 'project02_gedcom.ged'
main(fileInput)