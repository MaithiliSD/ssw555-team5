# list of all valid tags
validTags =  ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

# function to concatenate agruments with length greater than 1
def concat(eachWord):
        eachWord[2] = eachWord[2] + " " + eachWord[3]
        del eachWord[3]
        if(len(eachWord) != 3):
            concat(eachWord)

# function to print data as per format specified in "Project 02"
def printData(fname):
    file = open(fname)
    splitInputLines = []
    inputLines = []
    
    for line in file:
        inputLines.append(line.strip())
        splitInputLines.append(line.strip().split(' '))
        
    for eachWord in splitInputLines:
        if(len(eachWord) > 3):
            concat(eachWord)
            
    for i, line in enumerate(splitInputLines):
        print('--> ' + inputLines[i])
        
        # for tag = 1 and tag = 2
        if splitInputLines[i][0] == '1' or splitInputLines[i][0] == '2':
            # if tags are valid
            if splitInputLines[i][1] in validTags:
                if len(splitInputLines[i]) > 2:
                    print('<--', end = " ")
                    print(splitInputLines[i][0] + '|' + splitInputLines[i][1] + '|Y|' + splitInputLines[i][2])
                elif len(splitInputLines[i]) <= 2:
                    print('<--', end = " ")
                    print(splitInputLines[i][0] + '|' + splitInputLines[i][1] + '|Y')
            # if tags are invalid
            else:
                if len(splitInputLines[i]) < 2:
                    print('<--', end = " ")
                    print(splitInputLines[i][0] + '|' + splitInputLines[i][1] + '|N|' + splitInputLines[i][2])
                else:
                    print('<--', end = " ")
                    print(splitInputLines[i][0] + '|' + splitInputLines[i][1] + '|N')
                    
        # for tag = 0
        if splitInputLines[i][0] == '0':
            if len(splitInputLines[i]) > 2:
                # if tags are valid
                # check for "FAM", "INDI" tags
                if splitInputLines[i][2] in validTags:
                    print('<--', end = " ")
                    print(splitInputLines[i][0] + '|' + splitInputLines[i][2]+ '|Y|' + splitInputLines[i][1])
                # check for "NOTE" tags
                elif splitInputLines[i][1] in validTags:
                    print('<--', end = " ")
                    print(splitInputLines[i][0] + '|' + splitInputLines[i][1]+ '|Y|' + splitInputLines[i][2])
                # if tags are invalid
                else:
                    print('<--', end = " ")
                    print(splitInputLines[i][0] + '|' + splitInputLines[i][1] + '|N|' + splitInputLines[i][2])
            elif len(splitInputLines[i]) <= 2:
                # if tags are valid
                # check for "TRLR" tags
                if splitInputLines[i][1] in validTags:
                    print('<--', end = " ")
                    print(splitInputLines[i][0] + '|' + splitInputLines[i][1] + '|Y')
                # if tags are invalid
                else:
                    print('<--', end = " ")
                    print(splitInputLines[i][0] + '|' + splitInputLines[i][1] + '|N')
    file.close()

# use "printData" function on a sample file
file = printData('test_GEDCOM_file.ged');