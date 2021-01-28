import vrFileIO
import vrFileDialog
import vrRenderSettings
from PySide2 import QtCore, QtWidgets
from shiboken2 import wrapInstance

def vredMainWindow(): 
    main_window_ptr = getMainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QMainWindow)

class CustomDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        boxlayout = QtWidgets.QVBoxLayout(self)

        self.lineedit = QtWidgets.QLineEdit()
        boxlayout.addWidget(self.lineedit)

        self.button = QtWidgets.QPushButton("Set Label")
        self.button.clicked.connect(self.buttonClicked)
        boxlayout.addWidget(self.button)

        self.label = QtWidgets.QLabel()
        boxlayout.addWidget(self.label)

        self.setLayout(boxlayout)

    def buttonClicked(self):
        self.label.setText(self.lineedit.text())
        self.lineedit.setText("")


def renderViewpoints():
    renderDirectory = vrFileDialog.getExistingDirectory("Select a render directory:", vrFileIO.getFileIOBaseDir())

    if not renderDirectory:
        print("No directory where to save the renderings!")
        return

    viewpoints = vrCameraService.getAllViewpoints()
    for viewpoint in viewpoints:
        name = viewpoint.getName()
        vrRenderSettings.setRenderFilename("{}.jpg".format(name))
        vrRenderSettings.startRenderToFile(False)


dialog = CustomDialog(vredMainWindow())
dialog.show()
