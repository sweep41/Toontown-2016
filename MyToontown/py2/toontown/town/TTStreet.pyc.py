# 2013.08.22 22:26:53 Pacific Daylight Time
# Embedded file name: toontown.town.TTStreet
import Street

class TTStreet(Street.Street):
    __module__ = __name__

    def __init__(self, loader, parentFSM, doneEvent):
        Street.Street.__init__(self, loader, parentFSM, doneEvent)

    def load(self):
        Street.Street.load(self)

    def unload(self):
        Street.Street.unload(self)

    def doRequestLeave(self, requestStatus):
        self.fsm.request('trialerFA', [requestStatus])
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\town\TTStreet.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:26:53 Pacific Daylight Time
