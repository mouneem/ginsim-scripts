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

input_pattern = getInputPattern(gs)
input_componenets = get_node_names(get_nodes_by_index(gs,get_all_index_nodes(gs)))
input_perturbation = ""

for i in range(len(input_pattern)):
    input_perturbation += input_componenets[i]+"%"+input_pattern[i]+","

print input_perturbation

m2 = Apply_Perturbation_to_model(m,input_perturbation)



all_perturbations = get_perturbations_list(m,getPerturbationSize(gs))
Pert_and_StableStates = []

for perturbation in all_perturbations:
    perturbation2 = list(itertools.chain.from_iterable(perturbation))
    pt = ""
    for i in range(0,len(perturbation2),2):
        pt += str(perturbation2[i])+"%"+str(perturbation2[i+1])
    perturbed_model = Apply_Perturbation_to_model(m2,pt)
    print perturbed_model
    Pert_and_StableStates.append([[pt],Get_List_of_Stable_states(gs,perturbed_model)])


restriction = getPattern(gs)

out = []
for pert_states in Pert_and_StableStates :
    Similarity_Found = False
    for stable_state in pert_states[1]:
        c = 0
        print "\n"
        for i,j in zip(stable_state[len(input_pattern):],restriction):
            if str(i)==str(j):
                c += 1
        if c > len(restriction)-1:
            Similarity_Found = True
    print Similarity_Found
    if Similarity_Found == False:
        out.append([pert_states[0][0],pert_states[1]])



print "------"


forexport = []
for i in out:
    forexport.append(i)


print forexport
export_list_of_lists_to_csv(gs,forexport,getExportName(gs))


000100111010011111100000000101111111111011110000002
