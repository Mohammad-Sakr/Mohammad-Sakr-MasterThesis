import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import PhysicsBlock as PB


class PhysicsChain:
    
    def __init__(self,TubeParameters,PhysicsParameters):
        self.TubeParameters=TubeParameters
        self.PhysicsParameters=PhysicsParameters
        self.PhysicsChainName="default"
        self.PhysicsBlocks=[]
        self.params={}
        self.params['Test1']=1
        
    def addPhysicsBlock(self,PhysicsBlock):#Please add them in the correct order
        self.PhysicsBlocks.append(PhysicsBlock)
        
    def step(self,OperationParameters):
        for PhysicsBlock in self.PhysicsBlocks:
            PhysicsBlock.evaluate(self.params,OperationParameters)
            
    def failureCheck(self): #Name it "has failed"
        #This should be defined solely for each chain
        return False
    
    def paramReset(self):
        self.params={}
            
class PhysicsChainTest1(PhysicsChain):
    def __init__(self,TubeParameters,PhysicsParameters):
        self.TubeParameters=TubeParameters
        self.PhysicsParameters=PhysicsParameters
        self.PhysicsChainName="PhysicsChainTest1"
        self.PhysicsBlocks=[]
        self.PhysicsBlocks.append(PB.TestBlock3(1))
        self.PhysicsBlocks.append(PB.TestBlock2(1))
        self.PhysicsBlocks.append(PB.TestBlock3(1))
        self.params={}
        self.params['Test1']=1
        
    def failureCheck(self):
        if self.params['Test1']>50:
            return True
        return False    
    
    def paramReset(self):
        self.params={}
        self.params['Test1']=1
    
class PhysicsChainTest2(PhysicsChain):
    def __init__(self,TubeParameters,PhysicsParameters):
        self.TubeParameters=TubeParameters
        self.PhysicsParameters=PhysicsParameters
        self.PhysicsChainName="PhysicsChainTest2"
        self.PhysicsBlocks=[]
        self.PhysicsBlocks.append(PB.TestBlock3(1))
        self.PhysicsBlocks.append(PB.TestBlock2(1))
        self.PhysicsBlocks.append(PB.TestBlock3(1))
        self.PhysicsBlocks.append(PB.TestBlock2(1))
        self.PhysicsBlocks.append(PB.TestBlock3(1))
        self.params={}
        self.params['Test1']=1
        
    def failureCheck(self):
        if self.params['Test1']>5000:
            return True
        return False    
    
    def paramReset(self):
        self.params={}
        self.params['Test1']=1
        
    
class PhysicsChainTest3(PhysicsChain):
    def __init__(self,TubeParameters,PhysicsParameters):
        self.TubeParameters=TubeParameters
        self.PhysicsParameters=PhysicsParameters
        self.PhysicsChainName="PhysicsChainTest3"
        self.PhysicsBlocks=[]
        self.PhysicsBlocks.append(PB.TestBlock3(1))
        self.params={}
        self.params['Test1']=1
        
    def failureCheck(self):
        if self.params['Test1']>8:
            return True
        return False   
    
    def paramReset(self):
        self.params={}
        self.params['Test1']=1