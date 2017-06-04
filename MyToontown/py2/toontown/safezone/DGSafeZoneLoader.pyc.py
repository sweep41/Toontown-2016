# 2013.08.22 22:24:24 Pacific Daylight Time
# Embedded file name: toontown.safezone.DGSafeZoneLoader
from pandac.PandaModules import *
import SafeZoneLoader
import DGPlayground

class DGSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    __module__ = __name__

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DGPlayground.DGPlayground
        self.musicFile = 'phase_8/audio/bgm/DG_nbrhood.mid'
        self.activityMusicFile = 'phase_8/audio/bgm/DG_SZ.mid'
        self.dnaFile = 'phase_8/dna/daisys_garden_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_8/dna/storage_DG_sz.dna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.bird1Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_01.mp3')
        self.bird2Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_02.mp3')
        self.bird3Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_03.mp3')
        self.bird4Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_04.mp3')

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.bird1Sound
        del self.bird2Sound
        del self.bird3Sound
        del self.bird4Sound

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\safezone\DGSafeZoneLoader.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:24:24 Pacific Daylight Time
