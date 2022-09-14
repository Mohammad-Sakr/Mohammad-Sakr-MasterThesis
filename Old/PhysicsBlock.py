import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy

K=1.38e-23          #Boltzmann constant (in J/K)

class PhysicsBlock:
    
    def __init__(self,qo, A_eva):
        self.qo=qo                       #Energy (in J) of evaporation per atom of metal (at T=0)
        self.A_eva=A_eva                 #Evaporation constant (in g/m^2*s)

        
    def eva_rate(self,params):
        T_fil=params['T_fil']
        R_eva=self.A_eva*np.exp(-self.qo/(K*T_fil))
        params['R_eva']=R_eva
        return params