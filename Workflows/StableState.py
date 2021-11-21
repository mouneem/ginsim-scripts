import sys
sys.path.append(sys.path[0]+'/Assets')
from perturbation import *
from Args import *
from Apply_Perturbation import *
from Stable_States import *

g = gs.open(gs.args[0])

model = g.getModel()
ssrv = gs.service("stable")
searcher = ssrv.getStableStateSearcher(model)
searcher.call()
paths = searcher.getPaths()
values = paths.getPath()

def mutants_stable_states(input_row_number, input_test_state, string_name, input_no_st_parameter, input_show_parameter, input_disrupt_parameter):
    for p in perturbation:
        m = p.apply(model)
        searcher = ssrv.getStableStateSearcher(m)
        searcher.call()
        paths = searcher.getPaths()
        values = paths.getPath()

		st_matrix=[]
		st_matrix_contagem_multiple_st=[]

		if paths.countPaths()==0 and input_no_st_parameter==1:
			#if a perturbation has 1 ST then the countPaths() returns 1, this includes the ST that have *, they count only as one path/ST
			#if a perturbation has 2 ST then the countPaths() returns 2, like (1,1,0) and (0,1,1)
			#if a perturbation has 0 ST the countPaths() returns 0
			total_number_perturbation = total_number_perturbation+1
			check_p_already_written=2
			something_is_written=1

			if input_show_parameter==0:
				write_csv.writerow(str(p).replace(',', '-'))
			elif input_show_parameter==1:
				write_csv.writerow('No ST exist for the mutation:')
				write_csv.writerow(str(p).replace(',', '-'))
