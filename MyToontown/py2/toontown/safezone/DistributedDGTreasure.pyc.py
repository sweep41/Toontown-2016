# 2013.08.22 22:24:28 Pacific Daylight Time
# Embedded file name: toontown.safezone.DistributedDGTreasure
import DistributedSZTreasure

class DistributedDGTreasure(DistributedSZTreasure.DistributedSZTreasure):
    __module__ = __name__

    def __init__(self, cr):
        DistributedSZTreasure.DistributedSZTreasure.__init__(self, cr)
        self.modelPath = 'phase_8/models/props/flower_treasure'
        self.grabSoundPath = 'phase_4/audio/sfx/SZ_DD_treasure.mp3'
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\safezone\DistributedDGTreasure.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:24:28 Pacific Daylight Time
