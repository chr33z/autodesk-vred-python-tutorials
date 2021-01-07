# Example 1.0
# Calculating with QtVectors
import PySide2.QtGui
QVector3D = PySide2.QtGui.QVector3D

camera = vrCameraService.getActiveCamera()
cameraTranslation = vrMathService.getTranslation(camera.getWorldTransform())

print("Distance to origin: ", cameraTranslation.length())
print("Distance to origin (point): ", cameraTranslation.distanceToPoint(QVector3D(0,0,0)))

distanceToZAxis = cameraTranslation.distanceToLine(QVector3D(0,0,0), QVector3D(0,0,1))
print("Distance to z-axis", distanceToZAxis)

# Example 2.0
# Using vrMathService
boxPtr = vrNodeUtils.createBox(1000, 1000, 1000, 1, 1, 1, 1, 1, 1)
boxPtr.setName("Box")
boxPtr.setTranslation(100, 200, 300)
boxPtr.setRotation(23, 34, 45)
boxPtr.setScale(1.2, 1.3, 1.3)

box = vrNodeService.findNode("Box")
transform = box.getWorldTransform()

translation = vrMathService.getTranslation(transform)
rotation = vrMathService.getRotation(transform)
scale = vrMathService.getScaleFactor(transform)
scaleOrientation = vrMathService.getScaleOrientation(transform)

print("Translation", translation)
print("Rotation", rotation.toEulerAngles())
print("Scale", scale)
print("Scale Orientation", scaleOrientation.toEulerAngles())