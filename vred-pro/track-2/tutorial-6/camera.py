import math

# Example 1.0
# Get active camera with vrCameraService
camera = vrCameraService.getActiveCamera()

# Set Focal Length
camera.setFocalLength(35)


# Example 2.0
# Creating a camera using API v1 and settings its fov to 35
vrCamera.selectCamera("Perspective")
camera_v1 = vrCamera.getActiveCameraNode()

# read field of view mode (0 := vertical, 1 := horizontal)
fov_mode = camera_v1.fields().getUInt32("fovMode")
sensor_size = camera_v1.fields().getVec("sensorSize", 2)

# calculate fov based on sensor size
fov = vrOSGWidget.getFov()
focal_length = 35

if fov_mode is 0:
    fov = 2 * math.degrees(math.atan((sensor_size[1] / 2) / focal_length))
else:
    fov = 2 * math.degrees(math.atan((sensor_size[0] / 2) / focal_length))

vrOSGWidget.setFov(fov)


# Example 3.0
# Creating a camera using API v2 and calculating the fov manually
camera_v2_1 = vrCameraService.createCamera("Camera v2_1")

# read field of view mode (vertical or horizontal)
fov_mode = camera_v2_1.getFovMode()

# read sensor size as QtVector2D
sensor_size = camera_v2_1.getSensorSize()

# calculate fov based on sensor size
fov = camera_v2_1.getFov()
focal_length = 50

if fov_mode is vrCameraTypes.FovMode.Vertical:
    fov = 2 * math.degrees(math.atan((sensor_size.y() / 2) / focal_length))
else:
    fov = 2 * math.degrees(math.atan((sensor_size.x() / 2) / focal_length))

camera_v2_1.setFov(fov)