from Args import *
import csv

def importCSVList(gs):
    name = getInputFileName(gs)
    with open(name, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return your_list


def importCSVListByName(name):
    with open(name, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return your_list

def IsFile(s):
    if len(s.split("."))==2 :
        return True
    return False
