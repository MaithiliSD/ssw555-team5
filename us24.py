from project03 import indi_list, convertToNA

def us24(indi_list): #US23 Unique families by spouses  
    name_list = []
    unique_spouses = []
    
    for i in indi_list:
        name_list.append(str(convertToNA(i[5])))
        
    for x in name_list:
        if x not in unique_spouses and  x != "NA":
            unique_spouses.append(x)
    print(unique_spouses)


def main()->None:
   us24(indi_list)

if __name__ == "__main__":
    main()