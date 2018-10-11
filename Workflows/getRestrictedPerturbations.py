import sys
sys.path.append(sys.path[0]+'/Assets')
from perturbation import *
from Args import *
from filtre_perturbations import *


print "Workflow started..."
print "Generate perturbations..."

m = model(gs)
print "Opening Model :"+str(m)



if getRestType(gs)[0] == "max":
    export_list_of_lists_to_csv(gs,set_max_val(get_perturbations_list(m,getPerturbationSize(gs)),getRestType(gs)[1]),getExportName(gs))
elif getRestType(gs)[0] == "min":
    export_list_of_lists_to_csv(gs,set_min_val(get_perturbations_list(m,getPerturbationSize(gs)),getRestType(gs)[1]),getExportName(gs))
elif getRestType(gs)[0] == "range":
    export_list_of_lists_to_csv(gs,getPertInRangeFromString(get_perturbations_list(m,getPerturbationSize(gs)),getRestType(gs)[1]),getExportName(gs))
