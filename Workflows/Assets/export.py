#export.py
import csv
from Args import *

def export_flat_list_to_csv(gs,a_list,filename):
    if checkIfExport(gs):
        with open(filename, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in a_list:
                writer.writerow([val])
    else:
        print a_list

def export_list_of_lists_to_csv(gs,a_list,filename):
    print('exporting.. ', a_list)
    if getExportName(gs) != False:
        with open(filename, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(a_list)
    else:
        print a_list
