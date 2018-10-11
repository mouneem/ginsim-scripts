import sys
sys.path.append(sys.path[0]+'/Assets')
from perturbation import *
from Args import *
from filtre_perturbations import *
from Stable_States import *

print "Workflow started..."
print "Generate perturbations..."

m = model(gs)
print "Opening Model :"+str(m)


export_list_of_lists_to_csv(gs,filtre_states(Get_List_of_Stable_states(gs,m),getPattern(gs)),getExportName(gs))
