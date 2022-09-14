import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import PhysicsBlock as PB
import ChainModule as CM
import SimulationTrial as ST
import Simulation as S

#organize the models
#Look it up (google) 6.4 in python docs

params={}
Test1=PB.TestBlock1(1)
Test1.evaluate(params,0)

phyChain=CM.PhysicsChain(0,0)
phyChain.addPhysicsBlock(PB.TestBlock2(1))
phyChain.addPhysicsBlock(PB.TestBlock3(2))
phyChain.addPhysicsBlock(PB.TestBlock2(3))
phyChain.addPhysicsBlock(PB.TestBlock3(4))
phyChain.step(0)


phyChain1=CM.PhysicsChainTest1(0,0)
phyChain1.step(0)
print(phyChain1.failureCheck())
phyChain1.step(0)
print(phyChain1.failureCheck())
phyChain1.step(0)
print(phyChain1.failureCheck())
phyChain1.step(0)
print(phyChain1.failureCheck())

SimTri=ST.SimulationTrial(0,0,10)
SimTri.addPhysicsChain(CM.PhysicsChainTest1(0,0))
SimTri.addPhysicsChain(CM.PhysicsChainTest2(0,0))
SimTri.addPhysicsChain(CM.PhysicsChainTest3(0,0))
SimTri.run()

Sim=S.Simulation(0)
Sim.addSimulationTrial(SimTri)
Sim.run(3)

#Put a clear "Hello world" example
#Start implemetning a physics chain and then test them (only one chain first)






