#We'll build a system where different types of notifications 
# (e.g., Email, SMS, and Push Notification) are created using a Factory Design Pattern

from abc import ABC, abstractmethod

#abstract class

class Notification(ABC):
    @abstractmethod
    def notify(self,message:str):
        pass

#concrete class

class EmailNotification(Notification):
    def notify(self,message:str):
        print(f"Email Notification:{message}")
    
class SMSNotification(Notification):
    def notify(self,message:str):
        print(f"SMS Notification:{message}")

#factory

class NotificationFactory:
    def create_notification(self,notification:str)->Notification:
        if notification=='email':
            return EmailNotification()
        elif notification=='sms':
            return SMSNotification()
        else:
            return ValueError("Invalid Notification Type")

#client

if __name__=="__main__":
    factory=NotificationFactory()
    type=input("Enter the type of Notification:").strip().lower()
    notification=factory.create_notification(type)
    notification.notify("You got a Notification!!!!")
