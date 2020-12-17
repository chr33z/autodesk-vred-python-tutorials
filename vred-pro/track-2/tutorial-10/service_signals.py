# Example 1.0
# Connecting to service signals 
# vrAttachmentService
def annotationCreatedCallback(annotation):
    print("Created annotation", annotation)
    
def annotationAddedCallback():
    print("Added annotation")
    
def annotationsDeletedCallback():
    print("Deleted annotation")
    
def annotationsShowChangedCallback(visible):
    print("Annotations are visible: ", visible)

vrAnnotationService.annotationCreated.connect(annotationCreatedCallback)
vrAnnotationService.annotationsAdded.connect(annotationAddedCallback)
vrAnnotationService.annotationsDeleted.connect(annotationsDeletedCallback)
vrAnnotationService.showAnnotationsChanged.connect(annotationsShowChangedCallback)

# vrNodeService
def nodesChanged(nodes):
    print("Nodes changed: Rebuilding find cache...")
    vrNodeService.clearFindCache()
    vrNodeService.initFindCache()

vrNodeService.nodesAdded.connect(nodesChanged)
vrNodeService.nodesRemoved.connect(nodesChanged)

# Listening to general object changes
def propertyChanged(obj, propertyName):
   print("object name: {}, property name: {}".format(obj.getName(), propertyName))

vrObjectService.propertyChanged.connect(propertyChanged)