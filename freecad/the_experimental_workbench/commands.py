# coding: utf-8

r"""commands.py for The Experimental Workbench.

The Experimental Workbench is a new/namespace workbench.

"""

import os
import FreeCAD
import FreeCADGui as Gui
from PySide import QtCore, QtGui


class BaseCommand(object):
    NAME = ""
    ICONDIR = os.path.join(os.path.dirname(__file__), "resources")

    def __init__(self):
        pass

    def IsActive(self):
        if FreeCAD.ActiveDocument is None:
            return False
        else:
            return True

    def Activated(self):
        diag = QtGui.QMessageBox(QtGui.QMessageBox.Information, 'Info MessageBox', f"I am command {self.NAME}")
        diag.setWindowModality(QtCore.Qt.ApplicationModal)
        diag.exec_()

    def GetResources(self):
        return {'Pixmap': self.Pixmap,
                'MenuText': self.MenuText,
                'ToolTip': self.ToolTip}


class Command1(BaseCommand):
    NAME = "Command1"
    Pixmap = os.path.join(BaseCommand.ICONDIR, 'command1.svg')
    MenuText = 'Command 1'
    ToolTip = 'Run Command 1'


class Command2(BaseCommand):
    NAME = "Command2"
    Pixmap = os.path.join(BaseCommand.ICONDIR, 'command2.svg')
    MenuText = 'Command 2'
    ToolTip = 'Run Command 2'


class Command3(BaseCommand):
    NAME = "Command3"
    Pixmap = os.path.join(BaseCommand.ICONDIR, 'command3.svg')
    MenuText = 'Command 3'
    ToolTip = 'Run Command 3'
