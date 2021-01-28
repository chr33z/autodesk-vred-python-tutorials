'''
Run the python examples by copying and pasting the code snippets
into the VRED Script Editor and press run to see the results
'''

groupNode = vrNodeService.findNode("Group Node")
deleteNode(groupNode)


# Example 1.0:
# Finding nodes in the screnegraph
root = vrNodeService.findNode('Root')
camera = vrNodeService.findNode('Perspective')

print(root)
print(camera)
 

# Example 1.1:
# Creating new nodes
print()
print('---------------')
groupNode = createNode('Group', 'Group Node', root)
print(groupNode)
updateScenegraph(True)

# Example 1.2:
# Creating geometry and add them to the scenegraph
print()
print('---------------')
planeNode = createPlane(1000, 1000, 1, 1, 1, 1, 1)
planeNode.setName('Plane Geometry')
planeNode.setTranslation(100, 200, 10)
groupNode.addChild(planeNode)

boxNode = createBox(500, 500, 500, 1, 1, 1, 1, 1, 1)
boxNode.setName('Box Geometry')
boxNode.setTranslation(-100, -200, 10)
groupNode.addChild(boxNode)

# Example 1.3:
# Move nodes in the scenegraph
print()
print('---------------')
anotherNode = createNode('Transform', 'Another Node', root)
anotherNode.setTranslation(0, 0, 500)

planeNode = vrNodeService.findNode('Plane Geometry')
boxNode = vrNodeService.findNode('Box Geometry')

anotherNode.addChild(planeNode)
anotherNode.addChild(boxNode)

# Example 2.0:
# Create a new camera
camera = vrCameraService.createCamera("New Camera")

cameraFrom = QVector3D(2000, 2000, 5000)
cameraAt = QVector3D(0, 0, 0)
cameraUp = QVector3D(0, 0, 1)
fromAtUp = vrCameraFromAtUp(cameraFrom, cameraAt, cameraUp)

camera.setFromAtUp(fromAtUp)
camera.activate()

# Create a camera viewpoint from the current camera
viewpointName = 'New Viewpoint'
viewpoint = vrCameraService.createViewpoint(viewpointName)

# Example 3.0:
# Create a basic phong material
materialA = createMaterial("UPhongMaterial")
materialA.setName("Material A")
materialA.fields().setVec("diffuseColor", [1, 0, 0])

materialB = createMaterial("UPhongMaterial")
materialB.setName("Material B")
materialB.fields().setVec("diffuseColor", [0, 1, 0])

# Example 3.1:
# Create a material switch and add the newly created materials
materialSwitch = createMaterial("SwitchMaterial")
materialSwitch.setName("Material Switch")
materialSwitch.addMaterial(materialA)
materialSwitch.addMaterial(materialB)

# Example 3.2:
# Apply the material the geometry
plane = findNode("Plane Geometry")
box = findNode("Box Geometry")

materialA = findMaterial("Material A")
materialB = findMaterial("Material B")
plane.setMaterial(materialA)
box.setMaterial(materialB)

# Example 4.0
# Create a variant set
variantSetName = 'New Variant Set'
createVariantSet(variantSetName)
variantSet = getVariantSet(variantSetName)

# Example 4.1
# Add stuff to the variant set
variantSet.addScript("print('Hello World!')")
variantSet.addView(vrCameraService.getViewpoint('New Viewpoint'))