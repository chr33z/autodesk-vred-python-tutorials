import PySide2.QtGui
QColor = PySide2.QtGui.QColor
QVector4D = PySide2.QtGui.QVector4D
QVector3D = PySide2.QtGui.QVector3D
QVector2D = PySide2.QtGui.QVector2D

# Example 1
# QColor:
colorRed = QColor(255, 0, 0)
colorBlue = QColor(0, 255, 0)
colorGreen = QColor(0, 0, 255)

fontcolor = QColor.fromRgb(127, 24, 78)
backgroundColor = QColor.fromRgb(34, 24, 78)

materialAnnotation = vrAnnotationService.createAnnotation("MaterialAnnotation")
materialAnnotation.setFontColor(fontcolor)
materialAnnotation.setBackgroundColor(backgroundColor)
materialAnnotation.setText("I like it!")

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

print(fromVector)
print(atVector)
print(upVector)

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
