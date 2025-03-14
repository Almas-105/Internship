from abc import ABC,abstractmethod

class AirCraftSetup(ABC):
    def sequence(self):
        self.poweron()
        self.systemcheck()
        self.enginecheck()
        self.flight_control()
        self.communicationcheck()

    def poweron(self):
        print("Step1: Power Check is done")

    def flight_control(self):
        print("Step4: Flight control: Nominal")
    def communicationcheck(self):
        print("Step 5: Communication done")

    @abstractmethod
    def systemcheck(self):
        pass

    @abstractmethod
    def enginecheck(self):
        pass

class Passenger(AirCraftSetup):
    def systemcheck(self):
        print("Step 2: Passenger system checked")
    def enginecheck(self):
        print("Step 3: Passenger engine is checked")

class CargoFlight(AirCraftSetup):
    def systemcheck(self):
        print("Step2: Cargo Flight system checked")
    def enginecheck(self):
        print("Step3: Cargo Flight engine is checked")

class FighterJet(AirCraftSetup):
    def systemcheck(self):
        print("Step2: FighterJet system is checked")
    def enginecheck(self):
        print("Step 3: FighterJet engine is checked")

if __name__=="__main__":

    passenger=Passenger()
    print("\nPassenger Flight")
    passenger.sequence()

    cargo=CargoFlight()
    print("\nCargo Flight")
    cargo.sequence()

    jet=FighterJet()
    print("\nFighter Jet Flight")
    jet.sequence()