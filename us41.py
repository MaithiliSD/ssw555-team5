from project03 import gedcomRead
from typing import Dict, List
individual, Families = gedcomRead("project02_gedcom.ged")

def fixDates(dt):
    dt = dt.split(" ")
    if dt.__len__() == 3:
        return dt[0] + ' ' + dt[1] + ' ' + dt[2]
    if dt.__len__() == 1:
        return '10 JAN ' + dt[0]

    elif dt.__len__() == 2:
        return '10 ' + dt[0] + ' ' + dt[1]

def partialDates(individual: Dict, family: Dict) -> List[str]:
    fixedDates: List = []
    ind: List = []
    fam: List = []
    for key in individual:
        if 'BIRT' in individual[key]:
            if individual[key]['BIRT'].split(' ').__len__() < 3:
                ind.append([key, fixDates(individual[key]['BIRT'])])

        if 'DEAT' in individual[key]:
            if individual[key]['BIRT'].split(' ').__len__() < 3:
                ind.append([key, fixDates(individual[key]['DEAT'])])

    for key in family:
        if family[key]['MARR'].split(' ').__len__() < 3:
            fam.append([key, fixDates(family[key]['MARR'])])

    if ind.__len__() > 0 or fam.__len__() > 0:
        fixedDates.append('US41: All Dates Made Valid:')
    if ind.__len__() > 0:
        fixedDates.append(ind)

    if fam.__len__() > 0:
        fixedDates.append(fam)

    if fixedDates.__len__() == 0:
        fixedDates.append("US41: All Dates Already Valid")
    return fixedDates