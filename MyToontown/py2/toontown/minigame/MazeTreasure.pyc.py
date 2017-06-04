# 2013.08.22 22:22:52 Pacific Daylight Time
# Embedded file name: toontown.minigame.MazeTreasure
from direct.showbase.DirectObject import DirectObject
from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal

class MazeTreasure(DirectObject):
    __module__ = __name__
    RADIUS = 0.7

    def __init__(self, model, pos, serialNum, gameId):
        self.serialNum = serialNum
        self.nodePath = model.copyTo(render)
        self.nodePath.setPos(pos[0], pos[1], 1.0)
        self.sphereName = 'treasureSphere%s-%s' % (gameId, self.serialNum)
        self.collSphere = CollisionSphere(0, 0, 0, self.RADIUS)
        self.collSphere.setTangible(0)
        self.collNode = CollisionNode(self.sphereName)
        self.collNode.setIntoCollideMask(WallBitmask)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.nodePath.attachNewNode(self.collNode)
        self.collNodePath.hide()
        self.accept('enter' + self.sphereName, self.__handleEnterSphere)
        self.nodePath.flattenLight()

    def destroy(self):
        self.ignoreAll()
        self.nodePath.removeNode()
        del self.nodePath
        del self.collSphere
        self.collNodePath.removeNode()
        del self.collNodePath
        del self.collNode

    def __handleEnterSphere(self, collEntry):
        self.ignoreAll()
        messenger.send('MazeTreasureGrabbed', [self.serialNum])

    def showGrab(self):
        self.nodePath.reparentTo(hidden)
        self.collNode.setIntoCollideMask(BitMask32(0))
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\minigame\MazeTreasure.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:22:52 Pacific Daylight Time
