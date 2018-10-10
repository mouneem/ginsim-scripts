In order to run the scripts please use the function:

java -cp GINsim.jar:extensions/jython-standalone-2.7.0.jar org.ginsim.Launcher -s SCRIPT.py Models/Model.zginml 

+++++++++++++++++++++++++++++++
Required Python Packages:
- CSV module
- sys
- itertools
- collections
- math
- numpy 
- matplotlib

+++++++++++++++++++++++++++++++
|  Assets
|  |__ ./model.py
|  |	|__ model(gs) = import the model as JAVA object 
|  |__ ./components.py
|  |	|__ get_list_of_components_and_max(model) = returns the list of components and their max level
|  |	|__ get_component(list_of_components_and_max)
|  |	|__ get_all_index_nodes(gs):#get all comps index
|  |	|__ get_inner_comp_index(gs):#get inner components index
|  |	|__ get_inputs_index_nodes(gs):#get input index
|  |	|__ et_nodes_by_index(gs, list_of_index):#get node by index require one of previous fonctions
|  |	|__ get_node_name_and_max(list_of_nodes):
|  |	|__ get_node_names(list_of_nodes):
|  |__ ./convert.py
|  |	|__ tuples_to_lists(tuple) = convert tuple to list
|  |	|__ biolqm_concatenation(a,z) = input ["a",2] - output "a%2"
|  |	|__ Join_List_to_Strings(list) = ["x","x"] --> ["x,x"]
|  |	|__ Check_Duplications(list) = check duplicated items and returns boolean value : true if an element exist in the list and false if not
|  |	|__ Remove_duplcations(list) = #removing duplicated elements from the list of perturbations
|  |	|__ list_to_bioLQM_list(list) = list of perturbation to bioLQM pattern
|  |	|__ list_of_perturbations_to_strings(list) =  list of lists to list of strings
|  |	|__ csv_to_biolqm(csvfile) = convert one perturbation from csv file to biolqm string
|  |	|__ csv_to_biolqmlist(csvfile) = take as input the name of csv file and return a list of perturbation extracted from this file
|  |__ ./export.py
|  |	|__ export_flat_list_to_csv(list,filename) = export one dim. list to csv file
|  |	|__ export_list_of_lists_to_csv(list,filename)  = export list of lists to a csv file
|  |	|__ export_model(model,name):
|  |__ ./Stable_States.py
|  |	|__ Get_List_of_Stable_states(gs,model(gs) = the output is a list of boolean vars
|  |__ ./Perturbation
|  |	|__ get_perturbations_list(model,size) returns the list of combination of possible perturbations
|  |__ /.Apply_Perturbation
|  |	|__ Apply_Perturbation_to_model(model,perturbation)
|  |	|__ Apply_List_of_Perturbation_to_model(model,list_of_perturbations)
|  |	|__ input_combinations(list_of_nodes_name_and_max): # generate list of perturbations from nodes #size by default equal to one !
|  |	|__ input_combinations_sizeN(list_of_nodes_name_and_max, N): # generate list of perturbations from nodes of size N
|  |__ ./filtre_pattern
|  |	|__ filltr_patterns(patterns,filltrs): or
|  |	|__ filltr_patterns_and(patterns,filltrs): and
|  |	|__ check_size_equal(list_of_patterns)
|  |	|__ filltr_patterns_not(patterns,filltrs)
|  |__ ./filtre_perturbations
|  |	|__ set_max_val
|  |	|__ set_min_val
|  |	|__ get_perturbations_with_val_in_range


