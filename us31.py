## user story 31
## Maithili Deshmukh

# importing packages
import datetime 

file = open("project02_gedcom.ged","r")

# converting date into a standard format
def convertDateFormat(date):
    m = date.split()
    dt = datetime.datetime.strptime(m[1], "%b")
    m[1] = str(dt.month)
    return (m[0] + '-' + m[1] + '-' + m[2])

# get age by id
def getAgeByID(ind_list, id):
    d_flag = 0
    for i in ind_list:
        if(i[0] == id):
            b_date = i[3]
            m = b_date.split('-')
            b_year = int(m[0])
            b_month = int(m[1])
            b_date = int(m[2])
            if(i[4] != 0):
                d_date = i[4]
                d_flag = 1
    if(d_flag == 1):
        m = d_date.split('-')
        d_year = int(m[0])
        d_month = int(m[1])
        d_date = int(m[2])
        return d_year - b_year - ((d_month, d_date) < (b_month, b_date))
    c_date = getCurrDate().split('-')
    c_year = int(c_date[0])
    c_month = int(c_date[1])
    c_date = int(c_date[2])
    return c_year - b_year - ((c_month, c_date) < (b_month, b_date))

# us31
def listLivingSingle(list_indi):
    single = []
    for i in list_indi:
        if(i[4] == 0 and i[5] == []):
            single.append(i[0])
    for k in single:
        print("INDIVIDUAL: US31: " + k + ": " + getNameByID(list_indi, k) + " lives single.")
    print()

# get name by id
def getNameByID(list_indi, id):
    for i in list_indi:
        if(i[0] == id):
            return i[1]

# get curent date
def getCurrDate():
    c_date = str(datetime.date.today())
    return c_date

# family list
def fam_list():
    o_list = [0 for i in range(6)]
    o_list[5] = []
    return o_list

# individual list
def ind_list():
    o_list = [0 for i in range(7)]
    o_list[5] = []
    return o_list

# get last name
def getLastName(s):
    t=''
    for i in s:
        if(i != '/'):
            t += i
    return t

# parsing the gedcom file
def gedcomParse(file):
    indi_flag = 0
    fam_flag = 0
    list_indi = []
    list_fam = []
    indi = ind_list()
    fam = fam_list()
    for line in file:
        str = line.split()
        if(str != []):
            if(str[0] == '0'):
                if(indi_flag == 1):
                    list_indi.append(indi)
                    indi = ind_list()
                    indi_flag = 0
                if(fam_flag == 1):
                    list_fam.append(fam)
                    fam = fam_list()
                    fam_flag = 0
                if(str[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(str[2] == 'INDI'):
                        indi_flag = 1
                        indi[0] = (str[1])
                    if(str[2] == 'FAM'):
                        fam_flag = 1
                        fam[0] = (str[1])
            if(str[0] == '1'):
                if(str[1] == 'NAME'):
                    indi[1] = str[2] + " " + getLastName(str[3])
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
                        indi[3] = convertDateFormat(date)
                    if(date_id == 'DEAT'):
                        indi[4] = convertDateFormat(date)
                    if(date_id == 'MARR'):
                        fam[3] = convertDateFormat(date)
                    if(date_id == 'DIV'):
                        fam[4] = convertDateFormat(date)
    return list_indi, list_fam

list_indi, list_fam = gedcomParse(file)

listLivingSingle(list_indi)