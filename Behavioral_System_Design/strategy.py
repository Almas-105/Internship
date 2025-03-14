from abc import ABC, abstractmethod

class Landing(ABC):
    @abstractmethod
    def deploy(self):
        pass

#Strategy Classes

class NormalLanding(Landing):
    def deploy(self):
        return "Normal Landing"
    
class EmergencyLanding(Landing):
    def deploy(self):
        return "Emergency Landing"
class TerrainLanding(Landing):
    def deploy(self):
        return "Terrain Mode Landing"
    
#Context Class where the strategy selection is done

class ControlSystem:
    def __init__(self,strategy:Landing):
        self._strategy=strategy
    def set_strategy(self,strategy:Landing):
        self._strategy=strategy
    def deploy_landing(self):
        return self._strategy.deploy()

#Client

if __name__=="__main__":

    system=ControlSystem(NormalLanding())
    print(system.deploy_landing())

    system.set_strategy(EmergencyLanding())
    print(system.deploy_landing())

    system.set_strategy(TerrainLanding())
    print(system.deploy_landing())
        