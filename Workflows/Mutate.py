import sys
sys.path.append(sys.path[0]+'/Assets')
from perturbation import *
from Args import *
from Apply_Perturbation import *
from Stable_States import *

print "Workflow started..."

m = model(gs)
print "Opening Model :"+str(m)

perturbations = getPerturbations(gs)

for pert in perturbations:
    print "Applying Perts...", pert
    lqm.modifyModel(m,"perturbation",pert)
