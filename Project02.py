validTagsArr =  ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

def concat(eachWord):
        eachWord[2] = eachWord[2] + " " + eachWord[3]
        del eachWord[3]
        if(len(eachWord) != 3):
            concat(eachWord)
        
def loadFile(fname):
    file = open(fname)
    lineArr = []
    fullLines = []
    for line in file:
        fullLines.append(line.strip())
        lineArr.append(line.strip().split(' '))
    for eachWord in lineArr:
        if(len(eachWord) > 3):
            concat(eachWord)
    for i, line in enumerate(lineArr):
        print('--> ' + fullLines[i])
        if lineArr[i][0] == '1' or lineArr[i][0] == '2':
            if lineArr[i][1] in validTagsArr:
                if len(lineArr[i]) > 2:
                    print('<--', end = " ")
                    print(lineArr[i][0] + '|' + lineArr[i][1] + '|Y|' + lineArr[i][2])
                elif len(lineArr[i]) <= 2:
                    print('<--', end = " ")
                    print(lineArr[i][0] + '|' + lineArr[i][1] + '|Y')
            else:
                if len(lineArr[i]) < 2:
                    print('<--', end = " ")
                    print(lineArr[i][0] + '|' + lineArr[i][1] + '|N|' + lineArr[i][2])
                else:
                    print('<--', end = " ")
                    print(lineArr[i][0] + '|' + lineArr[i][1] + '|N')
        if lineArr[i][0] == '0':
            if len(lineArr[i]) > 2:
                if lineArr[i][2] in validTagsArr:
                    print('<--', end = " ")
                    print(lineArr[i][0] + '|' + lineArr[i][2]+ '|Y|' + lineArr[i][1])
                elif lineArr[i][1] in validTagsArr:
                    print('<--', end = " ")
                    print(lineArr[i][0] + '|' + lineArr[i][1]+ '|Y|' + lineArr[i][2])
                else:
                    print('<--', end = " ")
                    print(lineArr[i][0] + '|' + lineArr[i][1] + '|N|' + lineArr[i][2])
            elif len(lineArr[i]) <= 2:
                if lineArr[i][1] in validTagsArr:
                    print('<--', end = " ")
                    print(lineArr[i][0] + '|' + lineArr[i][1] + '|Y')
                else:
                    print('<--', end = " ")
                    print(lineArr[i][0] + '|' + lineArr[i][1] + '|N')
    file.close()
    
file = loadFile('test_GEDCOM_file.ged');