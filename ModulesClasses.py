"""Packages importing"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy

"""Constants"""
K=1.38e-23          #Boltzmann constant (in J/K)
R_gas=0.082057366   #Universal gas constant (in L*atm/mol*K)
NA=6.0221408e+23    #Avogadro constant (in 1/mol)
A_tungsten=183.84   #Tungsten mass number
P_breakdown=np.array([1e-6,1e-5,1e-4,1e-3,1e-2,1e-1])
V_breakdown=np.array([45.6,45.4,45.3,38.9,9.8,2.1])

class ArcingModule:
   
    def __init__(self, L_arc, V_tube, A_fil, qo, A_eva,T_vac ):
        self.L_arc=L_arc                 #The distance (in m) between cathode and anode
        self.V_tube=V_tube               #Total volume (in L) of the tube
        self.A_fil=A_fil                 #Total outer area (in m^2) of the filament
        self.qo=qo                       #Energy (in J) of evaporation per atom of metal (at T=0)
        self.A_eva=A_eva                 #Evaporation constant (in g/m^2*s)
        self.T_vac=T_vac                 #Vacuum (inside tube) absolute temperature (in K)
        self.m_eva_tot=0                 #Total accumulated number of moles of evaporated filament
        self.t_tot_elap=0                #Total elapsed time (in s)
        self.Arcing_Timings=np.array([]) #Timestamp for arcing
    
    def step(self,t_step,T_fil,V_anode):
        self.t_tot_elap=self.t_tot_elap+t_step #Accumulates time
        """Evaporation rate"""
        R_eva=self.A_eva*np.exp(-self.qo/(K*T_fil))  #Evaporation rate (in g/m^2*s)
        """Pressure buildup"""
        self.m_eva_tot=self.m_eva_tot+R_eva*t_step*self.A_fil #Total evaporated mass (in g)
        n=self.m_eva_tot/A_tungsten                      #Number of moles of evaporated filament
        P_atm=n*R_gas*self.T_vac/self.V_tube             #Pressure (in atm)
        P_mbar=P_atm*1.01e3                              #Pressure (in mbar)
        """Dielectric strength"""
       # print(P_mbar)
        V_arc=np.interp(np.log10(P_mbar),np.log10(P_breakdown),V_breakdown*(1000*self.L_arc)) #Required voltage for arcing (in kV)
        V_arc_stat=V_arc*np.random.weibull(5)  #Adding statistical nature for V_arc
        #print(V_arc_stat)
        if V_anode>V_arc_stat:
            self.Arcing_Timings=np.append(self.Arcing_Timings,self.t_tot_elap)
            print("Arc!!!")
   
    def elapsedTime(self):     #Returns the total elapsed time (in s)
        return self.t_tot_elap
    
    def arcingTimestamp(self): #Returns timestamp for arcing
        return self.Arcing_Timings
    
    def failureCheck(self):    #Returns boolean for failure
        if len(self.Arcing_Timings)>3: #There should be at least 4 arcs
            for i in range(3,len(self.Arcing_Timings)):
                if self.Arcing_Timings[i]-self.Arcing_Timings[i-3]<10: #time between the 4 arcs should be smaller than 10 seconds
                    return True
        else:
            return False