import sys
sys.path.append(sys.path[0]+'/Assets')
from perturbation import *
from components import *
from Stable_States import *
from Args import *
from input import *
from Apply_Perturbation import *

print "Workflow started..."
print "Generate perturbations...    "

m = model(gs)
print "Opening Model :"+str(m)

if getModelFile(gs):
    g2 = gs.open(getModelFile(gs)) #get the file
    model2 = g2.getModel() #get the model
    print "Opening Model :"+str(model2)


StableStatesOfModel1 = Get_List_of_Stable_states(gs,m)
StableStatesOfModel2 = Get_List_of_Stable_states(gs,model2)
Simi = []
Diff = []

Diff.append("Stable States that exist in the first only")
for i in StableStatesOfModel1:
    if i in StableStatesOfModel2:
        Simi.append(i)
    else:
        Diff.append(i)
Diff.append("Stable States that exist in the second only")
for i in StableStatesOfModel2:
    if not i in StableStatesOfModel1:
        Diff.append(i)

print "Similiar Stable States Are :"+str(len(Simi))
for i in Simi:
    print i

for i in Diff:
    print i
