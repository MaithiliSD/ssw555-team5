'''Finding the people marriage birth list before their death in GEDCOm file'''
import datetime


def l_name(str):
    '''Getting last name in file'''
    last_name = ''
    for i in str:
        if i != '/':
            last_name += i
    return last_name


def fams_list():
    '''Getting family list'''
    value = [0 for i in range(6)]
    value[5] = []
    return value


def indis_list():
    '''Getting individual list'''
    value = [0 for i in range(7)]
    value[5] = []
    return value


def date_format(date):
    '''Providing the correct date format to identify dates in file'''
    dates = date.split()
    if dates[1] == 'JAN':
        dates[1] = '01'
    if dates[1] == 'FEB':
        dates[1] = '02'
    if dates[1] == 'MAR':
        dates[1] = '03'
    if dates[1] == 'APR':
        dates[1] = '04'
    if dates[1] == 'MAY':
        dates[1] = '05'
    if dates[1] == 'JUN':
        dates[1] = '06'
    if dates[1] == 'JUL':
        dates[1] = '07'
    if dates[1] == 'AUG':
        dates[1] = '08'
    if dates[1] == 'SEP':
        dates[1] = '09'
    if dates[1] == 'OCT':
        dates[1] = '10'
    if dates[1] == 'NOV':
        dates[1] = '11'
    if dates[1] == 'DEC':
        dates[1] = '12'
    if dates[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        dates[2] = '0' + dates[2]
    return dates[0] + '-' + dates[1] + '-' + dates[2]


def fa_list(indi_list, id):
    '''Getting the death date from the file'''
    for i in indi_list:
        if i[0] == id:
            if i[4] != 0:
                return i[4]


def file_parse(file_name):
    '''Parsing the file'''
    open_file = open(file_name, 'r')
    indi = indis_list()
    fam = fams_list()
    indi_list = []
    fam_list = []
    fams = 0
    indis = 0
    for line in open_file:
        str = line.split()
        if str != []:
            if str[0] == '0':
                if fams == 1:
                    fam_list.append(fam)
                    fam = fams_list()
                    fams = 0
                if indis == 1:
                    indi_list.append(indi)
                    indi = indis_list()
                    indis = 0
                if str[1] in ['NOTE', 'HEAD', 'TRLR']:
                    pass
                else:
                    if str[2] == 'INDI':
                        indis = 1
                        indi[0] = (str[1])
                    if str[2] == 'FAM':
                        fams = 1
                        fam[0] = (str[1])
            if str[0] == '1':
                if str[1] == 'NAME':
                    indi[1] = str[2] + " " + l_name(str[3])
                if str[1] == 'SEX':
                    indi[2] = str[2]
                if str[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']:
                    date_id = str[1]
                if str[1] == 'FAMS':
                    indi[5].append(str[2])
                if str[1] == 'FAMC':
                    indi[6] = str[2]
                if str[1] == 'HUSB':
                    fam[1] = str[2]
                if str[1] == 'WIFE':
                    fam[2] = str[2]
                if str[1] == 'CHIL':
                    fam[5].append(str[2])
            if str[0] == '2':
                if str[1] == 'DATE':
                    date = str[4] + " " + str[3] + " " + str[2]
                    if date_id == 'BIRT':
                        indi[3] = date_format(date)
                    if date_id == 'DEAT':
                        indi[4] = date_format(date)
                    if date_id == 'MARR':
                        fam[3] = date_format(date)
                    if date_id == 'DIV':
                        fam[4] = date_format(date)
    return indi_list, fam_list

def get_spouse_family(indi_list, id):
    for i in indi_list:
        if(i[0] == id):
            return i[5]
        
def get_indi_name(indi_list, id):
    for i in indi_list:
        if(i[0] == id):
            return i[1]

def aunts_uncle(indi_list, fam_list):
    ua_list = []
    for i in fam_list:
        if(fa_list(fam_list, i[1]) == None):
            if(i[1] not in ua_list):
                ua_list.append(i[1])
        if(fa_list(indi_list, i[2]) == None):
            if(i[2] not in ua_list):
                ua_list.append(i[2])
    for i in ua_list:
        print("ID:" + i + " with name " + get_indi_name(indi_list, i) + " has uncle and aunt " + str(get_spouse_family(indi_list, i)))


def main(file_name):
    '''providing the file path'''
    indi_list, fam_list = file_parse(file_name)
    fam_list.sort()
    indi_list.sort()
    aunts_uncle(indi_list, fam_list)


main('/Sachin Paramesha/Sem3/SSW555/project/Home_work5/project04_gedcom copy.ged')
