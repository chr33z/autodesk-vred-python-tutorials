from PySide2 import QtCore, QtGui, QtWidgets

# global interpolator and slider for turntable
turntableInterpolator = None
turntableSlide = None

# checked signal of our tool
def turntableToolEnabled():
    print("Enable Turntable Tool")

# Unchecked signal of our tool
def turntableToolDisabled():
    print("Disable Turntable Tool")
   
# Create the tool, set its name and connect to the on and off state
turntableTool = vrImmersiveUiService.createTool("Turntable Tool")
turntableTool.setText("Turntable Tool")
turntableTool.setCheckable(True)
turntableTool.signal().checked.connect(turntableToolEnabled)
turntableTool.signal().unchecked.connect(turntableToolDisabled)