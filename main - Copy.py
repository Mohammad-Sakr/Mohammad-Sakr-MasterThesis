"""Packages importing"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy



"""Constants"""
K=1.38e-23          #Boltzmann constant (in J/K)
R_gas=0.082057366   #Universal gas constant (in L*atm/mol*K)
NA=6.0221408e+23    #Avogadro constant (in 1/mol)
A_tungsten=183.84   #Tungsten mass number



"""Tube parameters"""
L_arc=0.01          #The distance (in m) between cathode and anode
V_tube=(0.02*0.02)/4*0.05*3.14159*1000     #Total volume (in L) of the tube
A_fil=0.0001        #Total outer area (in m^2) of the filament
qo=1.33308e-18      #Energy (in J) of evaporation per atom of metal (at T=0)
T_fil=2000          #Filament absolute temperature (in K)
A_eva=708475900690  #Evaporation constant (in g/m^2*s)
T_vac=300           #Vacuum (inside tube) absolute temperature (in K)


"""Evaporation rate"""
R_eva=A_eva*np.exp(-qo/(K*T_fil))  #Evaporation rate (in g/m^2*s)

"""Pressure buildup"""
t_elap=60*60*24*365*5       #Time elapsed (in s)
m_eva_tot=R_eva*t_elap*A_fil #Total evaporated mass (in g)
n=m_eva_tot/A_tungsten       #Number of moles of evaporated filament
P=n*R_gas*T_vac/V_tube       #Pressure (in atm)

"""Dielectric strength"""
DE_vac=1e12                  #Dielectric strength (in MV/m) of vacuum
DE_air=3                     #Dielectric strength (in MV/m) of air (at 1 atm)
DE=(1-P)*DE_vac +P*DE_air    #Dielectric strength (in MV/m) for arbitrary pressure
V_arc=DE*L_arc               #Arcing voltage (in MV)

print(V_arc)