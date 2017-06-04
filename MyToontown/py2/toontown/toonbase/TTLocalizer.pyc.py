# 2013.08.22 22:26:36 Pacific Daylight Time
# Embedded file name: toontown.toonbase.TTLocalizer
from pandac.libpandaexpressModules import *
import string
import types
try:
    language = getConfigExpress().GetString('language', 'english')
    checkLanguage = getConfigExpress().GetBool('check-language', 0)
except:
    language = simbase.config.GetString('language', 'english')
    checkLanguage = simbase.config.GetBool('check-language', 0)

def getLanguage():
    return language


print 'TTLocalizer: Running in language: %s' % language
if language == 'english':
    _languageModule = 'toontown.toonbase.TTLocalizer' + string.capitalize(language)
else:
    checkLanguage = 1
    _languageModule = 'toontown.toonbase.TTLocalizer_' + language
print 'from ' + _languageModule + ' import *'
from toontown.toonbase.TTLocalizerEnglish import *
if checkLanguage:
    l = {}
    g = {}
    englishModule = __import__('toontown.toonbase.TTLocalizerEnglish', g, l)
    foreignModule = __import__(_languageModule, g, l)
    for key, val in englishModule.__dict__.items():
        if not foreignModule.__dict__.has_key(key):
            print 'WARNING: Foreign module: %s missing key: %s' % (_languageModule, key)
            locals()[key] = val
        elif isinstance(val, types.DictType):
            fval = foreignModule.__dict__.get(key)
            for dkey, dval in val.items():
                if not fval.has_key(dkey):
                    print 'WARNING: Foreign module: %s missing key: %s.%s' % (_languageModule, key, dkey)
                    fval[dkey] = dval

            for dkey in fval.keys():
                if not val.has_key(dkey):
                    print 'WARNING: Foreign module: %s extra key: %s.%s' % (_languageModule, key, dkey)

    for key in foreignModule.__dict__.keys():
        if not englishModule.__dict__.has_key(key):
            print 'WARNING: Foreign module: %s extra key: %s' % (_languageModule, key)
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\toonbase\TTLocalizer.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:26:36 Pacific Daylight Time
