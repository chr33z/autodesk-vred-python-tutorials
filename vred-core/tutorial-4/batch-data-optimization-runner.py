import os
import base64
import subprocess

vredCorePath = r'D:\Programme\Autodesk\VREDCore-13.3\bin\WIN64\VREDCore.exe'

directory = os.path.dirname(__file__)

with open(os.path.join(directory, 'batch-data-optimization.py'), 'r') as file:
    # Read file content
    scriptContent = file.read()

    # Convert python script to base64, in order to import it into VRED
    base64EncodedScript = base64.b64encode(scriptContent.encode('UTF-8')).decode('UTF-8')

    # Start VRED with prepython and the base64 encoded script as input
    subprocess.call([vredCorePath, '-prepython={}'.format(base64EncodedScript)])