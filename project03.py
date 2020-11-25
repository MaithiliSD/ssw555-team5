## SSW-555
## Project 03
## Team 5

from prettytable import PrettyTable
from datetime import date
import datetime

def famList():
    flist = [0 for i in range(6)]
    flist[5] = []
    return flist

def indiList():
    return [0 for i in range(7)]

def lName(s):
    data=''
    for i in s:
        if(i != '/'):
            data += i
    return data

def getNameByID(indiList, ID):
    for i in indiList:
        if(i[0] == ID):
            return i[1]
def fileLength(f):
    for i,l in enumerate(f):
        pass
    return i+1

def gedcomRead(fileName):
    readFile = open(fileName,'r')
    f = fileLength(open(fileName))
    indiVal = 0
    famVal = 0
    indi_list = []
    fam_list = []
    indiData = indiList()
    famData = famList()
    for line in readFile:
        s = line.split()
        if(s != []):
            if(s[0] == '1'):
                if(s[1] == 'NAME'):
                    indiData[1] = s[2] + " " + lName(s[3])
                if(s[1] == 'SEX'):
                    indiData[2] = s[2]
                if(s[1] == 'BIRT'):
                    dateID = 'BIRT'
                if(s[1] == 'DEAT'):
                    dateID = 'DEAT'
                if(s[1] == 'MARR'):
                    dateID = 'MARR'
                if(s[1] == 'DIV'):
                    dateID = 'DIV'
                if(s[1] == 'FAMS'):
                    indiData[5] = s[2]
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
                    if(dateID == 'BIRT'):
                        indiData[3] = date
                    if(dateID == 'DEAT'):
                        indiData[4] = date
                    if(dateID == 'MARR'):
                        famData[3] = date
                    if(dateID == 'DIV'):
                        famData[4] = date
    
            if(s[0] == '0'):
                if(indiVal == 1):
                    indi_list.append(indiData)
                    indiData = indiList()
                    indiVal = 0
                if(famVal == 1):
                    fam_list.append(famData)
                    famData = famList()
                    famVal = 0
                if(s[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(s[2] == 'INDI'):
                        indiVal = 1
                        indiData[0] = (s[1])
                    if(s[2] == 'FAM'):
                        famVal = 1
                        famData[0] = (s[1])
    return indi_list, fam_list


def isAlive(deadVar):
    if(deadVar == 0):
        return True
    else :
        return False
    
def convertToNA(value):
    if(value == 0):
        return "NA"
    else:
        return value
    
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - int(birthDate[0]) - ((today.month, today.day) < (int(getMonth(birthDate[1])), int(birthDate[2]))) 
  
    return age

def splitBdate(dateStr):
    dateArr = dateStr.split(" ")
    return dateArr

def getMonth(monthStr):
    full_date = datetime.datetime.strptime(monthStr, "%b")
    return full_date.month

indi_list, fam_list = gedcomRead("project02_gedcom.ged")
indi_list.sort()
fam_list.sort()

# indiTable = PrettyTable(["ID", "Name" , "Sex", "Birth Date", "Age" ,  "Alive" , "Death Date" , "Spouse" , "Child"])

# #adding the details about individuals to the table
# for i in indi_list:
#     indiTable.add_row([i[0] , i[1], i[2] , i[3], calculateAge(splitBdate(i[3])) , isAlive(i[4]) , convertToNA(i[4]) , convertToNA(i[5]) , convertToNA(i[6])])

# print("Individials")
# print (indiTable)

# famTable = PrettyTable(["ID", "Married", "Divorced", "Husband ID", "Husband's Name" , "Wif ID" , "Wife's Name" , "Children"])
# #adding Husband's and wife's details to the table
# for i in fam_list:
#     famTable.add_row([i[0] , i[3] , convertToNA(i[4]) , i[1] , getNameByID(indi_list,i[1]) , i[2] , getNameByID(indi_list,i[2]) , i[5]])

# print("Families")
# print (famTable)
