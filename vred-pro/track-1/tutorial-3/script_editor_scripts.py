# Example 1.0
# Global function library

import time
from datetime import datetime


def logInfo(message):
    now = datetime.now().time().strftime("%H:%M:%S.%f")
    print(now, '[INFO]', message)


def logWarn(message):
    now = datetime.now().time().strftime("%H:%M:%S.%f")
    print(now, '[WARN]', message)


def createViewpointFromCamera():
    now = datetime.now().time().strftime("%H:%M:%S.%f")
    vrCameraService.createViewpoint("vp_{}".format(now))


def renderViewpoints():
    viewpoints = vrCameraService.getAllViewpoints()

    renderDirectory = vrFileDialog.getExistingDirectory("Select a render directory:", vrFileIO.getFileIOBaseDir())

    if not renderDirectory:
        logWarn("No directory where to save the renderings!")
        return

    for viewpoint in viewpoints:
        name = viewpoint.getName()

        if name.startswith('vp_'):
            vrRenderSettings.setRenderFilename("{}.jpg".format(name))
            vrRenderSettings.startRenderToFile(False)
