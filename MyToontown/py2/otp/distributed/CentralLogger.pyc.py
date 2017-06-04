# 2013.08.22 22:15:15 Pacific Daylight Time
# Embedded file name: otp.distributed.CentralLogger
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
REPORT_PLAYER = 'REPORT_PLAYER'
ReportFoulLanguage = 'MODERATION_FOUL_LANGUAGE'
ReportPersonalInfo = 'MODERATION_PERSONAL_INFO'
ReportRudeBehavior = 'MODERATION_RUDE_BEHAVIOR'
ReportBadName = 'MODERATION_BAD_NAME'
ReportHacking = 'MODERATION_HACKING'

class CentralLogger(DistributedObjectGlobal):
    __module__ = __name__
    PlayersReportedThisSession = {}

    def hasReportedPlayer(self, targetDISLId, targetAvId):
        return self.PlayersReportedThisSession.has_key((targetDISLId, targetAvId))

    def reportPlayer(self, category, targetDISLId, targetAvId, description = 'None'):
        if self.hasReportedPlayer(targetDISLId, targetAvId):
            return False
        self.PlayersReportedThisSession[targetDISLId, targetAvId] = 1
        self.sendUpdate('sendMessage', [category,
         REPORT_PLAYER,
         targetDISLId,
         targetAvId])
        return True

    def writeClientEvent(self, eventString):
        self.sendUpdate('sendMessage', ['ClientEvent',
         eventString,
         0,
         0])
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\otp\distributed\CentralLogger.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:15:16 Pacific Daylight Time
