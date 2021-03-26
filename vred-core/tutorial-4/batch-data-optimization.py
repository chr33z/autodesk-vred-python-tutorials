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