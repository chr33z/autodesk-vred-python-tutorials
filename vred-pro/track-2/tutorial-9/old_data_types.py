# Example 1
# Color
blue = 127
red = 255
green = 127

vrRenderSettings.setRenderBackgroundColor(blue, red, green)
renderBackground = vrRenderSettings.getRenderBackgroundColor()
print(type(renderBackground), renderBackground)

# Example 2:
# QVector4D, QVector3D, QVector2D

# Vector 4
vrOSGWidget.setFrustum(3000, -3000, 3000, -3000)

# Vector 3
camera = vrCamera.getActiveCameraNode()
cameraPosition = camera.getTranslation()
print(type(cameraPosition), cameraPosition)