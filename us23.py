from project03 import indi_list

def us23(indi_list): #US23 Unique name and birth date
    birth_list = []
    name_list = []
    unique_names = []
    unique_birth = []
    for i in indi_list:
        birth_list.append(str(i[3]))
        name_list.append(str(i[1]))
    
    for x in name_list:
        if x not in unique_names:
            unique_names.append(x)

    for y in birth_list:
        if x not in unique_birth:
            unique_birth.append(y)

    print(unique_names,unique_birth)
            
def main()->None:
    us23(indi_list)

if __name__ == "__main__":
    main()