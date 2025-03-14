#In an air traffic control system, multiple aircraft communicate with a control tower (mediator) instead of directly with one another.
# System Requirements:
# Aircraft must request landing or takeoff permissions.
# The control tower ensures no two planes attempt the same operation simultaneously.
# If one plane is landing, other planes must wait for clearance.


from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def req_landing(self):
        pass
    def req_takeoff(self):
        pass

class ControlRoom(Mediator):
    def __init__(self):
        self.aircraft_queue=[]

    def req_landing(self,aircraft):
        if not self.aircraft_queue:
            print(f"{aircraft.name} is clear to land ")
        else:
            print(f"{aircraft.name} is waiting to land")
        self.aircraft_queue.append(aircraft)

    def req_takeoff(self,aircraft):
        if self.aircraft_queue and self.aircraft_queue[0]==aircraft:
            print(f"{aircraft.name} is clear for takeoff")
            self.aircraft_queue.pop(0)
        else:
            print(f"{aircraft.name} mus wait for clearance")

class AirCraft:
    def __init__(self,name,mediator:Mediator):
        self.name=name
        self.mediator=mediator
    def req_landing(self):
        print(f"{self.name} requests landing")
        self.mediator.req_landing(self)

    def req_takeoff(self):
        print(f"{self.name} requests takeoff")
        self.mediator.req_takeoff(self)

if __name__=="__main__":
    control=ControlRoom()

    aircraft1=AirCraft("Flight1",control)
    aircraft2=AirCraft("Flight2",control)
    aircraft3=AirCraft("Flight3",control)

    aircraft1.req_landing()
    aircraft2.req_landing()
    aircraft3.req_landing()

    aircraft1.req_takeoff()
    aircraft2.req_takeoff()
    aircraft3.req_takeoff()