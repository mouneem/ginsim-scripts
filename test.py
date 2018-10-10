import sys
sys.path.insert(0, '../Assets/')
from components import *
from export import *
from model import *



# Get stable states for all perturbations
model = gs.getModel()

find_stable_states(model, gs.getNodeOrder())
