# 2013.08.22 22:15:32 Pacific Daylight Time
# Embedded file name: otp.level.EntityTypes
from EntityTypeDesc import EntityTypeDesc
from toontown.coghq.SpecImports import *

class Entity(EntityTypeDesc):
    __module__ = __name__
    abstract = 1
    type = 'entity'
    attribs = (('type', None, 'const'),
     ('name', '<unnamed>', 'string'),
     ('comment', '', 'string'),
     ('parentEntId', 0, 'entId'))


class LevelMgr(Entity):
    __module__ = __name__
    type = 'levelMgr'
    permanent = 1
    attribs = (('name', 'LevelMgr', 'const'), ('parentEntId', 0, 'const'), ('modelFilename', '', 'const'))


class EditMgr(Entity):
    __module__ = __name__
    type = 'editMgr'
    permanent = 1
    blockAttribs = ('comment',)
    attribs = (('name', 'LevelMgr', 'const'),
     ('parentEntId', 0, 'const'),
     ('requestSave', None, 'const'),
     ('requestNewEntity', None, 'const'),
     ('insertEntity', None, 'const'),
     ('removeEntity', None, 'const'))


class AttribModifier(Entity):
    __module__ = __name__
    type = 'attribModifier'
    attribs = (('recursive', 0, 'bool'),
     ('typeName', '', 'string'),
     ('attribName', '', 'string'),
     ('value', '', 'string'))


class Locator(Entity):
    __module__ = __name__
    type = 'locator'
    attribs = (('searchPath', '', 'string'),)


class Nodepath(Entity):
    __module__ = __name__
    type = 'nodepath'
    attribs = (('parentEntId',
      0,
      'entId',
      {'type': 'nodepath'}),
     ('pos', Point3(0, 0, 0), 'pos'),
     ('hpr', Vec3(0, 0, 0), 'hpr'),
     ('scale', 1, 'scale'))


class Zone(Nodepath):
    __module__ = __name__
    type = 'zone'
    permanent = 1
    blockAttribs = ('pos', 'hpr')
    attribs = (('parentEntId', 0, 'const'), ('description', '', 'string'), ('visibility', [], 'visZoneList'))


class EntrancePoint(Nodepath):
    __module__ = __name__
    type = 'entrancePoint'
    attribs = (('entranceId', -1, 'int'), ('radius',
      15,
      'float',
      {'min': 0}), ('theta',
      20,
      'float',
      {'min': 0}))


class LogicGate(Entity):
    __module__ = __name__
    type = 'logicGate'
    output = 'bool'
    attribs = (('input1Event',
      0,
      'entId',
      {'output': 'bool'}),
     ('input2Event',
      0,
      'entId',
      {'output': 'bool'}),
     ('isInput1', 0, 'bool'),
     ('isInput2', 0, 'bool'),
     ('logicType',
      'or',
      'choice',
      {'choiceSet': ['or',
                     'and',
                     'xor',
                     'nand',
                     'nor',
                     'xnor']}))


class CutScene(Entity):
    __module__ = __name__
    type = 'cutScene'
    output = 'bool'
    attribs = (('pos', Point3(0, 0, 0), 'pos'),
     ('hpr', Vec3(0, 0, 0), 'hpr'),
     ('startStopEvent',
      0,
      'entId',
      {'output': 'bool'}),
     ('effect',
      'irisInOut',
      'choice',
      {'choiceSet': ['nothing', 'irisInOut', 'letterBox']}),
     ('motion',
      'foo1',
      'choice',
      {'choiceSet': ['foo1']}),
     ('duration', 5.0, 'float'))


class CollisionSolid(Nodepath):
    __module__ = __name__
    type = 'collisionSolid'
    attribs = (('solidType',
      'sphere',
      'choice',
      {'choiceSet': ['sphere', 'tube']}),
     ('radius', 1.0, 'float'),
     ('length', 0.0, 'float'),
     ('showSolid', 0, 'bool'))


class Model(Nodepath):
    __module__ = __name__
    type = 'model'
    attribs = (('loadType',
      'loadModelCopy',
      'choice',
      {'choiceSet': ['loadModelCopy', 'loadModel', 'loadModelOnce']}),
     ('modelPath', None, 'bamfilename'),
     ('flattenType',
      'light',
      'choice',
      {'choiceSet': ['none',
                     'light',
                     'medium',
                     'strong']}),
     ('collisionsOnly', 0, 'bool'),
     ('goonHatType',
      'none',
      'choice',
      {'choiceSet': ['none', 'hardhat', 'security']}))


class Path(Nodepath):
    __module__ = __name__
    type = 'path'
    attribs = (('pathIndex', 0, 'int'), ('pathScale', 1.0, 'float'))


class VisibilityExtender(Entity):
    __module__ = __name__
    type = 'visibilityExtender'
    attribs = (('event',
      None,
      'entId',
      {'output': 'bool'}), ('newZones', [], 'visZoneList'))


class AmbientSound(Nodepath):
    __module__ = __name__
    type = 'ambientSound'
    attribs = (('soundPath', '', 'bamfilename'), ('volume',
      1,
      'float',
      {'min': 0,
       'max': 1}), ('enabled', 1, 'bool'))


class PropSpinner(Entity):
    __module__ = __name__
    type = 'propSpinner'


class EntityGroup(Entity):
    __module__ = __name__
    type = 'entityGroup'
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\otp\level\EntityTypes.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:15:32 Pacific Daylight Time
