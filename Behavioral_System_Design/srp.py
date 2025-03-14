class EngineDiagnostics:
    def work(self):
        print("Running the diagnostics")

class LogData:
    def save_log(self,data):
        print(f"Saving the file data:{data}")

class Notification:
    def send_email(self,msg):
        print(f"Message: {msg}")

#Control System

class ControlSystem:
    def __init__(self):
        self._engine=EngineDiagnostics()
        self._data=LogData()
        self._email=Notification()

    def working(self):
        self._engine.work()
        self._data.save_log("Important Update")
        self._email.send_email("You have a update")

if __name__=="__main__":
    system=ControlSystem()
    system.working()