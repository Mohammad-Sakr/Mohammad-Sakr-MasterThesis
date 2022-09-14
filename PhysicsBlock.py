import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
global x,xx
global y
global c
x=[]
xx=[]
y=[]
c=0

K=1.38e-23          #Boltzmann constant (in J/K)
R_gas=0.082057366   #Universal gas constant (in L*atm/mol*K)
NA=6.0221408e+23    #Avogadro constant (in 1/mol)
A_tungsten=183.84   #Tungsten mass number
P_breakdown=np.array([1e-6,1e-5,1e-4,1e-3,1e-2,1e-1])
V_breakdown=np.array([45.6,45.4,45.3,38.9,9.8,2.1])

class PhysicsBlock:
    
    def __init__(self,TubeParameters):
        self.TubeParameters=TubeParameters
        
    def evaluate(self,params,tStep,OperationParameters):
        return params
    
    def resetBlock(self):
        return 0
    def applyStats(self,actualTubePars):
        return 0
        
class EvaporationRate(PhysicsBlock):
    
    def __init__(self,qo, A_eva):
        self.qo=qo                       #Energy (in J) of evaporation per atom of metal (at T=0)
        self.A_eva=A_eva                 #Evaporation constant (in g/m^2*s)

        
    def evaluate(self,params,tStep,OperationParameters):
        T_fil=OperationParameters['T_fil']
        R_eva=self.A_eva*np.exp(-self.qo/(K*T_fil))
        params['R_eva']=R_eva
        return params
    
    def applyStats(self,actualTubePars):
        self.qo=actualTubePars['qo']
        self.A_eva=actualTubePars['A_eva']
        
    
class PressureBuildup(PhysicsBlock):
    
    def __init__(self,A_fil,V_tube,T_vac):
        self.m_eva_tot=0                 #Total accumulated number of moles of evaporated filament
        self.A_fil=A_fil                 #Total outer area (in m^2) of the filament
        self.V_tube=V_tube               #Total volume (in L) of the tube
        self.T_vac=T_vac                 #Vacuum (inside tube) absolute temperature (in K)
        
        
    def evaluate(self,params,tStep,OperationParameters):
        self.m_eva_tot=self.m_eva_tot+params['R_eva']*tStep*self.A_fil #Total evaporated mass (in g)
        n=self.m_eva_tot/A_tungsten                           #Number of moles of evaporated filament
        P_atm=n*R_gas*self.T_vac/self.V_tube                  #Pressure (in atm)
        params['P_mbar']=P_atm*1.01e3                                   #Pressure (in mbar)
   
    def resetBlock(self):
        self.m_eva_tot=0 
        
    def applyStats(self,actualTubePars):
        self.A_fil=actualTubePars['A_fil']
        self.V_tube=actualTubePars['V_tube']    
        self.T_vac=actualTubePars['T_vac']    
        
        
class Outgassing(PhysicsBlock):
    
    def __init__(self,A_tube,V_tube,AAOR):
        self.A_tube=A_tube               #Total inner area of the tube (in m^2)
        self.V_tube=V_tube               #Total volume (in L) of the tube
        self.AAOR=AAOR                   #Average area outgassing rate (in mbar.l/s/cm^2)
        self.P_outgas_tot=0              #Total outgassing
        
    def evaluate(self,params,tStep,OperationParameters):
        self.P_outgas_tot=self.P_outgas_tot+self.AAOR*tStep*self.A_tube*1e4/self.V_tube
        params['P_mbar']=params['P_mbar']+self.P_outgas_tot #Modified pressure (outgassing)

    def resetBlock(self):
        self.P_outgas_tot=0 
        
    def applyStats(self,actualTubePars):
        self.A_tube=actualTubePars['A_tube']
        self.V_tube=actualTubePars['V_tube']    
        self.AAOR=actualTubePars['AAOR']    
                
class Arcing(PhysicsBlock):
    
    def __init__(self,L_arc):
        self.L_arc=L_arc                 #The distance (in m) between cathode and anode
        self.arcingCount=0
        self.consecutiveArcingCount=0
        
    def evaluate(self,params,tStep,OperationParameters):
       V_arc=np.interp(np.log10(params['P_mbar']),np.log10(P_breakdown),V_breakdown*(1000*self.L_arc)) #Required voltage for arcing (in kV)
       V_arc_stat=V_arc*np.random.weibull(5)  #Adding statistical nature for V_arc
       if OperationParameters['V_anode']>V_arc_stat:
            self.arcingCount=self.arcingCount+1
            self.consecutiveArcingCount=self.consecutiveArcingCount+1 
       else:
           self.consecutiveArcingCount=0
       if self.consecutiveArcingCount>3:
           params['isfailed']=True
           
    def resetBlock(self):
        self.arcingCount=0
        self.consecutiveArcingCount=0
        
    def applyStats(self,actualTubePars):
        self.L_arc=actualTubePars['L_arc']        
            
class FilamentEvaporation(PhysicsBlock):
    
    def __init__(self,r_fil,R_fil,NumPitches,rho_fil):
        self.m_eva_tot=0                 #Total accumulated number of moles of evaporated filament
        filamentTotalMass=np.pi*np.pi*r_fil*r_fil/4*R_fil*NumPitches*rho_fil*1000000
        self.m_eva_tot_fail=filamentTotalMass*0.1
        self.A_fil=np.pi*np.pi*r_fil*R_fil*NumPitches
        
    def evaluate(self,params,tStep,OperationParameters):
        self.m_eva_tot=self.m_eva_tot+params['R_eva']*tStep*self.A_fil #Total evaporated mass (in g)
        if self.m_eva_tot>self.m_eva_tot_fail:
            params['isfailed']=True
            
    def resetBlock(self):
        self.m_eva_tot=0   
    def applyStats(self,actualTubePars):
        filamentTotalMass=np.pi*np.pi*actualTubePars['r_fil']*actualTubePars['r_fil']/4*actualTubePars['R_fil']*actualTubePars['NumPitches']*actualTubePars['rho_fil']*1000000
        self.m_eva_tot_fail=filamentTotalMass*0.1
        self.A_fil=np.pi*np.pi*actualTubePars['r_fil']*actualTubePars['R_fil']*actualTubePars['NumPitches']
        
        
        
class FilamentEvaporationAtConstCurrent(PhysicsBlock):
    
    def __init__(self,qo, A_eva,r_fil,R_fil,NumPitches,rho_fil):
        self.qo=qo                       #Energy (in J) of evaporation per atom of metal (at T=0)
        self.A_eva=A_eva                 #Evaporation constant (in g/m^2*s)
        self.m_eva_tot=0                 #Total accumulated number of moles of evaporated filament
        self.filamentTotalMass=np.pi*np.pi*r_fil*r_fil/4*R_fil*NumPitches*rho_fil*1000000
        self.m_eva_tot_fail=self.filamentTotalMass*0.1
        self.A_fil=np.pi*np.pi*r_fil*R_fil*NumPitches
        
    def evaluate(self,params,tStep,OperationParameters):
        T_fil=OperationParameters['T_fil']*np.sqrt(self.filamentTotalMass/(self.filamentTotalMass-self.m_eva_tot))
        global x, xx, c, y
        x.append(T_fil)
        #xx.append((48*(1+4.83e-3*T_fil+1.663e-6*T_fil*T_fil))*(self.filamentTotalMass/(self.filamentTotalMass-self.m_eva_tot))*1/1000*0.96)
        xx.append(T_fil)
        y.append(c)
        c=c+tStep
        R_eva=self.A_eva*np.exp(-self.qo/(K*T_fil))
        self.m_eva_tot=self.m_eva_tot+R_eva*tStep*self.A_fil #Total evaporated mass (in g)
        if self.m_eva_tot>self.m_eva_tot_fail:
            params['isfailed']=True        
            
    def resetBlock(self):
        self.m_eva_tot=0 
    
    def applyStats(self,actualTubePars):
        self.qo=actualTubePars['qo']
        self.A_eva=actualTubePars['A_eva']        
        self.filamentTotalMass=np.pi*np.pi*actualTubePars['r_fil']*actualTubePars['r_fil']/4*actualTubePars['R_fil']*actualTubePars['NumPitches']*actualTubePars['rho_fil']*1000000
        self.m_eva_tot_fail=self.filamentTotalMass*0.1
        self.A_fil=np.pi*np.pi*actualTubePars['r_fil']*actualTubePars['R_fil']*actualTubePars['NumPitches']
        
        
        
        
        
        
        
        
        
        
        
        
# class TestBlock1(PhysicsBlock):
        
#     def evaluate(self,params,OperationParameters):
#         params['Test1']=5
#         print(params['Test1'])
#         return params
    
# class TestBlock2(PhysicsBlock):
        
#     def evaluate(self,params,OperationParameters):
#         params['Test1']=params['Test1']*2
#         print(params['Test1'])
#         return params
    
# class TestBlock3(PhysicsBlock):
        
#     def evaluate(self,params,OperationParameters):
#         params['Test1']=params['Test1']+1
#         print(params['Test1'])
#         return params
    
    
    
    