'''
Run the python examples by copying and pasting the code snippets
into the VRED Script Editor and press run to see the results
'''

# Example 1.0:
# Finding nodes in the screnegraph
root = vrNodeService.findNode('Root')
camera = vrNodeService.findNode('Perspective')

# Example 1.1:
# Creating new nodes
draftNode =

# Example 1.2:
# Creating geometry and add them to the scenegraph
plane = vrNodeUtils.createPlane(1000, 1000, 1, 1, 0, 0, 0)
plane.setName('Plane Geometry')
plane.setTranslation(100, 200, 10)
draftNode.addChild(plane)

box = vrNodeUtils.createBox(500, 500, 500, 1, 1, 0, 0, 0)
box.setName('cube Geometry')
box.setTranslation(-100, -200, 10)
draftNode.addChild(box)

# Example 1.3:
# Move nodes in the scenegraph
finalNode =
finalNode.setTranslation(0, 0, 100)

planeNode = findNode('Plane Geometry')
boxNode = findNode('Box Geometry')

draftNode.subChild(planeNode)
draftNode.subChild(boxNode)

finalNode.addChild(planeNode)
finalNode.addChild(boxNode)

# Example 2.0:
# Create a camera viewpoint from the current camera
viewpointName = 'New Viewpoint'
addViewPoint(viewpointName, False)
viewpoint = getViewpoint()

# Example 3.0:
# Create a basic phong material


# Example 3.1:
# Create a material switch and add the newly created materials


# Example 3.2:
# Apply the material switch to a geometry

# Example 4.0
# Create a variant set
variantSetName = 'New Variant Set'
createVariantSet(variantSetName)
variantSet = getVariantSet(variantSetName)

# Example 4.1
# Add stuff to the variant set
variantSet.addScript("print('Hello World!')")
variantSet.addView(viewpointName)
