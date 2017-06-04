# 2013.08.22 22:19:56 Pacific Daylight Time
# Embedded file name: toontown.effects.SkullBurst
from pandac.PandaModules import *
from direct.showbase.DirectObject import *
from direct.interval.IntervalGlobal import *
from PooledEffect import PooledEffect
from EffectController import EffectController

class SkullBurst(PooledEffect, EffectController):
    __module__ = __name__

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.fadeTime = 1.5
        self.startDelay = 0.0
        self.effectScale = 1.0
        self.effectColor = Vec4(1, 1, 1, 1)
        model = loader.loadModel('phase_4/models/props/tt_m_efx_ext_fireworkCards')
        self.effectModel = model.find('**/tt_t_efx_ext_skull')
        self.effectModel.reparentTo(self)
        self.effectModel.setColorScale(0, 0, 0, 0)
        self.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
        self.setBillboardPointWorld()
        self.setDepthWrite(0)
        self.setLightOff()
        self.setFogOff()

    def createTrack(self):
        self.effectModel.setColorScale(0, 0, 0, 0)
        self.effectModel.setScale(700 * self.effectScale)
        fadeIn = self.effectModel.colorScaleInterval(0.2, Vec4(self.effectColor), startColorScale=Vec4(0, 0, 0, 0), blendType='easeIn')
        fadeBlast = self.effectModel.colorScaleInterval(self.fadeTime, Vec4(0, 0, 0, 0), startColorScale=Vec4(self.effectColor), blendType='easeIn')
        scaleBlast = self.effectModel.scaleInterval(self.fadeTime, 850 * self.effectScale, startScale=750 * self.effectScale, blendType='easeOut')
        self.track = Sequence(Wait(self.startDelay), fadeIn, Parallel(fadeBlast, scaleBlast), Func(self.cleanUpEffect))

    def setEffectColor(self, color):
        self.effectColor = color

    def setEffectScale(self, scale):
        self.effectScale = scale

    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        if self.pool and self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\effects\SkullBurst.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:19:57 Pacific Daylight Time
