#Example 1

# Get the active camera from the camera service
camera = vrCameraService.createCamera("My New Camera")

# Create a new camera track on the camera object
cameraTrack = vrCameraService.createCameraTrack("My New Camera Track", camera)

# Create a new viewpoint on the camera track
viewpoint = vrCameraService.createViewpoint("My New Viewpoint", cameraTrack)


#Example 2

# Create a new pointlight with the vrLightService
newPointLight = vrLightService.createLight(
                    "My New PointLight",
                    vrLightTypes.LightType.Point
                )
                
# Set the translation of this pointlight                               
newPointLight.setTranslation(QVector3D(0,0,1000))


#Example 3

# Create a new camera with the vrCameraService
camera = vrCameraService.createCamera("New Camera")

# Create vectors that define the location and look-at point of the camera
cameraFrom = QVector3D(5000, 8000, 3000)
cameraAt = QVector3D(0, 0, 0)
cameraUp = QVector3D(0, 0, 1)

# Set the camera parameters
fromAtUp = vrCameraFromAtUp(cameraFrom, cameraAt, cameraUp)
camera.setFromAtUp(fromAtUp)

# Activate the camera
camera.activate()


# Create a new camera track on the camera object
cameraTrack = vrCameraService.createCameraTrack("My New Camera Track", camera)

# Create a new viewpoint on the camera track
viewpoint = vrCameraService.createViewpoint("My New Viewpoint", cameraTrack)

viewpoint.createPreview(True)