#We'll create a system that generates UI components (like buttons and checkboxes) for different operating systems (Windows and Mac).

from abc import ABC,abstractmethod

#abstract class

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class CheckBox(ABC):
    @abstractmethod
    def render(self):
        pass


#Concrete

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows-style Button"
class MacButton(Button):
    def render(self):
        return "Rendering Mac-style Button"
class WindowsCheckBox(CheckBox):
    def render(self):
        return "Rendering Windows-style Checkbox"
class MacCheckBox(CheckBox):
    def render(self):
        return "Rendering Mac-style CheckBox"
    
#Factory

class UIFactory:
    @abstractmethod
    def create_button(self)->Button:
        pass
    def create_checkbox(self)->CheckBox:
        pass
class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()
    def create_checkbox(self):
        return WindowsCheckBox()
class MacFactory(UIFactory):
    def  create_button(self):
        return MacButton()
    def create_checkbox(self):
        return MacCheckBox()
    
def render_ui(factory:UIFactory):
    button=factory.create_button()
    checkbox=factory.create_checkbox()

    print(button.render())
    print(checkbox.render())

if __name__=="__main__":
    os_type=input("Enter the OS (mac/windows):").strip().lower()
    if os_type=="windows":
        factory=WindowsFactory()
    elif os_type=="mac":
        factory=MacFactory()
    else:
        print("Invalid Choice")
    render_ui(factory)