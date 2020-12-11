# Example 1.0
# Finding Nodes

# Finding nodes with API v1 and v2
targetNode_v1 = findNode('Target')
targetNode_v2 = vrNodeService.findNode('Target')

# Example 2.0
# Using API v1 functions
createNode("Transform", "ChidlOfTarget", targetNode_v1)
createNode("Transform", "ChidlOfTarget", targetNode_v2)

# Using API v2 functions
camera = vrCameraService.getActiveCamera()
camera.adjustAtPosition(targetNode_v1)
camera.adjustAtPosition(targetNode_v2)

# Example 3.0
# Convert from nodePtr to vrdNode
targetNodePtr = findNode("Target")
targetNode = vrNodeService.getNodeFromId(targetNodePtr.getID())

# Convert from vrdNode to nodePtr
targetNodePtr = toNode(targetNode.getObjectId())
