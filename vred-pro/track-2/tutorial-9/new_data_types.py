# Example 1
# QColor:
colorRed = QColor(255, 0, 0)
colorBlue = QColor(0, 255, 0)
colorGreen = QColor(0, 0, 255)

fontcolor = QColor.fromRgb(127, 24, 78)
backgroundColor = QColor.fromHsv(180, 255, 255)

annotation = vrAnnotationService.createAnnotation("New Annotation")
annotation.setFontColor(fontcolor)
annotation.setBackgroundColor(backgroundColor)
annotation.setText("I like it!")

x = 0
y = 0
z = 300
position = QVector3D(x, y, z)
matAnnotation = vrAnnotationService.findAnnotation("MaterialAnnotation")
matAnnotation.setPosition(position)

# Example 2:
# QVector4D, QVector3D, QVector2D    

# QVector4D
camera = vrCameraService.getActiveCamera()
viewFrustum = camera.getFrustum()
print("Frustum as QVector4D:", viewFrustum)

# QVector3D
camera = vrCameraService.getActiveCamera()
fromAtUp = vrCameraService.getActiveCamera().getFromAtUp()
fromVector = fromAtUp.getFrom()
atVector = fromAtUp.getAt()
upVector = fromAtUp.getUp()

print("From Vector:", fromVector)
print("At Vector:", atVector)
print("Up Vector:", upVector)

cameraTangent = QVector3D.crossProduct((atVector - fromVector), upVector)
cameraTangent.normalize()
print("Cross product", cameraTangent)

x = 0
y = 0
z = -300
position = QVector3D(x, y, z)
matAnnotation = vrAnnotationService.findAnnotation("MaterialAnnotation")
matAnnotation.setPosition(position)

# QVector2D
camera = vrCameraService.getActiveCamera()
camera.setSensorSize(QVector2D(10, 10))
camera.updateFromPerspectiveMatch()

#Example 3:
# QMatrix4x4
camera = vrCameraService.getActiveCamera()
projectionMat = camera.getCustomProjectionMatrix()
print(projectionMat)

# Example:
# Math operations
