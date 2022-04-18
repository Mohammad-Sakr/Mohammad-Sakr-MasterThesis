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
L_arc=0.001         #The distance (in m) between cathode and anode
V_tube=0.00001      #Total volume (in L) of the tube
A_fil=0.0001        #Total outer area (in m^2) of the filament
qo=1.33308e-18      #Energy (in J) of evaporation per atom of metal (at T=0)
T_fil=2000          #Filament absolute temperature (in K)
A_eva=708475900690  #Evaporation constant (in g/m^2*s)
T_vac=300           #Vacuum (inside tube) absolute temperature (in K)


"""Evaporation rate"""
R_eva=A_eva*np.exp(-qo/(K*T_fil))  #Evaporation rate (in g/m^2*s)

"""Pressure buildup"""
t_elap=60*60*24*365*5 #Time elapsed (in s)
m_eva_tot=R_eva*t_elap*A_fil #Total evaporated mass (in g)
n=m_eva_tot/A_tungsten #Number of moles of evaporated filament
P=n*R_gas*T_vac/V_tube #Pressure (in atm)




"""
a=30
N=1000
x=np.linspace(-a,a,N)
y=np.array([1 if np.abs(n)<=1 else 0 for n in x])

Tstep=2*a/N
X=np.linspace(-1/(Tstep*2),1/(Tstep*2),N)
Y=scipy.fft.fftshift(scipy.fft(y))


plt.figure()
plt.plot(x,y)
plt.show()

plt.figure()
plt.plot(X,np.abs(Y))
plt.show()
"""
