
#radial function parameters

atom_list_r_items = ['O','Ti']
atom_list_r = atom_list_r_items[:]*8

eta_list_r = [0.003214,0.003214,0.035711,0.035711,0.071421,0.071421,
            0.124987,0.124987,0.214264,0.214264,0.357106,0.357106,
            0.714213,0.714213,1.428426,1.428426]

radial_parameters = [(a,b) for (a,b) in zip(atom_list_r,eta_list_r)]
print(len(radial_parameters))

#angular_function_parameters

atom_list_a_items = [('O','O'),('O','Ti'),('Ti','Ti')]
atom_list_a =  atom_list_a_items[:]*18
#print((atom_list_a))


eta_list_a_items = [0.000357,0.000357,0.000357,0.028569,0.028569,0.028569,
            0.089277,0.089277,0.089277]
eta_list_a = eta_list_a_items[:]*6
#print(len(eta_list_a))


lambda_list_a_items = [-1,-1,-1,-1,-1,-1,-1,-1,-1,
                        1,1,1,1,1,1,1,1,1,]
lambda_list_a = lambda_list_a_items[:]*3
#print(len(lambda_list_a))

zeta_list_a_items = [1,2,4]
zeta_list_a = [i for i in zeta_list_a_items for j in range(18)]
#print(len(zeta_list_a))

angular_parameters = [(a,b,c,d,e) for ((a,b),c,d,e) in zip(atom_list_a,eta_list_a,lambda_list_a,zeta_list_a)]

print(angular_parameters)