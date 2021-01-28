# Example 1
# Color
blue = 127
red = 255
green = 127

vrRenderSettings.setRenderBackgroundColor(blue, red, green)
renderBackground = vrRenderSettings.getRenderBackgroundColor()
print(type(renderBackground), renderBackground.x(), renderBackground.y(), renderBackground.z())

# Example 2
# Vectors
camera = vrCamera.getActiveCameraNode()
cameraPosition = camera.getTranslation()
print(type(cameraPosition), cameraPosition)


# Example 3
# Math operations on vectors
v1 = vr