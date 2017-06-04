# 2013.08.22 22:23:51 Pacific Daylight Time
# Embedded file name: toontown.pets.PetChase
from pandac.PandaModules import *
from direct.showbase.PythonUtil import reduceAngle
from otp.movement import Impulse
import math

class PetChase(Impulse.Impulse):
    __module__ = __name__

    def __init__(self, target = None, minDist = None, moveAngle = None):
        Impulse.Impulse.__init__(self)
        self.target = target
        if minDist is None:
            minDist = 5.0
        self.minDist = minDist
        if moveAngle is None:
            moveAngle = 20.0
        self.moveAngle = moveAngle
        self.lookAtNode = NodePath('lookatNode')
        self.lookAtNode.hide()
        self.vel = None
        self.rotVel = None
        return

    def setTarget(self, target):
        self.target = target

    def destroy(self):
        self.lookAtNode.removeNode()
        del self.lookAtNode
        del self.target
        del self.vel
        del self.rotVel

    def _setMover(self, mover):
        Impulse.Impulse._setMover(self, mover)
        self.lookAtNode.reparentTo(self.nodePath)
        self.vel = self.VecType(0)
        self.rotVel = self.VecType(0)

    def _process(self, dt):
        Impulse.Impulse._process(self, dt)
        me = self.nodePath
        target = self.target
        targetPos = target.getPos(me)
        x = targetPos[0]
        y = targetPos[1]
        distance = math.sqrt(x * x + y * y)
        self.lookAtNode.lookAt(target)
        relH = reduceAngle(self.lookAtNode.getH(me))
        epsilon = 0.005
        rotSpeed = self.mover.getRotSpeed()
        if relH < -epsilon:
            vH = -rotSpeed
        elif relH > epsilon:
            vH = rotSpeed
        else:
            vH = 0
        if abs(vH * dt) > abs(relH):
            vH = relH / dt
        if distance > self.minDist and abs(relH) < self.moveAngle:
            vForward = self.mover.getFwdSpeed()
        else:
            vForward = 0
        distanceLeft = distance - self.minDist
        if distance > self.minDist and vForward * dt > distanceLeft:
            vForward = distanceLeft / dt
        if vForward:
            self.vel.setY(vForward)
            self.mover.addShove(self.vel)
        if vH:
            self.rotVel.setX(vH)
            self.mover.addRotShove(self.rotVel)
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\pets\PetChase.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:23:51 Pacific Daylight Time
