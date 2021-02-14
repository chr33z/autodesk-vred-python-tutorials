import sys
import base64
import subprocess

vredCorePath = r'D:\Programme\Autodesk\VREDCore-13.3\bin\WIN64\VREDCore.exe'

# Defined a python script as a string
# This python script will run inside VRED
batchRenderingScript = '''
import os

print("=[VRED Core Tutorial] Batch Data Optimization")

sourceDirectory = 'C:/VRED_Examples/unoptimized'
targetDirectory = 'C:/VRED_Examples/optimzied'

# Create target directory if it does not exist
if not os.path.exists(targetDirectory):
    os.makedirs(targetDirectory)

# Iterate over files in source directory and process each filename
for filename in os.listdir(sourceDirectory):
    print("=[VRED Core Tutorial] Optimize file: {}".format(filename))

    # Create paths for the source and the target file
    # Replace windows backslashes with linux style forward slashes
    sourcePath = os.path.join(sourceDirectory, filename).replace('\\\\','/')
    targetPath = os.path.join(targetDirectory, filename).replace('\\\\','/')

    # Load file in VRED
    load(sourcePath)

    # Optimize Geometry
    removeTransformNodesWithNoChildren(findNode("Root"))
    optimizeIndices(findNode("Root"))

    # Save optimized file
    save(targetPath)

# Close VRED instance
terminateVred()

print("=[VRED Core Tutorial] Finished Optimizing files...")
'''

# Convert python script to base64, in order to import it into VRED
base64EncodedScript = base64.b64encode(batchRenderingScript.encode('UTF-8')).decode('UTF-8')

# Start VRED with prepython and the base64 encoded script as input
subprocess.call([vredCorePath, '-prepython={}'.format(base64EncodedScript)])