# 2013.08.22 22:21:01 Pacific Daylight Time
# Embedded file name: toontown.launcher.DownloadForceAcknowledge
from pandac.PandaModules import *
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer
import random

class DownloadForceAcknowledge():
    __module__ = __name__

    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.dialog = None
        return

    def enter(self, phase):
        doneStatus = {}
        if launcher.getPhaseComplete(phase):
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [doneStatus])
        else:
            try:
                base.localAvatar.b_setAnimState('neutral', 1)
            except:
                pass

            doneStatus['mode'] = 'incomplete'
            self.doneStatus = doneStatus
            percentComplete = base.launcher.getPercentPhaseComplete(phase)
            phaseName = TTLocalizer.LauncherPhaseNames[phase]
            verb = random.choice(TTLocalizer.DownloadForceAcknowledgeVerbList)
            msg = TTLocalizer.DownloadForceAcknowledgeMsg % {'phase': phaseName,
             'verb': verb}
            self.dialog = TTDialog.TTDialog(text=msg, command=self.handleOk, style=TTDialog.Acknowledge)
            self.dialog.show()

    def exit(self):
        if self.dialog:
            self.dialog.hide()
            self.dialog.cleanup()
            self.dialog = None
        return

    def handleOk(self, value):
        messenger.send(self.doneEvent, [self.doneStatus])
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\launcher\DownloadForceAcknowledge.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:21:01 Pacific Daylight Time
