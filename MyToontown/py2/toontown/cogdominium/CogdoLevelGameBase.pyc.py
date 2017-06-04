# 2013.08.22 22:17:45 Pacific Daylight Time
# Embedded file name: toontown.cogdominium.CogdoLevelGameBase
from direct.fsm.StatePush import FunctionCall
from otp.level.EntityStateVarSet import EntityStateVarSet
from otp.level.LevelSpec import LevelSpec

class CogdoLevelGameBase():
    __module__ = __name__

    def getLevelSpec(self):
        return LevelSpec(self.getSpec())

    if __dev__:

        def startHandleEdits(self):
            fcs = []
            Consts = self.getConsts()
            for item in Consts.__dict__.itervalues():
                if isinstance(item, EntityStateVarSet):
                    for attribName in item._getAttributeNames():
                        handler = getattr(self, '_handle%sChanged' % attribName, None)
                        if handler:
                            stateVar = getattr(item, attribName)
                            fcs.append(FunctionCall(handler, stateVar))

            self._functionCalls = fcs
            return

        def stopHandleEdits(self):
            if __dev__:
                for fc in self._functionCalls:
                    fc.destroy()

                self._functionCalls = None
            return

        def getEntityTypeReg(self):
            import CogdoEntityTypes
            from otp.level import EntityTypeRegistry
            typeReg = EntityTypeRegistry.EntityTypeRegistry(CogdoEntityTypes)
            return typeReg
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\cogdominium\CogdoLevelGameBase.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:17:45 Pacific Daylight Time
