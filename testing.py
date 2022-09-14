import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import PhysicsBlock as PB
import ChainModule as CM
import SimulationTrial as ST
import Simulation as S

#organize the models
#Look it up (google) 6.4 in python docs

# params={}
# Test1=PB.TestBlock1(1)
# Test1.evaluate(params,0)

# phyChain=CM.PhysicsChain(0,0)
# phyChain.addPhysicsBlock(PB.TestBlock2(1))
# phyChain.addPhysicsBlock(PB.TestBlock3(2))
# phyChain.addPhysicsBlock(PB.TestBlock2(3))
# phyChain.addPhysicsBlock(PB.TestBlock3(4))
# phyChain.step(0)


# phyChain1=CM.PhysicsChainTest1(0,0)
# phyChain1.step(0)
# print(phyChain1.failureCheck())
# phyChain1.step(0)
# print(phyChain1.failureCheck())
# phyChain1.step(0)
# print(phyChain1.failureCheck())
# phyChain1.step(0)
# print(phyChain1.failureCheck())

# SimTri=ST.SimulationTrial(0,0,10)
# SimTri.addPhysicsChain(CM.PhysicsChainTest1(0,0))
# SimTri.addPhysicsChain(CM.PhysicsChainTest2(0,0))
# SimTri.addPhysicsChain(CM.PhysicsChainTest3(0,0))
# SimTri.run()

# Sim=S.Simulation(0)
# Sim.addSimulationTrial(SimTri)
# Sim.run(3)

#Put a clear "Hello world" example
#Start implemetning a physics chain and then test them (only one chain first)

TubeParameters={
        'L_arc':0.01     ,           #The distance (in m) between cathode and anode
        'V_tube':(0.02*0.02)/4*0.05*3.14159*1000    ,           #Total volume (in L) of the tube
        'A_fil':0.0001      ,           #Total outer area (in m^2) of the filament
        'qo':1.33308e-18            ,           #Energy (in J) of evaporation per atom of metal (at T=0)
        'A_eva':667000496816.4105      ,           #Evaporation constant (in g/m^2*s)
        'T_vac':300      ,           #Vacuum (inside tube) absolute temperature (in K)
        'A_tube':0   ,           #Total inner area of the tube (in m^2)
        'AAOR':0     ,             #Average area outgassing rate (in mbar.l/s/cm^2)
        'r_fil':0.25/1000   ,
        'R_fil':2/1000 ,
        'NumPitches':25  ,
        'rho_fil':19.3    #Filament density (in g/cm^3)
    #Tol: -+5% for all mechanical parameters (vacuum -+1%)
    }
StatisticalParameters={
        'L_arc':5     ,           #The distance (in m) between cathode and anode
        'V_tube':5    ,           #Total volume (in L) of the tube
        'A_fil':5      ,           #Total outer area (in m^2) of the filament
        'qo':0            ,           #Energy (in J) of evaporation per atom of metal (at T=0)
        'A_eva':0      ,           #Evaporation constant (in g/m^2*s)
        'T_vac':1      ,           #Vacuum (inside tube) absolute temperature (in K)
        'A_tube':5   ,           #Total inner area of the tube (in m^2)
        'AAOR':5     ,             #Average area outgassing rate (in mbar.l/s/cm^2)
        'r_fil':5   ,
        'R_fil':5 ,
        'NumPitches':0  ,
        'rho_fil':0    #Filament density (in g/cm^3)
    }
OperationParameters={
        'T_fil':2300,           #Filament absolute temperature (in K)
        'V_anode':50            #Applied anode voltage (in kV)
    }


SimTri=ST.SimulationTrial(TubeParameters,OperationParameters,10000000,10000)
#SimTri.addPhysicsChain(CM.ArcingChain(TubeParameters))
#SimTri.addPhysicsChain(CM.FilamentBurn(TubeParameters))
SimTri.addPhysicsChain(CM.FilamentBurn2(TubeParameters))



Sim=S.Simulation(StatisticalParameters)
Sim.addSimulationTrial(SimTri)
Sim.run(1)
Sim.showResults()

#2*2/1000*3.14159*25*60*1e-6/100/((0.25/1000)*(0.25/1000)*3.14159)


