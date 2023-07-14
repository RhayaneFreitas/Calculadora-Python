import sys 
from PyQt5.QtWidgets import QApplication 
from appcontroller import ChangeMode

# Code to converter .ui->.py: pyuic5 InterfaceScientific.ui -o InterfaceScientific.py
# Code to converter .ui->.py: pyuic5 InterfaceBasic.ui -o InterfaceBasic.py
# Code to converter .ui->.py: pyuic5 About.ui -o About.py

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mode = ChangeMode()
    ctrl = mode.basic
    ctrl.show()
    app.exec_() 
    