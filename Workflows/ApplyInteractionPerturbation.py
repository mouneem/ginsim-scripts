import sys
sys.path.append(sys.path[0]+'/Assets')
from perturbation import *
from components import *
from Args import *
from input import *
from Apply_Perturbation import *

print "Workflow started..."
print "Generate perturbations...    "

m = model(gs)
print "Opening Model :"+str(m)

def Apply_interactopn_perturbation(model,path):
    lines = importCSVListByName(path)
    modls = []
    for i in range(1,len(lines)):
        try:
            pertur = lines[i][0]+":"+lines[i][1]+"%"+lines[i][2]
            modls.append(lqm.modifyModel(model,"perturbation",pertur))
        except Exception as e:
            raise
    return modls


def Apply_interactopn_perturbation(model,perturbations):
    return lqm.modifyModel(model,"perturbation",perturbations)



def exportModel(model):
    lqm.saveModel(model, "modelname.sbml", "ginml")

def Apply_interactopn_perturbations(model,path):
    lines = importCSVListByName(path)
    modls = []
    for i in range(1,len(lines)):
        try:
            pertur = lines[i][0]+":"+lines[i][1]+"%"+lines[i][2]
            modls.append(lqm.modifyModel(model,"perturbation",pertur))
        except Exception as e:
            raise
    return modls


if  IsFile(getInterArg(gs)):
    print "is file..."
    perturbed_model = Apply_interactopn_perturbations(m,getInterArg(gs))
else:
    perturbed_model = Apply_interactopn_perturbation(m,getInterArg(gs))
    perturbed_model =  [perturbed_model]

print type(perturbed_model[0])
lqm.saveModel(perturbed_model[0], getExportName(gs), "ginml")
