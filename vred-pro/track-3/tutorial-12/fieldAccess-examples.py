# Simple Field Access
material = createMaterial("UPhongMaterial")
material.setName("Python Material")
fields = material.fields()
fields.setVec3f("diffuseColor", 1, 0, 0)

# Complex Field Access
leatherMatFields = findMaterial("Leather red").fields()
colorComponentData = vrFieldAccess(leatherMatFields.getFieldContainer('colorComponentData'))
bumpComponent = vrFieldAccess(colorComponentData.getFieldContainer('bumpComponent'))
bumpImageComponent = vrFieldAccess(bumpComponent.getFieldContainer('image'))

width = bumpImageComponent.getInt32("width")
height = bumpImageComponent.getInt32("height")

print(width, height)

# Attaching arbitrary data to a node field
envNode = findNode("EnvironmentsTransform")
customAttachment = createAttachment("ValuePair")
vrFieldAccess(customAttachment).setMString('key', ['key1', 'key2', 'key3'])
vrFieldAccess(customAttachment).setMString('value', ['value1', 'value2', 'value3'])
envNode.addAttachment(customAttachment)

# Reading the values from the attachment
envNode = findNode("EnvironmentsTransform")
attachmentFieldAccess = vrFieldAccess(envNode.getAttachment("ValuePair"))
keys = attachmentFieldAccess.getMString('key')
values = attachmentFieldAccess.getMString('value')

keyValuePairs = list(zip(keys, values))
print(keyValuePairs)