from project03 import indi_list,fam_list

def us26(indi, fam):
    flag = True

    ind_in_fam = set()
    ind_in_ind = set()
    results = []
    for family in fam:
        ind_in_fam.add(family['WIFE'])
        ind_in_fam.add(family['HUSB'])
        for i in range(len(family['CHIL'])):
            ind_in_fam.add(family['CHIL'][i])
    for ind in indi:
        ind_in_ind.add(ind['INDI'])
    missed_ind = []
    for i in ind_in_ind:
        for j in ind_in_fam:
            if i == j:
                break
        else:
            missed_ind.append(i)
    if missed_ind:
        for ind in missed_ind:
            print(f'ERROR: INDIVIDUAL: US26:  {ind} cannot find corresponding families. \n')
            results.append(f'ERROR: INDIVIDUAL: US26:  {ind} cannot find corresponding families.')
            flag = False
    return flag


us26(indi_list, fam_list)