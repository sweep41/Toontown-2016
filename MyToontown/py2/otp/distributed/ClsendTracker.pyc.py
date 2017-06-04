# 2013.08.22 22:15:16 Pacific Daylight Time
# Embedded file name: otp.distributed.ClsendTracker
from pandac.PandaModules import StringStream
from direct.distributed.PyDatagram import PyDatagram
import random

class ClsendTracker():
    __module__ = __name__
    clsendNotify = directNotify.newCategory('clsend')
    NumTrackersLoggingOverflow = 0
    MaxTrackersLoggingOverflow = config.GetInt('max-clsend-loggers', 5)

    def __init__(self):
        self._logClsendOverflow = False
        if self.isPlayerControlled():
            if simbase.air.getTrackClsends():
                if ClsendTracker.NumTrackersLoggingOverflow < ClsendTracker.MaxTrackersLoggingOverflow:
                    self._logClsendOverflow = random.random() < 1.0 / config.GetFloat('clsend-log-one-av-in-every', choice(__dev__, 4, 50))
        if self._logClsendOverflow:
            ClsendTracker.NumTrackersLoggingOverflow += 1
        self._clsendMsgs = []
        self._clsendBufLimit = 100
        self._clsendFlushNum = 20
        self._clsendCounter = 0

    def announceGenerate(self):
        if self._logClsendOverflow:
            self.clsendNotify.info('logging all clsends for %s' % self.doId)

    def destroy(self):
        if self._logClsendOverflow:
            ClsendTracker.NumTrackersLoggingOverflow -= 1

    def trackClientSendMsg(self, dataStr):
        self._clsendMsgs.append((self.air.getAvatarIdFromSender(), dataStr))
        if len(self._clsendMsgs) >= self._clsendBufLimit:
            self._trimClsend()

    def _trimClsend(self):
        for i in xrange(self._clsendFlushNum):
            if self._logClsendOverflow:
                self._logClsend(*self._clsendMsgs[0])
            self._clsendMsgs = self._clsendMsgs[1:]
            self._clsendCounter += 1

    def _logClsend(self, senderId, dataStr):
        msgStream = StringStream()
        simbase.air.describeMessage(msgStream, '', dataStr)
        readableStr = msgStream.getData()
        sstream = StringStream()
        PyDatagram(dataStr).dumpHex(sstream)
        hexDump = sstream.getData()
        self.clsendNotify.info('%s [%s]: %s%s' % (self.doId,
         self._clsendCounter,
         readableStr,
         hexDump))

    def dumpClientSentMsgs(self):
        for msg in self._clsendMsgs:
            self._logClsend(*msg)
            self._clsendCounter += 1
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\otp\distributed\ClsendTracker.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:15:16 Pacific Daylight Time
