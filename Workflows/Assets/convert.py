import collections



#convert tuple to list
def tuples_to_lists(the_tuples):
    the_lists = []
    for t in the_tuples:
        the_lists.append(list(t))
    return the_lists

# input     -> "a",2args   --- output    -> "a%2"
def biolqm_concatenation(a,z):
    return a+"%"+str(z) #return a string

#converting a list of perturbation to bioLQM pattern
def list_to_bioLQM_list(lst):
    couples = []
    for i in lst: #lst of element
        couples_joined = []
        elements = []
        for j in i: #element to string
            couple = biolqm_concatenation(j[0],j[1])
            elements.append(couple)
        Joined_Couple = ""
        for e in range(len(elements)):
            Joined_Couple = Joined_Couple + str(elements[e])
            if e != len(elements)-1:
                Joined_Couple = Joined_Couple + ","
        couples.append(Joined_Couple)
    for c in couples:
        couples_joined.append(c)
    return couples_joined



def list_of_perturbations_to_strings(list_of_perturbations):
    out_list = []
    for perturbation in list_of_perturbations:
        perturbation_out = ""
        for comp_state in perturbation:
            perturbation_out += comp_state[0]+"%"+str(comp_state[1])
        out_list.append(perturbation_out)
    return out_list



#["x","x"] --> ["x,x"]
def Join_List_to_Strings(lst):
    o = []
    for b in lst :
        o.append(",".join(b))
    return o #return list of strings


#check duplicated items
#return boolean : true if an element exist in the list !
def Check_Duplications(list_of_values):
    value_dict = collections.defaultdict(int)
    for item in list_of_values:
        value_dict[item] += 1
    return any(val > 1 for val in value_dict.values())


#removing duplicated elements from the list of perturbations
def Remove_duplcations(list_of_perturbations):
    List_of_Duplicated_Elements = []
    for i in range(len(list_of_perturbations)):
        lst = []
        for j in list_of_perturbations[i]:
            lst.append(j[0])
        #checking for duplication in the list of combinations
        if Check_Duplications(lst):
            List_of_Duplicated_Elements.append(i)
        #end of if
    #end of for
    i = 0 # i = postion of the element to keep
    list_of_perturbationss_cleaned = [] # the output
    for i in range(len(list_of_perturbations)):
        if i not in List_of_Duplicated_Elements:
            list_of_perturbationss_cleaned.append(list_of_perturbations[i])
    #return
    return list_of_perturbationss_cleaned





def StringToRange(s):
    z = s.split("-")
    return range(int(z[0]),int(z[1])+1)

#convert one perturbation from csv file to biolqm string
def csv_to_biolqm(csvfile):
    biolqm = ""
    biolqmlist = []
    with open(csvfile, 'rb') as f:
        reader = csv.reader(f)
        list_st = list(reader)
        for i in list_st:
            flag = 0
            for j in i:
                flag +=1
                biolqm += j
                if flag%2:
                    biolqm += "%"
        biolqmlist += biolqm
    return biolqm
