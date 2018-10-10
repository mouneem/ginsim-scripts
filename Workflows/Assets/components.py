#components.py

#get from ginssim/biolqm model the list of components and their max level
def get_list_of_components_and_max(model):
    lst = []
    for node in model.getComponents(): #Java function
        if not node.isInput(): #Java attribute check if input node exist
            lst += [[str(node.nodeID).split("'")[0],node.max]] #making a list of components
    # return list of ['Node Name' , Node Max size]
    return lst

#get component list from a list of components and their max
def get_component(list_of_components_and_max):
    list_of_components = []
    for e in list_of_components_and_max:
        for i in range(e[1]+1):
            list_of_components.append([e[0],i])
    return list_of_components



#get all comps index
def get_all_index_nodes(gs):
    no = gs.open(gs.args[0]).getNodeOrder()
    return [range(no.size())]

#get inner components index
def get_inner_comp_index(gs):
    nodeOrder = gs.open(gs.args[0]).getNodeOrder()
    nodeList = []
    for n in range(nodeOrder.size()):
        if (nodeOrder[n].isInput()):
            pass
        else:
            nodeList.append(n)
    return nodeList


#get input index
def get_inputs_index_nodes(gs):
    nodeOrder = gs.open(gs.args[0]).getNodeOrder()
    inputNodes = []
    idx = 0
    for n in range(nodeOrder.size()):
        if nodeOrder[n].isInput():
            inputNodes.append(n)
    return inputNodes

#get node by index require one of previous fonctions
def get_nodes_by_index(gs, list_of_index):
    nodeOrder = gs.open(gs.args[0]).getNodeOrder()
    nodeList = []
    try:
        if len(list_of_index)==1:
            list_of_index = list_of_index[0]
    except Exception as e:
        raise
    for n in list_of_index:
        nodeList.append(nodeOrder[n])
    return nodeList

#get node info
#input should be a list of nodes
def get_node_name_and_max(list_of_nodes):
    list_of_info = []
    for node in list_of_nodes:
        list_of_info.append([str(node),node.getMaxValue()])
    return list_of_info

def get_node_names(list_of_nodes):
    list_of_info = []
    for node in list_of_nodes:
        list_of_info.append(str(node))
    return list_of_info
