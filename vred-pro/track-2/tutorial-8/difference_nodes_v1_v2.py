# Node pointers with API v1

# Find node "EXT" with API v1
extNodePtr = findNode("EXT")

# set translation
extNodePtr.setTranslation(0,0,38)

# get translation
translation = extNodePtr.getTranslation()
print("Translation:", translation)

# set name
extNodePtr.setName("Another EXT")



# Node pointers with API v2

# Find node "EXT" with API v2
extVrdNode = vrNodeService.findNode("EXT")

# set translation
translationVector = QVector3D(0,0,38)
extVrdNode.setTranslation(translationVector)

# get translation
translation = extVrdNode.getTranslation()
print("Translation:", translation)

# set name
extVrdNode.setName("Another EXT")