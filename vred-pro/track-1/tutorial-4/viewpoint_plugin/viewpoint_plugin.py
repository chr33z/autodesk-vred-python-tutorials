from PySide2 import QtCore, QtGui, QtWidgets

import os
import random
import threading

# Import vred modules in a try-catch block to prevent any errors
# Abort plugin initialization when an error occurs
importError = False
try:
    import vrController
    import vrFileIO
    import vrMovieExport
    import vrFileDialog
    import vrRenderSettings
except ImportError:
    importError = True
    pass

import uiTools

# Load a pyside form and the widget base from a ui file that describes the layout 
form, base = uiTools.loadUiType('viewpoint_plugin.ui')

class vrViewpointPlugin(form, base):
    """
    Main plugin class

    Inherits from fhe form and the widget base that was generated from the ui-file
    """
    
    def __init__(self, parent=None):
        """Setup and connect the plugins user interface"""

        super(vrViewpointPlugin, self).__init__(parent)
        parent.layout().addWidget(self)
        self.parent = parent
        self.setupUi(self)
        self.setupUserInterface()

        # Initialize some class variables that we need for our loop function
        self.loopCounter = 0
        self.loopRunning = False


    def setupUserInterface(self):
        """Setup and connect the plugins user interface"""

        self._render_all.clicked.connect(self.renderViewpoints)

        self._random_viewpoint.clicked.connect(self.selectRandomViewpoint)
        self._random_viewpoint.setIcon(QtGui.QIcon("icon_random_viewpoint.png"))
        self._random_viewpoint.setIconSize(QtCore.QSize(32,32))

        self._loop_viewpoints.clicked.connect(self.loopViewpoints)


    def renderViewpoints(self):
        """
        Open a directory dialog and then render all viewpoints to that directory
        """

        print("[Viewpoint Plugin] Render all viewpoints...")
        renderDirectory = vrFileDialog.getExistingDirectory("Select a render directory:", vrFileIO.getFileIOBaseDir())
        if not renderDirectory:
            print("No directory where to save the renderings!")
            return

        viewpoints = vrCameraService.getAllViewpoints()
        for viewpoint in viewpoints:
            name = viewpoint.getName()
            viewpoint.activate()
            print("{}/{}.jpg".format(renderDirectory, name))
            vrRenderSettings.setRenderFilename("{}/{}.jpg".format(renderDirectory, name))
            vrRenderSettings.startRenderToFile(False)

        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Finished Rendering Viewpoints")
        msgBox.setInformativeText("Finished Rendering Viewpoints. Do you want to open the render directory?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        ret = msgBox.exec_()

        if ret == QtWidgets.QMessageBox.Ok:
            os.startfile(renderDirectory)


    def selectRandomViewpoint(self):
        """ Select a random viewpoint from all viewpoints """

        print("[Viewpoint Plugin] Select a random viewpoint...")

        viewpoints = vrCameraService.getAllViewpoints()
        randomViewpoint = random.choice(viewpoints)
        randomViewpoint.activate()


    def loopViewpoints(self):
        """
        Loops through all viewpoints once. Stops looping when the button is pressed again
        """

        # When a loop is already running, then cancel the loop
        if self.loopRunning:
            print("[Viewpoint Plugin] Stop loop...")
            self.__setLoopViewpointLabel("Loop Viewpoints")

            self.loopRunning = False
            return

        # Otherwise start a new loop
        if self.loopCounter == 0 and not self.loopRunning:
            print("[Viewpoint Plugin] Loop all viewpoints...")
            self.__setLoopViewpointLabel("Stop Loop")

            viewpoints = vrCameraService.getAllViewpoints()
            self.loopCounter = len(viewpoints) - 1
            self.loopRunning = True
            threading.Timer(1.0, self.__loopNextViewpoint).start()


    def __loopNextViewpoint(self):
        """
        Loops through all viewpoints once. Stops looping when the button is pressed again
        """

        if self.loopCounter == 0 or not self.loopRunning:
            self.loopRunning = False
            self.loopCounter = 0
            return

        viewpoints = vrCameraService.getAllViewpoints()
        viewpoints[self.loopCounter].activate()
        self.loopCounter = self.loopCounter - 1
        threading.Timer(2.0, self.__loopNextViewpoint).start()


    def __setLoopViewpointLabel(self, labelText):
        """ Change the text of the "loop" button """

        self._loop_viewpoints.setText(labelText)

# Actually start the plugin
if not importError:
    viewpointPlugin = vrViewpointPlugin(VREDPluginWidget)