# 2013.08.22 22:15:28 Pacific Daylight Time
# Embedded file name: otp.level.DistributedEntity
from direct.distributed import DistributedObject
import Entity
from direct.directnotify import DirectNotifyGlobal

class DistributedEntity(DistributedObject.DistributedObject, Entity.Entity):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEntity')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        Entity.Entity.__init__(self)
        self.levelDoId = 0
        self.entId = 0
        self.level = None
        return

    def generateInit(self):
        DistributedEntity.notify.debug('generateInit')
        DistributedObject.DistributedObject.generateInit(self)

    def generate(self):
        DistributedEntity.notify.debug('generate')
        DistributedObject.DistributedObject.generate(self)

    def setLevelDoId(self, levelDoId):
        DistributedEntity.notify.debug('setLevelDoId: %s' % levelDoId)
        self.levelDoId = levelDoId

    def setEntId(self, entId):
        DistributedEntity.notify.debug('setEntId: %s' % entId)
        self.entId = entId

    def announceGenerate(self):
        DistributedEntity.notify.debug('announceGenerate (%s)' % self.entId)
        if self.levelDoId != 0:
            level = base.cr.doId2do[self.levelDoId]
            self.initializeEntity(level, self.entId)
            self.level.onEntityCreate(self.entId)
        else:
            self.level = None
        DistributedObject.DistributedObject.announceGenerate(self)
        return

    def disable(self):
        DistributedEntity.notify.debug('disable (%s)' % self.entId)
        self.destroy()
        DistributedObject.DistributedObject.disable(self)

    def delete(self):
        DistributedEntity.notify.debug('delete')
        DistributedObject.DistributedObject.delete(self)
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\otp\level\DistributedEntity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:15:29 Pacific Daylight Time
