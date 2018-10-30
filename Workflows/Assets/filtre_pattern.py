#filtre pattern (states)
from convert import *


def check_size_equal(list_of_patterns):
    counter = 0
    for p in range(len(list_of_patterns)-1):
        if len(list_of_patterns[p]) == len(list_of_patterns[p+1]):
            counter = counter + 1
    if len(list_of_patterns)-1 == counter:
        return True
    else:
        return False

#filtring function !
def filltr_patterns(patterns,filltrs):
    output = []
    if check_size_equal(patterns+filltrs):
        L = len(filltrs[0])
        for pattern in patterns:
            flag = False
            for filtre in filltrs:
                counters = []
                counter = 0
                for index in range(L):
                    if pattern[index] == "*" or filtre[index] == "*" or pattern[index] == filtre[index]:
                        counter = counter + 1
                counters.append(counter)
                for c in counters:
                    if c == L :
                        flag = True
                print pattern,filtre,output
            if flag:
                output.append(pattern)
        return output
    else:
        return -1

#filtring function !
def filltr_patterns_and(patterns,filltrs):
    output = []
    if filltrs[0]:
        L = len(filltrs[0])
    for pattern in patterns:
        flag = False
        match = 0
        for filtre in filltrs:
            c = 0
            for index in range(L):
                if pattern[index] == "*" or filtre[index] == "*" or pattern[index] == filtre[index]:
                    c = c + 1
            print c
            if c == L :
                match = match + 1
        if match == len(filltrs):
            output.append(pattern)
        print pattern,filltrs,match, len(filltrs)
    return output

#filtring function !
def filltr_patterns_not(patterns,filltrs):
    output = []
    if check_size_equal(patterns+filltrs):
        L = len(filltrs[0])
        for pattern in patterns:
            flag = False
            for filtre in filltrs:
                counters = []
                counter = 0
                for index in range(L):
                    if pattern[index] == "*" or filtre[index] == "*" or pattern[index] == filtre[index]:
                        counter = counter + 1
                counters.append(counter)
                for c in counters:
                    if c == L :
                        flag = True
                print pattern,filtre,output
            if not flag:
                output.append(pattern)
        return output
    else:
        return -1



def not_filtre_stable_states_by_perturbation(list_of_patterns_and_perturbations,restriction):
    valid_states_per_perturbation = []
    for perturbation_and_state in list_of_patterns_and_perturbations:
        valid_states = []
        for state in perturbation_and_state[1]:
            #loop pattern size
            counter = 0
            for j in range(len(restriction)):
                if (restriction[j] == str(state[j]) or str(state[j]) == "-1") or restriction[j] == "*" :
                    counter += 1
            #print counter, len(restriction)
            if counter != len(restriction):
                valid_states.append(state)
        if len(valid_states) == len(perturbation_and_state[1]):
            valid_states_per_perturbation.append([perturbation_and_state[0],perturbation_and_state[1]])
    return valid_states_per_perturbation


def or_filtre_stable_states_by_perturbation(list_of_patterns_and_perturbations,restriction):
    valid_states_per_perturbation = []
    for perturbation_and_state in list_of_patterns_and_perturbations:
        valid_states = []
        for state in perturbation_and_state[1]:
            #loop pattern size
            counter = 0
            for j in range(len(restriction)):
                if restriction[j] == str(state[j]) or "-1" == str(state[j]) or restriction[j] == "*":
                    counter += 1
            if counter == len(restriction):
                valid_states.append(state)
        if len(valid_states) == len(perturbation_and_state[1]):
                valid_states_per_perturbation.append([perturbation_and_state[0],valid_states])
    return valid_states_per_perturbation
