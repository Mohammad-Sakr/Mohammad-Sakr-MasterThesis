import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy

K=1.38e-23          #Boltzmann constant (in J/K)

class PhysicsBlock:
    
    def __init__(self,TubeParameters):
        self.TubeParameters=TubeParameters
        
    def evaluate(self,params,OperationParameters):
        return params
    
class EvaporationRate(PhysicsBlock):
    
    def __init__(self,qo, A_eva):
        self.qo=qo                       #Energy (in J) of evaporation per atom of metal (at T=0)
        self.A_eva=A_eva                 #Evaporation constant (in g/m^2*s)

        
    def evaluate(self,params,OperationParameters):
        T_fil=params['T_fil']
        R_eva=self.A_eva*np.exp(-self.qo/(K*T_fil))
        params['R_eva']=R_eva
        return params
    
class TestBlock1(PhysicsBlock):
        
    def evaluate(self,params,OperationParameters):
        params['Test1']=5
        print(params['Test1'])
        return params
    
class TestBlock2(PhysicsBlock):
        
    def evaluate(self,params,OperationParameters):
        params['Test1']=params['Test1']*2
        print(params['Test1'])
        return params
    
class TestBlock3(PhysicsBlock):
        
    def evaluate(self,params,OperationParameters):
        params['Test1']=params['Test1']+1
        print(params['Test1'])
        return params
    
    
    
    