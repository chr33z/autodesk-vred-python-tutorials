# https://knowledge.autodesk.com/support/vred-products/learn-explore/caas/CloudHelp/cloudhelp/2021/ENU/VRED/files/Python-Documentation/Python-Examples/VRED-Python-Documentation-Python-Examples-Visualize-user-positions-html-html.html
# This scripts shows an overview of user positions in a collaboration sesion
class UserMap(vrAEBase):
    
    def __init__(self):
        vrAEBase.__init__(self)
        self.spheres = {}
        self.addLoop()
        # callback sesson start/stop
        vrSessionService.sessionJoined.connect(self.started)
        vrSessionService.sessionLeft.connect(self.ended)
        # callback user joins/leaves session
        vrSessionService.userArrives.connect(self.userArrived)
        vrSessionService.userLeaves.connect(self.userLeaves)
        
    def loop(self):
        # this is my local camera position
        myPos = getTransformNodeTranslation(vrSessionService.getUser().getHeadNode(),True)
        for user in vrSessionService.getRemoteUsers():
            sphere = self.spheres[user.getUserId()]
            # this is the users head transformation node
            pos = getTransformNodeTranslation(user.getHeadNode(),True)
            # move indicator for user position
            setTransformNodeTranslation(sphere,(pos.x()-myPos.x())/100,(pos.y()-myPos.y())/100,-500,False)
   
    def started(self):
        self.group = createNode("Group", "UserMap", vrCameraService.getActiveCamera())
        self.plane = createCylinder(2, 100, 50, True, True, True, .0, .1, .0)
        self.setTransparent(self.plane)
        addChilds(self.group,[self.plane])
        color = vrSessionService.getUser().getUserColor()
        sphere = createSphere(3, 2, color.redF(), color.greenF(), color.blueF())
        addChilds(self.group,[sphere])
        setTransformNodeTranslation(sphere,0,0,-500,False)
        setTransformNodeRotation(self.plane, 90, 0, 0)
        setTransformNodeTranslation(self.plane, 0, 0, -500, False)
        self.setActive(True)
        
    def ended(self):
        subChilds(self.group,[self.plane])
        subChilds(vrCameraService.getActiveCamera(),[self.group])
        self.setActive(False)
        
    def userArrived(self,user):
        color = user.getUserColor()
        sphere = createSphere(2, 2, color.redF(), color.greenF(), color.blueF())
        addChilds(self.group,[sphere])
        self.spheres[user.getUserId()] = sphere
        
    def userLeaves(self,user):
        sphere = self.spheres[user.getUserId()]
        subChilds(self.group,[sphere])
        
    def setTransparent(self,node):
        node.getMaterial().fields().setVec3f("seeThrough",.95,.95,.95)

map = UserMap()