from project03 import indi_list,fam_list,calculateAge

def us22(indi,fam):
    flag = True
    ids_indi = []
    ids_fam = []
    for i in indi:
        ids_indi.append(i[0])
    for j in fam:
        ids_fam.append(j[0])
    l = set([x for x in ids_indi if ids_indi.count(x)>1])
    fa = set([x for x in ids_indi if ids_fam.count(x)>1])
    if ((len(ids_indi) == len(set(ids_indi))) and (len(ids_fam) == len(set(ids_fam)))):
        return flag
    else:
        flag = False
        if(len(l) > 0):
            print("There is a repeating id in individual" + str(l))
            return flag
        elif (len(fa)> 0 ):
            print("There is a repeating id in Fam" + str(fa))
            return flag

def main()->None:
    us22(indi_list,fam_list)

if __name__ == "__main__":
    main()