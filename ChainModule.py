import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import PhysicsBlock as PB


class PhysicsChain:
    
    def __init__(self,TubeParameters):
        self.TubeParameters=TubeParameters
        self.PhysicsChainName="default"
        self.PhysicsBlocks=[]
        self.elapsedTime=0
        self.params={}
        self.params['isfailed']=False
        
    def addPhysicsBlock(self,PhysicsBlock):#Please add them in the correct order
        self.PhysicsBlocks.append(PhysicsBlock)
        
    def step(self,tStep,OperationParameters):
        self.elapsedTime=self.elapsedTime+tStep
        for PhysicsBlock in self.PhysicsBlocks:
            PhysicsBlock.evaluate(self.params,tStep,OperationParameters)
            
    def failureCheck(self): #Name it "has failed"
        if self.params['isfailed']==True:
            return True
        else:
            return False
    
    def paramReset(self):
        self.params={}
        self.params['isfailed']=False
        for block in self.PhysicsBlocks:
            block.resetBlock()
        
    def getTotalElapsedTime(self):
        return self.elapsedTime
            
    def applyStats(self,actualTubePars):
        for PhysicsBlock in self.PhysicsBlocks:
            PhysicsBlock.applyStats(actualTubePars)




class ArcingChain(PhysicsChain):
    
    def __init__(self,TubeParameters):
        self.TubeParameters=TubeParameters
        self.PhysicsChainName="ArcingChain"
        self.PhysicsBlocks=[]
        self.elapsedTime=0
        self.params={}
        self.params['isfailed']=False
        self.PhysicsBlocks.append(PB.EvaporationRate(TubeParameters['qo'], TubeParameters['A_eva']))
        self.PhysicsBlocks.append(PB.PressureBuildup(TubeParameters['A_fil'],TubeParameters['V_tube'],TubeParameters['T_vac']))
        self.PhysicsBlocks.append(PB.Outgassing(TubeParameters['A_tube'],TubeParameters['V_tube'],TubeParameters['AAOR']))
        self.PhysicsBlocks.append(PB.Arcing(TubeParameters['L_arc']))
    


class FilamentBurn(PhysicsChain):
    
    def __init__(self,TubeParameters):
        self.TubeParameters=TubeParameters
        self.PhysicsChainName="FilamentBurn"
        self.PhysicsBlocks=[]
        self.elapsedTime=0
        self.params={}
        self.params['isfailed']=False
        self.PhysicsBlocks.append(PB.EvaporationRate(TubeParameters['qo'], TubeParameters['A_eva']))
        self.PhysicsBlocks.append(PB.FilamentEvaporation(TubeParameters['r_fil'],TubeParameters['R_fil'],TubeParameters['NumPitches'],TubeParameters['rho_fil']))


class FilamentBurn2(PhysicsChain):
    
    def __init__(self,TubeParameters):
        self.TubeParameters=TubeParameters
        self.PhysicsChainName="FilamentBurn2"
        self.PhysicsBlocks=[]
        self.elapsedTime=0
        self.params={}
        self.params['isfailed']=False
        self.PhysicsBlocks.append(PB.FilamentEvaporationAtConstCurrent(TubeParameters['qo'], TubeParameters['A_eva'],TubeParameters['r_fil'],TubeParameters['R_fil'],TubeParameters['NumPitches'],TubeParameters['rho_fil']))

                
# class PhysicsChainTest1(PhysicsChain):
#     def __init__(self,TubeParameters,PhysicsParameters):
#         self.TubeParameters=TubeParameters
#         self.PhysicsParameters=PhysicsParameters
#         self.PhysicsChainName="PhysicsChainTest1"
#         self.PhysicsBlocks=[]
#         self.PhysicsBlocks.append(PB.TestBlock3(1))
#         self.PhysicsBlocks.append(PB.TestBlock2(1))
#         self.PhysicsBlocks.append(PB.TestBlock3(1))
#         self.params={}
#         self.params['Test1']=1
        
#     def failureCheck(self):
#         if self.params['Test1']>50:
#             return True
#         return False    
    
#     def paramReset(self):
#         self.params={}
#         self.params['Test1']=1
    
# class PhysicsChainTest2(PhysicsChain):
#     def __init__(self,TubeParameters,PhysicsParameters):
#         self.TubeParameters=TubeParameters
#         self.PhysicsParameters=PhysicsParameters
#         self.PhysicsChainName="PhysicsChainTest2"
#         self.PhysicsBlocks=[]
#         self.PhysicsBlocks.append(PB.TestBlock3(1))
#         self.PhysicsBlocks.append(PB.TestBlock2(1))
#         self.PhysicsBlocks.append(PB.TestBlock3(1))
#         self.PhysicsBlocks.append(PB.TestBlock2(1))
#         self.PhysicsBlocks.append(PB.TestBlock3(1))
#         self.params={}
#         self.params['Test1']=1
        
#     def failureCheck(self):
#         if self.params['Test1']>5000:
#             return True
#         return False    
    
#     def paramReset(self):
#         self.params={}
#         self.params['Test1']=1
        
    
# class PhysicsChainTest3(PhysicsChain):
#     def __init__(self,TubeParameters,PhysicsParameters):
#         self.TubeParameters=TubeParameters
#         self.PhysicsParameters=PhysicsParameters
#         self.PhysicsChainName="PhysicsChainTest3"
#         self.PhysicsBlocks=[]
#         self.PhysicsBlocks.append(PB.TestBlock3(1))
#         self.params={}
#         self.params['Test1']=1
        
#     def failureCheck(self):
#         if self.params['Test1']>8:
#             return True
#         return False   
    
#     def paramReset(self):
#         self.params={}
#         self.params['Test1']=1