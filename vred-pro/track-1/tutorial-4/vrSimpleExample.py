# vrSimpleExample

from PySide2 import QtCore, QtGui, QtWidgets

importError = False
try:
    import vrController
    import vrFileIO
    import vrMovieExport
except ImportError:
    importError = True
    pass

import uiTools

vrSimpleExample_form, vrSimpleExample_base = uiTools.loadUiType('vrSimpleExampleGUI.ui')

class vrSimpleExample(vrSimpleExample_form, vrSimpleExample_base):
    def __init__(self, parent=None):
        super(vrSimpleExample, self).__init__(parent)
        parent.layout().addWidget(self)
        self.parent = parent
        self.setupUi(self)

        # add resize grip in bottom right corner.
        self.sizeGrip = QtWidgets.QSizeGrip(parent);
        self.sizeGrip.setFixedSize(16, 16)
        self.sizeGrip.move(parent.rect().bottomRight() - self.sizeGrip.rect().bottomRight())
        self.sizeGrip.raise_()
        self.sizeGrip.show()

        vrMessageService.message.connect(self.receivedMessage)
        self._new_scene.clicked.connect(self.newScene)
        self._load_scene.clicked.connect(self.loadScene)
        self._create_snapshot.clicked.connect(self.createSnapshot)

    def resizeEvent(self, event):
        # move resize grip to bottom right corner.
        self.sizeGrip.move(self.parent.rect().bottomRight() - self.sizeGrip.rect().bottomRight())
        self.sizeGrip.raise_()

    def receivedMessage(self, id, args):
        if id == vrController.VRED_MSG_LOADED_GEOMETRY:
            if 'filename' in args:
                print('Loaded file ' + args['filename'])
            else:
                print('Loaded file')

    def newScene(self):
        print("newScene")
        vrController.newScene()

    def loadScene(self):
        filename = vrFileIO.getVREDExamplesDir() + "/vred-test-scene.vpb"
        vrFileIO.load(filename)

    def createSnapshot(self):
        vrMovieExport.createSnapshot("c:/test.png", 640, 512)

if not importError:
    simpleExample = vrSimpleExample(VREDPluginWidget)
