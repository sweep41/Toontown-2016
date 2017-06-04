# 2013.08.22 22:25:10 Pacific Daylight Time
# Embedded file name: toontown.speedchat.TTSCSillyPhaseThreeMenu
from direct.showbase import PythonUtil
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat.SCMenuHolder import SCMenuHolder
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from otp.otpbase import OTPLocalizer
SillyPhaseThreeMenu = [(OTPLocalizer.SillyHolidayMenuSections[1], [30323,
   30324,
   30325,
   30326,
   30327]), (OTPLocalizer.SillyHolidayMenuSections[2], [30318,
   30319,
   30320,
   30321,
   30322])]

class TTSCSillyPhaseThreeMenu(SCMenu):
    __module__ = __name__

    def __init__(self):
        SCMenu.__init__(self)
        self.__SillyPhaseThreeMessagesChanged()
        submenus = []

    def destroy(self):
        SCMenu.destroy(self)

    def clearMenu(self):
        SCMenu.clearMenu(self)

    def __SillyPhaseThreeMessagesChanged(self):
        self.clearMenu()
        try:
            lt = base.localAvatar
        except:
            return

        for section in SillyPhaseThreeMenu:
            if section[0] == -1:
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print 'warning: tried to link Silly PhaseThree phrase %s which does not seem to exist' % phrase
                        break
                    self.append(SCStaticTextTerminal(phrase))

            else:
                menu = SCMenu()
                for phrase in section[1]:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print 'warning: tried to link Silly PhaseThree phrase %s which does not seem to exist' % phrase
                        break
                    menu.append(SCStaticTextTerminal(phrase))

                menuName = str(section[0])
                self.append(SCMenuHolder(menuName, menu))
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\speedchat\TTSCSillyPhaseThreeMenu.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:25:10 Pacific Daylight Time
