import sys
sys.path.append(sys.path[0]+'/Assets')
from perturbation import *
from Args import *

print "Workflow started..."
print "Generate perturbations..."

m = model(gs)
print "Opening Model :"+str(m)


export_list_of_lists_to_csv(gs,get_perturbations_list(m,getPerturbationSize(gs)),getExportName(gs))
