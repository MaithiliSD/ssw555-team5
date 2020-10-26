from project03 import indi_list,fam_list,calculate_age,split_date,is_alive,i,convert_na



def US24(indi_list): #US23 Unique families by spouses  
    name_list = []
    unique_spouses = []
    
    for i in indi_list:
        name_list.append(str(convert_na(i[5])))
        
    for x in name_list:
        if x not in unique_spouses and  x != "NA":
            unique_spouses.append(x)
    print(unique_spouses)


def main()->None:
   
    US24(indi_list)

if __name__ == "__main__":
    main()