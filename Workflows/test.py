import sys
sys.path.append(sys.path[0]+'/Assets')
from perturbation import *
from components import *
from Args import *
from Apply_Perturbation import *

print "Workflow started..."
print "Generate perturbations..."

m = model(gs)
print "Opening Model :"+str(m)



def Apply_interactopn_perturbation(model,perturbations):
    return lqm.modifyModel(model,"perturbation",perturbations)


Apply_interactopn_perturbation(m,getInteractionPert(gs))
