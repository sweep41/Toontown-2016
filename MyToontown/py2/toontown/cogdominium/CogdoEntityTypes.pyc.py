# 2013.08.22 22:17:33 Pacific Daylight Time
# Embedded file name: toontown.cogdominium.CogdoEntityTypes
from otp.level.EntityTypes import *

class CogdoLevelMgr(LevelMgr):
    __module__ = __name__
    type = 'levelMgr'


class CogdoBoardroomGameSettings(Entity):
    __module__ = __name__
    type = 'cogdoBoardroomGameSettings'
    attribs = (('TimerScale', 1.0, 'float'),)


class CogdoCraneGameSettings(Entity):
    __module__ = __name__
    type = 'cogdoCraneGameSettings'
    attribs = (('GameDuration', 180.0, 'float'),
     ('EmptyFrictionCoef', 0.1, 'float'),
     ('Gravity', -32, 'int'),
     ('RopeLinkMass', 1.0, 'float'),
     ('MagnetMass', 1.0, 'float'),
     ('MoneyBagGrabHeight', -8.2, 'float'))


class CogdoCraneCogSettings(Entity):
    __module__ = __name__
    type = 'cogdoCraneCogSettings'
    attribs = (('CogSpawnPeriod', 10.0, 'float'),
     ('CogWalkSpeed', 2.0, 'float'),
     ('CogMachineInteractDuration', 2.0, 'float'),
     ('CogFlyAwayHeight', 50.0, 'float'),
     ('CogFlyAwayDuration', 4.0, 'float'))
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\cogdominium\CogdoEntityTypes.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:17:33 Pacific Daylight Time
