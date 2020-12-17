# Simple Field Access
material = createMaterial("UPhongMaterial")
material.setName("Python Material")
fields = material.fields()
fields.setVec3f("diffuseColor", 1, 0, 0)

# Complex Field Access
matFields = findMaterial("Shadow").fields()
colorComponentData = vrFieldAccess(matFields.getFieldContainer('colorComponentData'))
diffuseComponent = vrFieldAccess(colorComponentData.getFieldContainer('diffuseComponent'))
diffuseComponent.setVec3f("color", 1,0,0)

# Attaching arbitrary data to a node field
envNode = findNode("Environments")
customAttachment = createAttachment("ValuePair")
vrFieldAccess(customAttachment).setMString('key', ['key1', 'key2', 'key3'])
vrFieldAccess(customAttachment).setMString('value', ['value1', 'value2', 'value3'])
envNode.addAttachment(customAttachment)

# Reading the values from the attachment
envNode = findNode("Environments")
attachmentFieldAccess = vrFieldAccess(envNode.getAttachment("ValuePair"))
keys = attachmentFieldAccess.getMString('key')
values = attachmentFieldAccess.getMString('value')

keyValuePairs = list(zip(keys, values))
print(keyValuePairs)