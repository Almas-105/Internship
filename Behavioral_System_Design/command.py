#Smart Home Controller where you can:
#  Turn ON the Light
#  Turn OFF the Light
#  Undo the Last Command

from abc import ABC,abstractmethod

#command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass

#Receiver-Light

class Light:
    def turn_on(self):
        print("Light is ON")
    def turn_off(self):
        print("Light is Off")

#Concrete Command Class
class LightOnCommand(Command):
    def __init__(self,light:Light):
        self.light=light
    def execute(self):
        self.light.turn_on()
    def undo(self):
        self.light.turn_off()
class LightOffCommand(Command):
    def __init__(self,light:Light):
        self.light=light
    def execute(self):
        self.light.turn_off()
    def undo(self):
        self.light.turn_on()
    

#Invoker

class RemoteControl:
    def __init__(self):
        self.history=[]
    def press_button(self,command:Command):
        command.execute()
        self.history.append(command)
    def press_undo(self):
        if self.history:
            command=self.history.pop()
            command.undo()
        else:
            print("Nothing to undo")


if __name__=="__main__":
    light=Light()
    light_on=LightOnCommand(light)
    light_off=LightOffCommand(light)

    remote=RemoteControl()
    remote.press_button(light_on)
    remote.press_button(light_off)

    remote.press_undo()
    remote.press_undo()
    remote.press_undo()