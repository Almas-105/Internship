class DiagonosticSystem:
    def run_diagnostic(self):
        return "Running Diagnosis"

#Base

class BaseDiagonosticSystem:
    def __init__(self,diagnostic_system):
        self._diagnostic_system=diagnostic_system
    def run_diagnostic(self):
        return self._diagnostic_system.run_diagnostic()
    
#Concrete Decorators

class AlertSystem(BaseDiagonosticSystem):
    def run_diagnostic(self):
        return self._diagnostic_system.run_diagnostic()+"\n Alert System Activated: Critical issues found!!"
    
class DataLogger(BaseDiagonosticSystem):
    def run_diagnostic(self):
        return self._diagnostic_system.run_diagnostic()+"\nData Logger: Data is saved in the Data Logger"
    
class PerformanceOptimizer(BaseDiagonosticSystem):
    def run_diagnostic(self):
        return self._diagnostic_system.run_diagnostic()+"\nPerformace efiiciency improved"
    
#Client Code

diag=DiagonosticSystem()
print(diag.run_diagnostic())

alert_diag=AlertSystem(diag)
print(alert_diag.run_diagnostic())

alert_data_diag=DataLogger(alert_diag)
print(alert_data_diag.run_diagnostic())

alert_data_perf=PerformanceOptimizer(alert_data_diag)
print(alert_data_perf.run_diagnostic())


        

