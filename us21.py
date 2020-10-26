import datetime

def lName(str):
    last_name=''
    for i in str:
        if(i != '/'):
            last_name += i
    return last_name

def listFam():
    value = [0 for i in range(6)]
    value[5] = []
    return value

def listIndi():
    value = [0 for i in range(7)]
    value[5] = []
    return value

def getGenderID(indi_list, id):
    for i in indi_list:
        if(i[0] == id):
            return i[2]
            
def DateFormat(date):
    dates = date.split()
    if(dates[1] == 'JAN'): dates[1] = '01'
    if(dates[1] == 'FEB'): dates[1] = '02'
    if(dates[1] == 'MAR'): dates[1] = '03'
    if(dates[1] == 'APR'): dates[1] = '04'
    if(dates[1] == 'MAY'): dates[1] = '05'
    if(dates[1] == 'JUN'): dates[1] = '06'
    if(dates[1] == 'JUL'): dates[1] = '07'
    if(dates[1] == 'AUG'): dates[1] = '08'
    if(dates[1] == 'SEP'): dates[1] = '09'
    if(dates[1] == 'OCT'): dates[1] = '10'
    if(dates[1] == 'NOV'): dates[1] = '11'
    if(dates[1] == 'DEC'): dates[1] = '12'
    if(dates[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        dates[2] = '0' + dates[2]
    return (dates[0] + '-' + dates[1] + '-' + dates[2])

def fileParse(file_name):
    open_file = open(file_name,'r')
    indi = listIndi()
    fam = listFam()
    indi_list = []
    fam_list = []
    fams = 0
    indis = 0
    
    for line in open_file:
        str = line.split()
        if(str != []):
            if(str[0] == '0'):
                if(fams == 1):
                    fam_list.append(fam)
                    fam = listFam()
                    fams = 0
                if(indis == 1):
                    indi_list.append(indi)
                    indi = listIndi()
                    indis = 0
                if(str[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(str[2] == 'INDI'):
                        indis = 1
                        indi[0] = (str[1])
                    if(str[2] == 'FAM'):
                        fams = 1
                        fam[0] = (str[1])
            if(str[0] == '1'):
                if(str[1] == 'NAME'):
                    indi[1] = str[2] + " " + lName(str[3])
                if(str[1] == 'SEX'):
                    indi[2] = str[2]
                if(str[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = str[1]
                if(str[1] == 'FAMS'):
                    indi[5].append(str[2])
                if(str[1] == 'FAMC'):
                    indi[6] = str[2]
                if(str[1] == 'HUSB'):
                    fam[1] = str[2]
                if(str[1] == 'WIFE'):
                    fam[2] = str[2]
                if(str[1] == 'CHIL'):
                    fam[5].append(str[2])
            if(str[0] == '2'):
                if(str[1] == 'DATE'):
                    date = str[4] + " " + str[3] + " " + str[2]
                    if(date_id == 'BIRT'):
                        indi[3] = DateFormat(date)
                    if(date_id == 'DEAT'):
                        indi[4] = DateFormat(date)
                    if(date_id == 'MARR'):
                        fam[3] = DateFormat(date)
                    if(date_id == 'DIV'):
                        fam[4] = DateFormat(date)
    return indi_list, fam_list

def correctGenderForRole(indi_list, fam_list):
    genders = []
    for i in fam_list:
        if(getGenderID(indi_list, i[2]) != 'F'):
            genders.append(i[2])
            print(" Female individual has incorrect gender role ")
        if(getGenderID(indi_list, i[1]) != 'M'):
            genders.append(i[1])
            print(" Male individual has incorrect Gender role ")      
    if(len(genders) != 0):
        print(" Individual with incorrect gender role are present ")
    else:
        print(" No individual with incorrect gender roles ")


def main(file_name):

    indi_list, fam_list = fileParse(file_name)
    fam_list.sort()
    indi_list.sort()
    correctGenderForRole(indi_list, fam_list)

main('/Users/MSI/Desktop/Exam/Sem3/SSW555/project/Home_work5/project04_gedcom.ged')
