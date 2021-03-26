from vrKernelServices import vrSceneplateTypes
from vrKernelServices import vrdSceneplateNode

# Get reference to sceneplate types
NodeType = vrSceneplateTypes.NodeType
ContentType = vrSceneplateTypes.ContentType
PositionType = vrSceneplateTypes.Position


def addWatermark(text):
    '''
    Add a watermark with a text to your scene
    '''
    print("Create Watermark")
    sceneplateRoot = vrSceneplateService.getRootNode()
    watermarkNode = vrSceneplateService.createNode(sceneplateRoot, NodeType.Frontplate, "Watermark")
    watermark = vrdSceneplateNode(watermarkNode)
    watermark.setContentType(ContentType.Text)
    watermark.setText(text)

    watermark.setFontColor(QVector3D(0.7, 0.7, 0.7))
    watermark.setPosition(PositionType.Center)