def us26(indi, fam, f):
    flag = True
    print("User Story 26 - Corresponding entries , running")

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
            f.write(
                f'ERROR: INDIVIDUAL: US26:  {ind} cannot find corresponding families. \n')
            results.append(
                f'ERROR: INDIVIDUAL: US26:  {ind} cannot find corresponding families.')
            flag = False
    print("User Story 26 Completed")
    return flag