# Example 1.0
# Simple Field Access

material = createMaterial("UPhongMaterial")
material.setName("Python Material")
fields = material.fields()
fields.setVec3f("diffuseColor", 1, 0, 0)

# Complex Field Access
