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
