# Example 1
# Recreating material switches
print('--- Create Switch Materials ---')

allMaterials = getAllMaterials()

# get all materials which name starts with "switch"
switchMaterials = list(filter(lambda matPtr: matPtr.getName().startswith('switch'), allMaterials))

# iterate all switch materials and process
for switchMaterial in switchMaterials:
    switchPtr = switchMaterial
    switchName = switchPtr.getName()
    print('Found switch: ' + str(switchName))

    # extract material prefix
    materialPrefix = '_'.join(switchName.split('_')[1:])

    # Get all materials which name starts with the material prefix 
    childMaterials = list(filter(lambda matPtr: matPtr.getName().startswith(materialPrefix), allMaterials))
    childMaterialNames = [x.getName() for x in childMaterials]
    print('Found child materials: ' + ', '.join(childMaterialNames))

    # Create new material switch
    print('Create new material switch...')
    newMaterialSwitch = createMaterial("SwitchMaterial")
    newMaterialSwitch.setName(switchName)

    # Add child materials to switch
    for child in childMaterials:
        newMaterialSwitch.addMaterial(child)

    # swap old switch material with new switch material
    print('Assign new material switch...')
    nodes = switchPtr.getNodes()
    for node in nodes:
        node.setMaterial(newMaterialSwitch)

    print('')

print('Finished!')
print('---')

# Example 2
# Calling global functions in the script editor
logInfo('This is an info message from a variant set.')
logWarn('This is a warning message from a variant set.')

createViewpointFromCamera()

renderViewpoints()
