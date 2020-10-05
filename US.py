from project03 import indi_list,fam_list,calculateAge,splitBdate,isAlive


def US07(): #  US07 Less then 150 years old
    result= False  
    

    for i in (indi_list):
        if (calculateAge(splitBdate(i[3])) < 150):
            print("INDIVIDUAL: US07: "+" Less than 150 years old: Birth date "+ i[3])
            result = True
   
    return result


def US09(): #US09 Birth before death of parents
    result= False  
    print("US- 09 Birth before death of parents")
    for f in fam_list:
        for i in indi_list:
            if i[0] == f[1]:
               
                if (isAlive(i[4])) == True:
                    print("Child's Birth before death of parents")
                    result = True
    return result
            
def main()->None:
   
    US07()
    US09()

if __name__ == "__main__":
    main()

    
