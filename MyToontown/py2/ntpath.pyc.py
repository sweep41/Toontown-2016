# 2013.08.22 22:13:11 Pacific Daylight Time
# Embedded file name: ntpath
import os
import stat
import sys
__all__ = ['normcase',
 'isabs',
 'join',
 'splitdrive',
 'split',
 'splitext',
 'basename',
 'dirname',
 'commonprefix',
 'getsize',
 'getmtime',
 'getatime',
 'getctime',
 'islink',
 'exists',
 'isdir',
 'isfile',
 'ismount',
 'walk',
 'expanduser',
 'expandvars',
 'normpath',
 'abspath',
 'splitunc',
 'curdir',
 'pardir',
 'sep',
 'pathsep',
 'defpath',
 'altsep',
 'extsep',
 'devnull',
 'realpath',
 'supports_unicode_filenames']
curdir = '.'
pardir = '..'
extsep = '.'
sep = '\\'
pathsep = ';'
altsep = '/'
defpath = '.;C:\\bin'
if 'ce' in sys.builtin_module_names:
    defpath = '\\Windows'
elif 'os2' in sys.builtin_module_names:
    altsep = '/'
devnull = 'nul'

def normcase(s):
    return s.replace('/', '\\').lower()


def isabs(s):
    s = splitdrive(s)[1]
    return s != '' and s[:1] in '/\\'


def join(a, *p):
    path = a
    for b in p:
        b_wins = 0
        if path == '':
            b_wins = 1
        elif isabs(b):
            if path[1:2] != ':' or b[1:2] == ':':
                b_wins = 1
            elif len(path) > 3 or len(path) == 3 and path[-1] not in '/\\':
                b_wins = 1
        if b_wins:
            path = b
        elif path[-1] in '/\\':
            if b and b[0] in '/\\':
                path += b[1:]
            else:
                path += b
        elif path[-1] == ':':
            path += b
        elif b:
            if b[0] in '/\\':
                path += b
            else:
                path += '\\' + b
        else:
            path += '\\'

    return path


def splitdrive(p):
    if p[1:2] == ':':
        return (p[0:2], p[2:])
    return ('', p)


def splitunc(p):
    if p[1:2] == ':':
        return ('', p)
    firstTwo = p[0:2]
    if firstTwo == '//' or firstTwo == '\\\\':
        normp = normcase(p)
        index = normp.find('\\', 2)
        if index == -1:
            return ('', p)
        index = normp.find('\\', index + 1)
        if index == -1:
            index = len(p)
        return (p[:index], p[index:])
    return ('', p)


def split(p):
    d, p = splitdrive(p)
    i = len(p)
    while i and p[i - 1] not in '/\\':
        i = i - 1

    head, tail = p[:i], p[i:]
    head2 = head
    while head2 and head2[-1] in '/\\':
        head2 = head2[:-1]

    head = head2 or head
    return (d + head, tail)


def splitext(p):
    i = p.rfind('.')
    if i <= max(p.rfind('/'), p.rfind('\\')):
        return (p, '')
    else:
        return (p[:i], p[i:])


def basename(p):
    return split(p)[1]


def dirname(p):
    return split(p)[0]


def commonprefix(m):
    if not m:
        return ''
    prefix = m[0]
    for item in m:
        for i in range(len(prefix)):
            if prefix[:i + 1] != item[:i + 1]:
                prefix = prefix[:i]
                if i == 0:
                    return ''
                break

    return prefix


def getsize(filename):
    return os.stat(filename).st_size


def getmtime(filename):
    return os.stat(filename).st_mtime


def getatime(filename):
    return os.stat(filename).st_atime


def getctime(filename):
    return os.stat(filename).st_ctime


def islink(path):
    return False


def exists(path):
    try:
        st = os.stat(path)
    except os.error:
        return False

    return True


lexists = exists

def isdir(path):
    try:
        st = os.stat(path)
    except os.error:
        return False

    return stat.S_ISDIR(st.st_mode)


def isfile(path):
    try:
        st = os.stat(path)
    except os.error:
        return False

    return stat.S_ISREG(st.st_mode)


def ismount(path):
    unc, rest = splitunc(path)
    if unc:
        return rest in ('', '/', '\\')
    p = splitdrive(path)[1]
    return len(p) == 1 and p[0] in '/\\'


def walk(top, func, arg):
    try:
        names = os.listdir(top)
    except os.error:
        return

    func(arg, top, names)
    exceptions = ('.', '..')
    for name in names:
        if name not in exceptions:
            name = join(top, name)
            if isdir(name):
                walk(name, func, arg)


def expanduser(path):
    if path[:1] != '~':
        return path
    i, n = 1, len(path)
    while i < n and path[i] not in '/\\':
        i = i + 1

    if i == 1:
        if 'HOME' in os.environ:
            userhome = os.environ['HOME']
        elif 'HOMEPATH' not in os.environ:
            return path
        else:
            try:
                drive = os.environ['HOMEDRIVE']
            except KeyError:
                drive = ''

            userhome = join(drive, os.environ['HOMEPATH'])
    else:
        return path
    return userhome + path[i:]


def expandvars(path):
    if '$' not in path:
        return path
    import string
    varchars = string.ascii_letters + string.digits + '_-'
    res = ''
    index = 0
    pathlen = len(path)
    while index < pathlen:
        c = path[index]
        if c == "'":
            path = path[index + 1:]
            pathlen = len(path)
            try:
                index = path.index("'")
                res = res + "'" + path[:index + 1]
            except ValueError:
                res = res + path
                index = pathlen - 1

        elif c == '$':
            if path[index + 1:index + 2] == '$':
                res = res + c
                index = index + 1
            elif path[index + 1:index + 2] == '{':
                path = path[index + 2:]
                pathlen = len(path)
                try:
                    index = path.index('}')
                    var = path[:index]
                    if var in os.environ:
                        res = res + os.environ[var]
                except ValueError:
                    res = res + path
                    index = pathlen - 1

            else:
                var = ''
                index = index + 1
                c = path[index:index + 1]
                while c != '' and c in varchars:
                    var = var + c
                    index = index + 1
                    c = path[index:index + 1]

                if var in os.environ:
                    res = res + os.environ[var]
                if c != '':
                    res = res + c
        else:
            res = res + c
        index = index + 1

    return res


def normpath(path):
    path = path.replace('/', '\\')
    prefix, path = splitdrive(path)
    if prefix == '':
        while path[:1] == '\\':
            prefix = prefix + '\\'
            path = path[1:]

    elif path.startswith('\\'):
        prefix = prefix + '\\'
        path = path.lstrip('\\')
    comps = path.split('\\')
    i = 0
    while i < len(comps):
        if comps[i] in ('.', ''):
            del comps[i]
        elif comps[i] == '..':
            if i > 0 and comps[i - 1] != '..':
                del comps[i - 1:i + 1]
                i -= 1
            elif i == 0 and prefix.endswith('\\'):
                del comps[i]
            else:
                i += 1
        else:
            i += 1

    if not prefix and not comps:
        comps.append('.')
    return prefix + '\\'.join(comps)


def abspath(path):
    global abspath
    try:
        from nt import _getfullpathname
    except ImportError:

        def _abspath(path):
            if not isabs(path):
                path = join(os.getcwd(), path)
            return normpath(path)

        abspath = _abspath
        return _abspath(path)

    if path:
        try:
            path = _getfullpathname(path)
        except WindowsError:
            pass

    else:
        path = os.getcwd()
    return normpath(path)


realpath = abspath
supports_unicode_filenames = hasattr(sys, 'getwindowsversion') and sys.getwindowsversion()[3] >= 2
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\ntpath.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:13:12 Pacific Daylight Time
