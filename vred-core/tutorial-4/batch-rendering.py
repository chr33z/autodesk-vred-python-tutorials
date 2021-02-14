import sys
import base64
import subprocess

vredCorePath = r'D:\Programme\Autodesk\VREDCore-13.3\bin\WIN64\VREDCore.exe'

# Defined a python script as a string
# This python script will run inside VRED
batchRenderingScript = '''
print("=[VRED Core Tutorial] Batch Rendering")

vredSceneFile = r"C:/ProgramData/Autodesk/VREDPro-13.3/examples/Automotive_Genesis.vpb"
variants = ("Black Metallic", "Blue Fire Metallic", "Silver Dark Metallic")
viewpoints = ("Home", "Left-Back", "Viewpoint")
pathTemplate = r"C:/VRED_Examples/batch_rendering/variant_{viewpoint}_{variant}.png"

print("=[VRED Core Tutorial] Load Source file...")
load(vredSceneFile)

print("=[VRED Core Tutorial] Iterate viewpoints and variants...")
for viewpointName in viewpoints:
    vp = vrCameraService.getViewpoint(viewpointName)
    if not vp.isNull():
        vp.activate()
        for variantName in variants:
            print("=[VRED Core Tutorial] Rendering {}, {}".format(viewpointName, variantName))
            vrVariants.selectVariantSet(variantName)
            createSnapshot(pathTemplate.format(viewpoint=viewpointName, variant=variantName), 1920, 1080)

print("=[VRED Core Tutorial] Finished Rendering...")
'''

# Convert python script to base64, in order to import it into VRED
base64EncodedScript = base64.b64encode(batchRenderingScript.encode('UTF-8')).decode('UTF-8')

# Start VRED with prepython and the base64 encoded script as input
subprocess.call([vredCorePath, '-prepython={}'.format(base64EncodedScript)])