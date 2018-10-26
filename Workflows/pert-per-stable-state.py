import sys
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

for p in P:
    perturbation_biolqm_format = ""
    if type(p) is list:
        pass
    else:
        perturbation_biolqm_format = str(p[0])+"%"+str(p[1])
    perturbed_model = Apply_Perturbation_to_model(m,perturbation_biolqm_format)
    SS+=([p,Get_List_of_Stable_states(gs,perturbed_model)])

for S in SS:
    print S

export_list_of_lists_to_csv(gs,SS,"allstablestates")
print "exported !"
