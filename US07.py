from project03 import indi_list,fam_list,calculateAge,splitBdate,isAlive


def US07(): #  US07 Less then 150 years old
    result= False  
    

    for i in (indi_list):
        if (calculateAge(splitBdate(i[3])) < 150):
            print("INDIVIDUAL: US07: "+" Less than 150 years old: Birth date "+ i[3])
            result = True
   
    return result

            
def main()->None:
   
    US07()

if __name__ == "__main__":
    main()

    
