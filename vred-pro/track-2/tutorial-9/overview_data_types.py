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
materialAnnotation.setDefaultFontColor(fontcolor)
materialAnnotation.setDefaultBackgroundColor(backgroundColor)

# Example 2:
# QVector4D, QVector3D, QVector2D

# QVector4D
camera = vrCameraService.getActiveCamera()
viewFrustum = camera.getFrustum()
print("Frustum as QVector4D:", viewFrustum)

# QVector3D
trackingOrigin = vrDeviceService.getTrackingOrigin()
print("Tracking Origin as QVector3D:", trackingOrigin)

x = 100
y = 200
z = 300
position = QVector3D(x, y, z)
materialAnnotation.setPosition(position)

# QVector2D
camera.setSensorSize(QVector2D(36, 24))