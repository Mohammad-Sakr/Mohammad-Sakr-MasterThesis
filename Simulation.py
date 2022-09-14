import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import tqdm
import PhysicsBlock as PB
import ChainModule as CM
import SimulationTrial as ST

class Simulation:
     def __init__(self,StatisticalParameters):
        self.StatisticalParameters=StatisticalParameters
        self.SimulationTrials=[]
        self.ChainsNames=[]
        self.results={}
        
     def addSimulationTrial(self,SimulationTrial):
        self.SimulationTrials.append(SimulationTrial)
        
     def getChainsNames(self):
         for SimulationTrial in self.SimulationTrials:
            names=SimulationTrial.getChainsNames()
            for name in names:
                self.ChainsNames.append(name)
         self.ChainsNames=list(set(self.ChainsNames)) #removing duplicates
         
     def run(self,SimNum):
         self.getChainsNames()
         for name in self.ChainsNames:
             self.results[name]=[]
         
         for i in tqdm.tqdm(range(SimNum)):
             for SimulationTrial in self.SimulationTrials:
                 SimulationTrial.simReset()
                 SimulationTrial.applyStats(self.StatisticalParameters)
                 failures=SimulationTrial.run()
                 for name in self.ChainsNames:
                     if failures[name+"Failure"]==True:
                         self.results[name].append(failures[name+"FailureTime"])
             
                         
                 
     def showResults(self):
         #print(self.results)
         for name in self.ChainsNames:
              plt.figure()
              plt.hist(self.results[name], bins='auto')  # arguments are passed to np.histogram
              plt.title("Failures of "+name)
              plt.xlabel("Time (in hours)")
              plt.ylabel("Number of failures")
              plt.show()
                 
                 
                 