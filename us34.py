def age_list(indi_list):
    '''Printing the Age list'''
    age_list = []
    for individual in indi_list:
        if individual[4] != 0:
            age_list.append(individual[0])
    print("Deceased individuals list is : ", death_list)
    for i in age_list:
        print("Individual with ID " + i + " and name " + name_by_id(indi_list, i) + " passed away on " + death_date(indi_list, i))