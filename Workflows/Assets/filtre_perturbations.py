#filtre pattern (states)
from convert import *

def set_max_val(perturbations,max):
    return get_perturbations_with_val_in_range(perturbations,range(0,int(max)+1))

def set_min_val(perturbations,min):
    return get_perturbations_with_val_in_range(perturbations,range(int(min),99))

def getPertInRangeFromString(perturbations,stringRange):
    return get_perturbations_with_val_in_range(perturbations,StringToRange(stringRange))

def get_perturbations_with_val_in_range(perturbations,cc):
    output = []
    for i in perturbations:
        for perturbation in i:
            if int(perturbation[1]) in cc:
                output.append(perturbation)
    return output
