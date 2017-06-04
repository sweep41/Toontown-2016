# 2013.08.22 22:19:31 Pacific Daylight Time
# Embedded file name: toontown.effects.BlastEffect
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from EffectController import EffectController

class BlastEffect(NodePath, EffectController):
    __module__ = __name__

    def __init__(self):
        NodePath.__init__(self, 'BlastEffect')
        EffectController.__init__(self)
        self.fadeTime = 0.15
        self.effectColor = Vec4(1, 1, 1, 1)
        model = loader.loadModel('phase_4/models/props/tt_m_efx_ext_particleCards')
        self.effectModel = model.find('**/tt_t_efx_ext_particleBlast')
        self.effectModel.reparentTo(self)
        self.effectModel.setColorScale(0, 0, 0, 0)
        self.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
        self.setBillboardPointWorld()
        self.setDepthWrite(0)
        self.setLightOff()
        self.setFogOff()

    def createTrack(self):
        self.effectModel.setColorScale(0, 0, 0, 0)
        fadeBlast = self.effectModel.colorScaleInterval(self.fadeTime, Vec4(0, 0, 0, 0), startColorScale=Vec4(self.effectColor), blendType='easeOut')
        scaleBlast = self.effectModel.scaleInterval(self.fadeTime, 4, startScale=1.0, blendType='easeIn')
        self.track = Sequence(Parallel(fadeBlast, scaleBlast), Func(self.cleanUpEffect))

    def setEffectColor(self, color):
        self.effectColor = color
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\effects\BlastEffect.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:19:31 Pacific Daylight Time