## user story 32
## Maithili Deshmukh

# importing packages
import datetime

dateList=[]

tempList = []

# individual list

def individualList():
    ilist = [0 for i in range(7)]
    ilist[5] = []
    return ilist

# family list
def familyList():
    flist = [0 for i in range(6)]
    flist[5] = []
    return flist

# get last name
def lastName(s):
    temp=''
    for i in s:
        if(i != '/'):
            temp += i
    return temp

# get name using id
def getNameByID(indiListData, id):
    for i in indiListData:
        if(i[0] == id):
            return i[1]
   
# get birth dates by id
def getBirthDateUsingID(indiListData, id):
    for i in indiListData:
        if(i[0] == id):
            return i[3]
			
# converting date into a standard format
def convertDateFormat(date):
    m = date.split()
    dt = datetime.datetime.strptime(m[1], "%b")
    m[1] = str(dt.month)
    return (m[0] + '-' + m[1] + '-' + m[2])

# us32
def listOfMultipleBirths(indiListData, famListData):
    for i in famListData:
        listOfMultipleBirth = []
        listOfBirthDates = []
        if(i[5] != []):
            for j in i[5]:
                listOfBirthDates.append(getBirthDateUsingID(indiListData, j))
            for j in set(listOfBirthDates):
                temp = []
                for k in i[5]:
                    if(j == getBirthDateUsingID(indiListData, k)):
                        temp.append(k)
                listOfMultipleBirth.append(temp)
        if(listOfMultipleBirth != []):
            for j in listOfMultipleBirth:
                if(len(j) > 1):
                    print('ERROR: INDIVIDUAL: US32: These individuals ' + i[0] + ' were born at the same time: ', j)
                    for k in j:
                        print(k + ': ' + getNameByID(indiListData, k))

# parsing the gedcom file 
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


def main(file_name):
    indiListData, famListData = gedcomParse(file_name)
    indiListData.sort()
    famListData.sort()
    listOfMultipleBirths(indiListData, famListData)
   
fileInput= 'project02_gedcom.ged'
main(fileInput)