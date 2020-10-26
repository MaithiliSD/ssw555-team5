## user story 03
## Maithili Deshmukh

# individual list
def individualList():
    output_list = [0 for i in range(7)]
    output_list[5] = []
    return output_list

def getLastName(str):
    temp_var=''
    for i in str:
        if(i != '/'):
            temp_var += i
    return temp_var

# us03
def birthBeforeDeath(list_individual):
    birthBeforeDeath_list= []
    for indi in list_individual:
        if(indi[4] != 0):
            if(indi[3] > indi[4]):
                birthBeforeDeath_list.append(indi[0])
                print("ERROR: INDIVIDUAL: US03: " + indi[0] + ": Died " + indi[4] + " before born " + indi[3])
    return birthBeforeDeath_list

# converting date into a standard format
def convertDateFormat(date):
    m = date.split()
    if(m[1] == 'JAN'): m[1] = '01';
    if(m[1] == 'FEB'): m[1] = '02';
    if(m[1] == 'MAR'): m[1] = '03';
    if(m[1] == 'APR'): m[1] = '04';
    if(m[1] == 'MAY'): m[1] = '05';
    if(m[1] == 'JUN'): m[1] = '06';
    if(m[1] == 'JUL'): m[1] = '07';
    if(m[1] == 'AUG'): m[1] = '08';
    if(m[1] == 'SEP'): m[1] = '09';
    if(m[1] == 'OCT'): m[1] = '10';
    if(m[1] == 'NOV'): m[1] = '11';
    if(m[1] == 'DEC'): m[1] = '12';
    if(m[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        m[2] = '0' + m[2]
    return (m[0] + '-' + m[1] + '-' + m[2])

# parsing the gedcom file
def gedcomParse(file_name):
    f = open(file_name,'r')
    list_individual = []
    indi_on = 0
    individual = individualList()
    for line in f:
        str = line.split()
        if(str != []):
            if(str[0] == '0'):
                if(indi_on == 1):
                    list_individual.append(individual)
                    individual = individualList()
                    indi_on = 0
                if(str[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(str[2] == 'INDI'):
                        indi_on = 1
                        individual[0] = (str[1])                       
            if(str[0] == '1'):
                if(str[1] == 'NAME'):
                    individual[1] = str[2] + " " + getLastName(str[3])
                if(str[1] == 'SEX'):
                    individual[2] = str[2]
                if(str[1] == 'FAMS'):
                    individual[5].append(str[2])
                if(str[1] == 'FAMC'):
                    individual[6] = str[2]
                if(str[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = str[1]                                
            if(str[0] == '2'):
                if(str[1] == 'DATE'):
                    date = str[4] + " " + str[3] + " " + str[2]
                    if(date_id == 'BIRT'):
                        individual[3] = convertDateFormat(date)
                    if(date_id == 'DEAT'):
                        individual[4] = convertDateFormat(date)
    return list_individual

def main(file_name):
    list_individual= gedcomParse(file_name)
    list_individual.sort()
    birthBeforeDeath(list_individual)

fileInput = 'project02_gedcom.ged'
main(fileInput)