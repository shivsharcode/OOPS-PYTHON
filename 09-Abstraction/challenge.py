
from abc import ABC, abstractmethod

class Notification(ABC):
    
    @abstractmethod
    def send(self, message):
        print("Preparing notification...")
        

class EmailNotification(Notification):
    
    # overriding send
    def send(self, message):
        super().send(message)
        print(f"Sending Email: {message}")
        

class SMSNotification(Notification):
    
    # overriding send
    def send(self, message):
        super().send(message)
        print(f"Sending SMS: {message}")
        

def notify(user_notification, message):
    user_notification.send(message)
    
    
notify(EmailNotification(), "Hello Shivam")
notify(SMSNotification(), "OTP: 1234")
