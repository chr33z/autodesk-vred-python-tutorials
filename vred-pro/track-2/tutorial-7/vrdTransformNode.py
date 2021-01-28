groupNode = vrNodeService.findNode("Group")
deleteNode(groupNode)

numberOfBoxes = 50
boxSize = 50
xStep = 125
xRotationStep = 20
z = 500
radius = 400

boxGroup = createNode("Group")

for i in range(0, numberOfBoxes):
    box = vrNodeUtils.createBox(boxSize, boxSize, boxSize, 1, 1, 1, 0, 0, 0)
    box.setName("box {}".format(i))
    boxGroup.addChild(box)
    
    # Get the vrdNode object of the box
    boxNode = vrNodeService.getNodeFromId(box.getID())
    
    boxTranslation = QVector3D(xStep * i, 0 ,z)
    boxNode.setTranslation(boxTranslation)
    
    boxScale = boxNode.getScale() * (1 + (i * 0.01))
    boxNode.setScale(boxScale)
    
    boxLocalRotation = QVector3D(xRotationStep, 0, 0) * i
    boxNode.setRotationAsEuler(boxLocalRotation)
    
    boxNode.setWorldRotatePivot(QVector3D(0, 0, 0))
    boxNode.setRotatePivotTranslation(QVector3D(0, 0, z + radius))
    