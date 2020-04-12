from src import material, state

copper_params = {
    'mag'        : [0,0,1],
    'sa_equil'   : [0.0],
    'diff'       : [0.3],
    'polar_con'  : [0.5],
    'polar_diff' : [0.9],
    'len_pre'    : [4.0e-9],
    'len_dph'    : [4.0e-9],
    'len_sf'     : [2.0e-9],
}

copper_1 = material.Material(copper_params)
copper_1.params['thickness'] = [5.0e-9]
copper_1.params['n_dx'] = [100]

copper_2 = material.Material(copper_params)
copper_2.params['thickness'] = [10.0e-9]
copper_2.params['n_dx'] = [100]

sys = state.State([copper_1, copper_2])
#print(sys.space)