# vrPySideExample

from PySide2 import QtWidgets
from PySide2 import QtCore

def vredMainWindow(id):
    from shiboken2 import wrapInstance
    return wrapInstance(id, QtWidgets.QMainWindow)

class CustomMenu():
    def __init__(self, mw):
        self.mw = mw
        self.testAction = QtWidgets.QAction(mw.tr("Test"), mw)
        self.testAction.triggered.connect(self.test)

        self.menu = QtWidgets.QMenu(mw.tr("Scripts"), mw)
        self.menu.addAction(self.testAction)
        
        # insert new menu before Help.
        actions = mw.menuBar().actions()
        for action in actions:
            if action.text() == mw.tr("&Help"):
                mw.menuBar().insertAction(action, self.menu.menuAction())
                break

    def __del__(self):
        self.mw.menuBar().removeAction(self.menu.menuAction())

    def test(self):
        print "TEST!"

customMenu = CustomMenu(vredMainWindow(VREDMainWindowId))
