import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import PhysicsBlock as PB
import ChainModule as CM

class SimulationTrial:
     def __init__(self,TubeParameters,OperationParameters,StepsNum,tStep):
        self.TubeParameters=TubeParameters
        self.OperationParameters=OperationParameters
        self.StepsNum=StepsNum
        self.tStep=tStep
        self.PhysicsChains=[]
        self.failure={}
        
     def addPhysicsChain(self,PhysicsChain):
        self.PhysicsChains.append(PhysicsChain)
        
     def run(self):
         
         for PhysicsChain in self.PhysicsChains:
             self.failure[PhysicsChain.PhysicsChainName+"Failure"]=False
             
         for i in range(self.StepsNum):
             for PhysicsChain in self.PhysicsChains:
                 if PhysicsChain.failureCheck():
                     if self.failure[PhysicsChain.PhysicsChainName+"Failure"]==False:
                         self.failure[PhysicsChain.PhysicsChainName+"Failure"]=True
                         self.failure[PhysicsChain.PhysicsChainName+"FailureStep"]=i-1
                         self.failure[PhysicsChain.PhysicsChainName+"FailureTime"]=(i-1)*self.tStep/3600
                         
                 else:
                     PhysicsChain.step(self.tStep,self.OperationParameters)
         return self.failure
         
     def simReset(self):
         for PhysicsChain in self.PhysicsChains:
             PhysicsChain.paramReset()
         self.failure={}
         
     def getChainsNames(self):
         names=[]
         for PhysicsChain in self.PhysicsChains:
             names.append(PhysicsChain.PhysicsChainName)
         return names
         
     def applyStats(self,StatisticalParameters):
         actualTubePars={}
         for parName in self.TubeParameters.keys():
             deviation=StatisticalParameters[parName]/100*(np.random.normal(0, 1, 1))+1
             actualTubePars[parName]=self.TubeParameters[parName]*deviation
         for PhysicsChain in self.PhysicsChains: 
                 PhysicsChain.applyStats(actualTubePars)