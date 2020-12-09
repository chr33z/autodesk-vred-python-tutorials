# Example 1.0
# Working with Nodes

# Use vrdNode objects in case of nodePtr
targetNode = vrNodeService.findNode("Target")

# API v1 function
createNode("Transform", "ChidlOfTarget", target)


# Example 2.0
# Convert from nodePtr to vrdNode
targetNodePtr = findNode("Target")
targetNode = vrNodeService.getNodeFromId(targetNodePtr.getID())

# Convert from vrdNode to nodePtr
targetNodePtr = toNode(targetNode.getObjectId())