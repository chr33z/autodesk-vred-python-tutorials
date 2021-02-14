import sys
import base64
import subprocess
import os

# batchRenderingScript = '''
print("=[VRED Core Tutorial] Batch Data Conversion")

vredCorePath = r'D:\Programme\Autodesk\VREDCore-13.3\bin\WIN64\VREDCore.exe'

sourceExtension = 'vpb'
sourceDirectory = r'C:\VRED_Examples\vpb'

targetExtension = 'fbx'
targetDirectory = r'C:\VRED_Examples\fbx'

# Create target directory if it does not exist
if not os.path.exists(targetDirectory):
    os.makedirs(targetDirectory)

# Iterate over files in source directory and process each filename
for filename in os.listdir(sourceDirectory):
    # ... but only if the file extension matches
    if filename.endswith(sourceExtension): 
        # Extract the file name without the extension
        namePart = filename.split('.')[0]

        print("=[VRED Core Tutorial] Data Conversion: {} from {} to {}".format(namePart, sourceExtension, targetExtension))

        # Create paths for the source and the target file
        # Replace windows backslashes with linux style forward slashes
        sourcePath = os.path.join(sourceDirectory, filename).replace('\\','/')
        targetPath = os.path.join(targetDirectory, '{}.{}'.format(namePart, targetExtension)).replace('\\','/')

        # Start vred and process files
        subprocess.call([vredCorePath, '-prepython=load("{}"); save("{}"); terminateVred()'.format(sourcePath, targetPath)])

print("=[VRED Core Tutorial] Finished Batch Data Conversion...")

