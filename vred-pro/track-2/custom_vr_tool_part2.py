from PySide2 import QtCore, QtGui, QtWidgets

# global interpolator and slider for turntable
turntableInterpolator = None
turntableSlide = None

# Function to initialize and active the turntable
def turntableToolEnabled():
    print("Enable Turntable Tool")

    global turntableInterpolator
    global turntableSlide

    turntable = vrNodeService.findNode("*tool_turntable", wildcard=True)
    toNode(turntable.getObjectId()).makeTransform()

    turntableInterpolator = vrInterpolator()
    turntableSlide = vrRotationSlide(turntable, 0, 0, 0, 0, 0, 359, 15.0)
    turntableInterpolator.add(turntableSlide)
    turntableInterpolator.setActive(True)

# Function to disable the turntable and clear the scene
def turntableToolDisabled():
    print("Disable Turntable Tool")
    global turntableInterpolator

    if turntableInterpolator:
        turntableInterpolator.setActive(False)
        turntableInterpolator = None

# Create the tool, set its name and connect to the on and off state
turntableTool = vrImmersiveUiService.createTool("Turntable Tool")
turntableTool.setText("Turntable Tool")
turntableTool.setCheckable(True)
turntableTool.signal().checked.connect(turntableToolEnabled)
turntableTool.signal().unchecked.connect(turntableToolDisabled)