#perturbation.py

#importing function from other py files
import sys
from components import *
from model import *
from convert import *
from export import *
from collections import *
import itertools
import math
import collections

# *******************************************************
# list_of_components: [["a",1],["b",0]]
# Size : the size of the combinations in the output
# *******************************************************
def get_perturbations_list(model,size):
    # get list_of_components_and_max from the given model
    #1 - itertools  make combinations tuples from the list of components given
    #2 - Converting tuples from the List Of Tuples to List of lists to allaw working with indexes
    #removing duplicated elements from the list of perturbations
    componets = get_component(get_list_of_components_and_max(model))
    cleaned_list_of_perturbations = []
    for s in size:
        c = Remove_duplcations(tuples_to_lists(list(itertools.combinations(componets,s))))
        cleaned_list_of_perturbations = cleaned_list_of_perturbations + c
    #returning the list of string each string refer to combination of component and a state
    return cleaned_list_of_perturbations



###############################################################################
###############################################################################
###############################################################################
####################### Components Combimations ###############################
###############################################################################
###############################################################################
###############################################################################

# generate list of perturbations from nodes
def input_combinations(list_of_nodes_name_and_max): #size by default equal to one !
    list_of_perturbations = []
    for node in list_of_nodes_name_and_max:
        id = node[0]
        max = node[1]
        for i in range(node[1]+1):
            list_of_perturbations.append([id,i])
    return list_of_perturbations


# generate list of perturbations from nodes of size N
def input_combinations_sizeN(list_of_nodes_name_and_max, N):
    list_of_perturbations = Remove_duplcations(tuples_to_lists(list(itertools.combinations(input_combinations(list_of_nodes_name_and_max),N))))
    return list_of_perturbations
