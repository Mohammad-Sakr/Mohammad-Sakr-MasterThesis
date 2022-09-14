import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import PhysicsBlock as PB
import ChainModule as CM
import SimulationTrial as ST

class Simulation:
     def __init__(self,StatisticalParameters):
        self.StatisticalParameters=StatisticalParameters
        self.SimulationTrials=[]
        
     def addSimulationTrial(self,SimulationTrial):
        self.SimulationTrials.append(SimulationTrial)
        
     def run(self,SimNum):
        for i in range(SimNum):
            for SimulationTrial in self.SimulationTrials:
                SimulationTrial.simReset()
                SimulationTrial.run()