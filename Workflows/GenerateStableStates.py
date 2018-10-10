import sys
sys.path.append(sys.path[0]+'/Assets')
from Stable_States import *
from Args import *

print "Workflow started..."
print "Generate stable states..."

m = model(gs)
print "Opening Model :"+str(m)


export_list_of_lists_to_csv(gs,Get_List_of_Stable_states(gs,m),getExportName(gs))
