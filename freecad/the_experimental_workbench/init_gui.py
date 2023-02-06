# coding: utf-8

r"""init_gui.py for The Experimental Workbench.

The Experimental Workbench is a new/namespace workbench.

"""

import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.the_experimental_workbench import ICONPATH


class TheExperimentalWorkbench(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """

    MenuText = "The Experimental Workbench"
    ToolTip = "A workbench used to experiment and learn"
    Icon = os.path.join(ICONPATH, "the_experimental_workbench_icon.svg")
    commands = [
        "Command1",
        "Command2",
        "Command3"]

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        from freecad.the_experimental_workbench import my_numpy_function

        from .commands import Command1, Command2, Command3

        App.Console.PrintMessage("switching to workbench_starterkit\n")
        App.Console.PrintMessage("run a numpy function: sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))

        self.appendToolbar("Experimental WB", self.commands)
        self.appendMenu("Experimental WB", self.commands)

        Gui.addCommand('Command1', Command1())
        Gui.addCommand('Command2', Command2())
        Gui.addCommand('Command3', Command3())

    def Activated(self):
        """Code which should be computed when a user switch to this workbench."""
        pass

    def Deactivated(self):
        """Code which should be computed when this workbench is deactivated."""
        pass


Gui.addWorkbench(TheExperimentalWorkbench())
