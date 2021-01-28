# Old API transformations

# Create a point p1
x1 = -500
y1 = 0
z1 = 1500

p1 = vrNodeUtils.createSphere(1, 100, 1, 1, 1)
p1.setTranslation(x1, y1, z1)
p1.setName("p1")

# Create a point p2
x2 = 500
y2 = 0
z2 = 500

p2 = vrNodeUtils.createSphere(1, 100, 1, 1, 1)
p2.setTranslation(x2, y2, z2)
p2.setName("p2")

# Create a point p_center at the geometrical center between p1 and p2
x_c = (x1 + x2) / 2
y_c = (y1 + y2) / 2
z_c = (z1 + z2) / 2

p_center = vrNodeUtils.createSphere(1, 100, 1, 1, 1)
p_center.setTranslation(x_c, y_c, z_c)
p_center.setName("p_center")


# NEW API transformations

# Create a point p1
v1 = QVector3D(-500, 500, 1500)
p1 = vrNodeUtils.createSphere(1, 100, 1, 1, 1)
vrNodeService.getNodeFromId(p1.getID()).setTranslation(v1)
p1.setName("p1")

# Create a point p2
v2 = QVector3D(500, 500, 500)
p2 = vrNodeUtils.createSphere(1, 100, 1, 1, 1)
vrNodeService.getNodeFromId(p2.getID()).setTranslation(v2)
p2.setName("p2")

# Create a point p_center at the geometrical center between p1 and p2
v_center = (v1 + v2) / 2
p_center = vrNodeUtils.createSphere(1, 100, 1, 1, 1)
vrNodeService.getNodeFromId(p_center.getID()).setTranslation(v_center)
p_center.setName("p_center")