from vrKernelServices import vrSceneplateTypes
from vrKernelServices import vrdSceneplateNode

NodeType = vrSceneplateTypes.NodeType
ContentType = vrSceneplateTypes.ContentType
PositionType = vrSceneplateTypes.Position

def addWatermark(text):
    sceneplateRoot = vrSceneplateService.getRootNode()
    watermarkNode = vrSceneplateService.createNode(sceneplateRoot, NodeType.Frontplate, "Watermark")
    watermark = vrdSceneplateNode(watermarkNode)
    watermark.setContentType(ContentType.Text)
    watermark.setText(text)

    watermark.setFontColor(QVector3D(0.7, 0.7, 0.7))
    watermark.setPosition(PositionType.Center)