# Example 1.0
# Finding Nodes

# Finding nodes with API v1 and v2
study_NodePtr = findNode('Study_Transform')
study_vrdNode = vrNodeService.findNode('Study_Transform')

# Example 2.0
# Using API v1 functions with vrdNodes
createNode("Group", "Interieur_nodePtr", study_NodePtr)
print("Created new group with nodePtr")

createNode("Group", "Interieur_vrdNode", study_vrdNode)
print("Created new group with vrdNode")

updateScenegraph(True)


# Using API v2 functions with vrNodePtrs
interieur_NodePtr = findNode('Interieur_nodePtr')

childIndex = study_vrdNode.getChildIndex(interieur_NodePtr)

print("Interieur Node is at index:", childIndex)


# Example 3.0
# Convert from nodePtr to vrdNode
targetNodePtr = findNode("Target")
targetNode = vrNodeService.getNodeFromId(targetNodePtr.getID())

# Convert from vrdNode to nodePtr
targetNodePtr = toNode(targetNode.getObjectId())
