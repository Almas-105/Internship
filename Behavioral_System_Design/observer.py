# Real-time Temperature Monitoring

#Observers-temp,alert(trigger)

class TempDisplay:
    def update(self,temp):
        print(f"Temparature Displayed:{temp}")
class AlertSystem:
    def update(self,temp):
        if temp>80:
            print(f"Alert:High Temparature")

#Subject-Temparature Sensor

class TemparatureSensor:
    def __init__(self):
        self._observers=[]
        self._temp=0
    def attach(self,observer):
        self._observers.append(observer)
    def dettach(self,observer):
        self._observers.remove(observer)
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temp)
    def set_temp(self,temp):
        self._temp=temp
        print(f"New Temparature Recorderd:{temp}")
        self.notify_observers()


sensor=TemparatureSensor()
display=TempDisplay()
alert=AlertSystem()

sensor.attach(display)
sensor.attach(alert)

sensor.set_temp(50)
sensor.set_temp(100)
sensor.set_temp(200)