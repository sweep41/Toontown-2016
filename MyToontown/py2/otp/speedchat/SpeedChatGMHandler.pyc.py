# 2013.08.22 22:15:50 Pacific Daylight Time
# Embedded file name: otp.speedchat.SpeedChatGMHandler
from pandac.PandaModules import *
from direct.showbase import DirectObject
from otp.otpbase import OTPLocalizer

class SpeedChatGMHandler(DirectObject.DirectObject):
    __module__ = __name__
    scStructure = None
    scList = {}

    def __init__(self):
        if SpeedChatGMHandler.scStructure is None:
            self.generateSCStructure()
        return

    def generateSCStructure(self):
        SpeedChatGMHandler.scStructure = [OTPLocalizer.PSCMenuGM]
        phraseCount = 0
        numGMCategories = base.config.GetInt('num-gm-categories', 0)
        for i in range(0, numGMCategories):
            categoryName = base.config.GetString('gm-category-%d' % i, '')
            if categoryName == '':
                continue
            categoryStructure = [categoryName]
            numCategoryPhrases = base.config.GetInt('gm-category-%d-phrases' % i, 0)
            for j in range(0, numCategoryPhrases):
                phrase = base.config.GetString('gm-category-%d-phrase-%d' % (i, j), '')
                if phrase != '':
                    idx = 'gm%d' % phraseCount
                    SpeedChatGMHandler.scList[idx] = phrase
                    categoryStructure.append(idx)
                    phraseCount += 1

            SpeedChatGMHandler.scStructure.append(categoryStructure)

        numGMPhrases = base.config.GetInt('num-gm-phrases', 0)
        for i in range(0, numGMPhrases):
            phrase = base.config.GetString('gm-phrase-%d' % i, '')
            if phrase != '':
                idx = 'gm%d' % phraseCount
                SpeedChatGMHandler.scList[idx] = phrase
                SpeedChatGMHandler.scStructure.append(idx)
                phraseCount += 1

    def getStructure(self):
        return SpeedChatGMHandler.scStructure

    def getPhrase(self, id):
        return SpeedChatGMHandler.scList[id]
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\otp\speedchat\SpeedChatGMHandler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:15:50 Pacific Daylight Time
