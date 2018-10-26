import sys
import itertools
sys.path.append(sys.path[0]+'/Assets')
from perturbation import *
from Stable_States import *
from Apply_Perturbation import *
from Args import *

print "Workflow started..."
print "Generate perturbations..."

m = model(gs)
print "Opening Model :"+str(m)


def Apply_Perturbation_to_model(model,perturbation):
    return lqm.modifyModel(model,"perturbation",perturbation)

P = get_perturbations_list(m,getPerturbationSize(gs))

SS = []

biolqm_perts = []



for p in P:
    lp = list(itertools.chain.from_iterable(p))
    pt = ""
    for i in range(0,len(lp),2):
        pt += str(lp[i])+"%"+str(lp[i+1])
    perturbed_model = Apply_Perturbation_to_model(m,pt)
    SS+=([[pt],Get_List_of_Stable_states(gs,perturbed_model)])

for S in SS:
    print S
print lp
export_list_of_lists_to_csv(gs,SS,getExportName(gs))
print "exported !"
