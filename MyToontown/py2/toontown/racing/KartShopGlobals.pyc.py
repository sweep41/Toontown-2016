# 2013.08.22 22:24:15 Pacific Daylight Time
# Embedded file name: toontown.racing.KartShopGlobals
from direct.showbase import PythonUtil

class KartShopGlobals():
    __module__ = __name__
    EVENTDICT = {'guiDone': 'guiDone',
     'returnKart': 'returnKart',
     'buyKart': 'buyAKart',
     'buyAccessory': 'buyAccessory'}
    KARTCLERK_TIMER = 180
    MAX_KART_ACC = 16


class KartGlobals():
    __module__ = __name__
    ENTER_MOVIE = 1
    EXIT_MOVIE = 2
    COUNTDOWN_TIME = 30
    BOARDING_TIME = 10.0
    ENTER_RACE_TIME = 6.0
    ERROR_CODE = PythonUtil.Enum('success, eGeneric, eTickets, eBoardOver, eNoKart, eOccupied, eTrackClosed, eTooLate, eUnpaid')
    FRONT_LEFT_SPOT = 0
    FRONT_RIGHT_SPOT = 1
    REAR_LEFT_SPOT = 2
    REAR_RIGHT_SPOT = 3
    PAD_GROUP_NUM = 4

    def getPadLocation(padId):
        return padId % KartGlobals.PAD_GROUP_NUM

    getPadLocation = staticmethod(getPadLocation)
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\racing\KartShopGlobals.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:24:15 Pacific Daylight Time
