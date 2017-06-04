# 2013.08.22 22:20:53 Pacific Daylight Time
# Embedded file name: toontown.hood.HQPeriscopeAnimatedProp
import AnimatedProp
from direct.actor import Actor
from direct.interval.IntervalGlobal import *

class HQPeriscopeAnimatedProp(AnimatedProp.AnimatedProp):
    __module__ = __name__

    def __init__(self, node):
        AnimatedProp.AnimatedProp.__init__(self, node)
        parent = node.getParent()
        self.periscope = Actor.Actor(node, copy=0)
        self.periscope.reparentTo(parent)
        self.periscope.loadAnims({'anim': 'phase_3.5/models/props/HQ_periscope-chan'})
        self.periscope.pose('anim', 0)
        self.node = self.periscope
        self.track = Sequence(Wait(2.0), self.periscope.actorInterval('anim', startFrame=0, endFrame=40), Wait(0.7), self.periscope.actorInterval('anim', startFrame=40, endFrame=90), Wait(0.7), self.periscope.actorInterval('anim', startFrame=91, endFrame=121), Wait(0.7), self.periscope.actorInterval('anim', startFrame=121, endFrame=91), Wait(0.7), self.periscope.actorInterval('anim', startFrame=90, endFrame=40), Wait(0.7), self.periscope.actorInterval('anim', startFrame=40, endFrame=90), Wait(0.7), self.periscope.actorInterval('anim', startFrame=91, endFrame=121), Wait(0.5), self.periscope.actorInterval('anim', startFrame=121, endFrame=148), Wait(3.0), name=self.uniqueName('HQPeriscope'))

    def delete(self):
        AnimatedProp.AnimatedProp.delete(self)
        self.node.cleanup()
        del self.node
        del self.periscope
        del self.track

    def enter(self):
        AnimatedProp.AnimatedProp.enter(self)
        self.track.loop()

    def exit(self):
        AnimatedProp.AnimatedProp.exit(self)
        self.track.finish()
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\hood\HQPeriscopeAnimatedProp.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:20:53 Pacific Daylight Time
