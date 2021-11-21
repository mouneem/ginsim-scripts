#!/usr/bin/python
import sys
#importing function from other py files
sys.path.append('/Assets')
from components import *
from model import *
from convert import *
from export import *

#call function get_list_of_components_and_max
#export_list_to_csv(get_list_of_components_and_max(Get_Model(gs)),Output_file_name(gs))
def Get_List_of_Stable_states(gs,model):
    list_of_stable_states = []
    #get service for stable states -- Java function
    ssrv = gs.service("stable")
    #get service for model -- Java function
    searcher = ssrv.getStableStateSearcher(model)
    searcher.run() # -- Java function
    #get stable states list as java obejctfrom collections import defaultdict
    paths = searcher.getPaths() # -- Java function
    print('#'*88,paths.countPaths())
    for p in paths: # for each stabe state do:
        #extract the stable state from the java object1
        values = paths.getPath() # -- Java function
        # the object extracted is an array
        x = values.tolist() #convertiong the array to a list and adding to the output list of lists
        list_of_stable_states.append(x)
    return list_of_stable_states

def Get_Stable_states_from_list(gs,model):
    list_of_stable_states = []
    for m in model:
        #get service for stable states -- Java function
        ssrv = gs.service("stable")
        #get service for model -- Java function
        searcher = ssrv.getStableStateSearcher(m)
        searcher.run() # -- Java function
        #get stable states list as java obejctfrom collections import defaultdict
        paths = searcher.getPaths() # -- Java function
        for p in paths: # for each stabe state do:
            #extract the stable state from the java object1
            values = paths.getPath() # -- Java function
            # the object extracted is an array
            x = values.tolist() #convertiong the array to a list and adding to the output list of lists
            list_of_stable_states.append(x)
    return list_of_stable_states


def filtre_states(list_of_stable_states, pattern):
    sat = []
    for stable_state in list_of_stable_states:
        match = 0
        for i in range(len(pattern)):
            if stable_state[i] == -1 or pattern[i] == "*" or str(stable_state[i]) == pattern[i]:
                match = match + 1
        if match == len(pattern):
            sat.append(stable_state)
    return sat
