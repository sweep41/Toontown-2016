from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyTrampolineActivityAI import DistributedPartyTrampolineActivityAI

class DistributedPartyWinterTrampolineActivityAI(DistributedPartyTrampolineActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyWinterTrampolineActivityAI")

