# 2013.08.22 22:26:01 Pacific Daylight Time
# Embedded file name: toontown.toon.HealthForceAcknowledge
from pandac.PandaModules import *
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer

class HealthForceAcknowledge():
    __module__ = __name__

    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.dialog = None
        return

    def enter(self, hpLevel):
        doneStatus = {}
        toonHp = base.localAvatar.getHp()
        if toonHp >= hpLevel:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [doneStatus])
        else:
            base.localAvatar.b_setAnimState('neutral', 1)
            doneStatus['mode'] = 'incomplete'
            self.doneStatus = doneStatus
            msg = TTLocalizer.HealthForceAcknowledgeMessage
            self.dialog = TTDialog.TTDialog(text=msg, command=self.handleOk, style=TTDialog.Acknowledge)

    def exit(self):
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        return

    def handleOk(self, value):
        messenger.send(self.doneEvent, [self.doneStatus])
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\toon\HealthForceAcknowledge.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:26:01 Pacific Daylight Time
