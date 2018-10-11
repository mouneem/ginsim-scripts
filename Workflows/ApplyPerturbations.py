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


def exportModel(model,n):
    lqm.saveModel(model, n, "sbml")

def Apply_List_of_Perturbation_to_model(model,perturbations):
    list_of_perturbations = []
    if(perturbations):
        for perturbation in perturbations:
            list_of_perturbations.append(lqm.modifyModel(model,"perturbation",perturbation))
        return list_of_perturbations
    return model

def Apply_Perturbation_to_model(model,perturbation):
    return lqm.modifyModel(model,"perturbation",perturbation)

pert = getSinglePerturbation(gs)
print pert
newModel = Apply_Perturbation_to_model(m,pert)
print newModel
print "exporting :"+ getExportName(gs)
if getExportName(gs):
    modelname = getExportName(gs)
    exportModel(newModel,modelname)
