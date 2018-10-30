import sys
import itertools
sys.path.append(sys.path[0]+'/Assets')
from perturbation import *
from Stable_States import *
from Apply_Perturbation import *
from Args import *
from filtre_pattern import *

print "Workflow started..."
print "Generate perturbations..."

m = model(gs)
print "Opening Model :"+str(m)

def Apply_Perturbation_to_model(model,perturbation):
    return lqm.modifyModel(model,"perturbation",perturbation)

#get the input values to fix from the command line !
fix_pattern = getFix(gs)

#get the components and make the fixing perturbation
#get components names !
comps = get_node_names(get_nodes_by_index(gs,get_all_index_nodes(gs)))[:len(fix_pattern)]
fix_perturnaton = "" #biolqm perturbation
for i in range(len(fix_pattern)):
    fix_perturnaton += comps[i]+"%"+fix_pattern[i]+","
#apply the perturbation to fix the first value of the model
m2 = Apply_Perturbation_to_model(m,fix_perturnaton)
print "Model Created:"+str(m2)
#get the list of perturbations
all_perturbations = get_perturbations_list(m2,getPerturbationSize(gs))

StableStates_by_perturbation = []
# make the list of StableStates_by_perturbation
for perturbation in all_perturbations:
    perturbation2 = list(itertools.chain.from_iterable(perturbation))
    pt = ""
    for i in range(0,len(perturbation2),2):
        pt += str(perturbation2[i])+"%"+str(perturbation2[i+1])
    perturbed_model = Apply_Perturbation_to_model(m2,pt)
    print perturbed_model
    StableStates_by_perturbation.append([[pt],Get_List_of_Stable_states(gs,perturbed_model)])

print "list of Stable States by Perturbation generated !"

if(getType(gs)=="not"):
    for i in not_filtre_stable_states_by_perturbation(StableStates_by_perturbation,getPattern(gs)):
        print i
elif(getType(gs)=="and"):
    pass
elif(getType(gs)=="or"):
    for i in or_filtre_stable_states_by_perturbation(StableStates_by_perturbation,getPattern(gs)):
        print i
