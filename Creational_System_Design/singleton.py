#Using  metaclass for implementing singleton

class SingletonMeta(type):
    _instances={}

    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls]=super().__call__(*args,**kwargs)
            print("New Singleton Instance Created")
        return cls._instances[cls]
class Logger(metaclass=SingletonMeta):
    def log(self,message):
        print(f"[LOG]:{message}")


logger1=Logger()
logger2=Logger()

logger1.log("First Log Entry")
logger2.log("Second Log Entry")

print(logger1==logger2)