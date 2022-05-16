"""Packages importing"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import ModulesClasses as MC

"""Tube parameters"""
L_arc=0.01                              #The distance (in m) between cathode and anode
V_tube=(0.02*0.02)/4*0.05*3.14159*1000  #Total volume (in L) of the tube
A_fil=0.0001                            #Total outer area (in m^2) of the filament
qo=1.33308e-18                          #Energy (in J) of evaporation per atom of metal (at T=0)
A_eva=708475900690                      #Evaporation constant (in g/m^2*s)
T_vac=300                               #Vacuum (inside tube) absolute temperature (in K)
A_tube=0                                #Total inner area of the tube (in m^2)
AAOR=0                                  #Average area outgassing rate (in mbar.l/s/cm^2)

"""Module instantiation"""
Arcing_M=MC.ArcingModule(L_arc,V_tube,A_fil, qo,A_eva, T_vac,A_tube,AAOR)

"""Step parameters"""
t_step=365*24*3600*2 #time step (in s)
T_fil=2000           #Filament absolute temperature (in K)
V_anode=50           #Applied anode voltage (in kV)

#Arcing_M.step(t_step/4,T_fil,V_anode)
for i in range(63072000):
    Arcing_M.step(1,T_fil,V_anode)
    if Arcing_M.failureCheck():
        print("failure!!!")
        break
print(Arcing_M.elapsedTime()/3600)






