import sys
sys.path.append(sys.path[0]+'/Assets')
from perturbation import *
from Args import *
from Apply_Perturbation import *
from Stable_States import *

print "Workflow started..."
print "Applying Perts..."

m = model(gs)
print "Opening Model :"+str(m)


def Apply_List_of_Perturbation_to_model(model,perturbations):
    list_of_perturbations = []
    if(perturbations):
        for perturbation in perturbations:
            list_of_perturbations.append(lqm.modifyModel(model,"perturbation",perturbation))
        return list_of_perturbations
    return model
