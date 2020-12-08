from vrKernelService import vrCameraService
import vrFileIO
import vrFileDialog
import vrRenderSettings


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


renderViewpoints()
