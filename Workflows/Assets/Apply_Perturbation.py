# -*- coding: utf-8 -*-
import sys
from model import *
from export import *

def Apply_Perturbation_to_model(model,perturbation):
    return lqm.modifyModel(model,"perturbation",perturbation)

def Apply_List_of_Perturbation_to_model(model,perturbations):
    list_of_perturbations = []
    if(perturbations):
        for perturbation in perturbations:
            list_of_perturbations.append(lqm.modifyModel(model,"perturbation",perturbation))
        return list_of_perturbations
    print("pert not applied")
    return model



def Apply_interactopn_perturbation(model,perturbations):
    return lqm.modifyModel(model,"perturbation",perturbations)
