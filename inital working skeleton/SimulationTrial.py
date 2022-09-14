import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import PhysicsBlock as PB
import ChainModule as CM

class SimulationTrial:
     def __init__(self,TubeParameters,OperationParameters,StepsNum):
        self.TubeParameters=TubeParameters
        self.OperationParameters=OperationParameters
        self.StepsNum=StepsNum
        self.PhysicsChains=[]
        self.failure={}
        
     def addPhysicsChain(self,PhysicsChain):
        self.PhysicsChains.append(PhysicsChain)
        
     def run(self):
         
         for PhysicsChain in self.PhysicsChains:
             self.failure[PhysicsChain.PhysicsChainName]=False
             
         for i in range(self.StepsNum):
             for PhysicsChain in self.PhysicsChains:
                 if PhysicsChain.failureCheck():
                     if self.failure[PhysicsChain.PhysicsChainName]==False:
                         self.failure[PhysicsChain.PhysicsChainName]=True
                         self.failure[PhysicsChain.PhysicsChainName+"Step"]=i-1
                 else:
                     PhysicsChain.step(self.OperationParameters)
         print(self.failure)
         
     def simReset(self):
         for PhysicsChain in self.PhysicsChains:
             PhysicsChain.paramReset()
         self.failure={}
         
         
                 