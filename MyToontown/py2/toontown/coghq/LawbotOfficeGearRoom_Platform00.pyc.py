# 2013.08.22 22:19:12 Pacific Daylight Time
# Embedded file name: toontown.coghq.LawbotOfficeGearRoom_Platform00
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone7a',
        'wantDoors': 1},
 1001: {'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 100008: {'type': 'healBarrel',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(9.21172, -65.1636, 0),
          'hpr': Vec3(218.48, 0, 0),
          'scale': Vec3(1, 1, 1),
          'rewardPerGrab': 20,
          'rewardPerGrabMax': 0},
 100000: {'type': 'model',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 100001,
          'pos': Point3(-7.80516, 13.4827, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(2.5, 2.5, 2.5),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBoxX2'},
 100002: {'type': 'model',
          'name': 'copy of <unnamed>',
          'comment': '',
          'parentEntId': 100001,
          'pos': Point3(-22.7622, 13.4827, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(2.5, 2.5, 2.5),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBoxX3'},
 100003: {'type': 'model',
          'name': 'copy of <unnamed> (2)',
          'comment': '',
          'parentEntId': 100001,
          'pos': Point3(-22.5819, -16.4761, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(2.5, 2.5, 2.5),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox'},
 100004: {'type': 'model',
          'name': 'copy of <unnamed> (3)',
          'comment': '',
          'parentEntId': 100001,
          'pos': Point3(7.45035, -18.4214, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(2.5, 2.5, 2.75),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBoxX2'},
 100005: {'type': 'model',
          'name': 'copy of <unnamed> (4)',
          'comment': '',
          'parentEntId': 100001,
          'pos': Point3(-7.74191, -16.7512, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(2.5, 2.5, 2.75),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBoxX2'},
 100009: {'type': 'model',
          'name': 'copy of <unnamed> (4)',
          'comment': '',
          'parentEntId': 100001,
          'pos': Point3(7.38913, -1.56591, 31.7727),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(2.3, 2.9, 2.62459),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_metal_crate'},
 100017: {'type': 'model',
          'name': 'copy of <unnamed> (3)',
          'comment': '',
          'parentEntId': 100001,
          'pos': Point3(-7.94704, -1.56591, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(2.3, 2.92, 2.92),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox'},
 100012: {'type': 'mover',
          'name': 'mover',
          'comment': '',
          'parentEntId': 100011,
          'pos': Point3(0, -10, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cycleType': 'loop',
          'entity2Move': 100014,
          'modelPath': 0,
          'moveTarget': 100013,
          'pos0Move': 2,
          'pos0Wait': 2,
          'pos1Move': 2,
          'pos1Wait': 2,
          'startOn': 1,
          'switchId': 0},
 100001: {'type': 'nodepath',
          'name': 'crateMaster',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': 1},
 100011: {'type': 'nodepath',
          'name': 'spotlightMover',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(29.8179, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100013: {'type': 'nodepath',
          'name': 'mover target',
          'comment': '',
          'parentEntId': 100011,
          'pos': Point3(0, 10, 0),
          'hpr': Point3(180, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100015: {'type': 'nodepath',
          'name': 'lightTarget1',
          'comment': '',
          'parentEntId': 100011,
          'pos': Point3(0, -10, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': 1},
 100016: {'type': 'nodepath',
          'name': 'copy of lightTarget1',
          'comment': '',
          'parentEntId': 100011,
          'pos': Point3(0, 10, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100010: {'type': 'platform',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-22.5404, -1.15634, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1.18055, 1.18055, 1.18055),
          'floorName': 'platformcollision',
          'modelPath': 'phase_9/models/cogHQ/platform1',
          'modelScale': Point3(1, 1, 2),
          'motion': 'noBlend',
          'offset': Point3(0, 0, 15),
          'period': 4.0,
          'phaseShift': 0.0,
          'waitPercent': 0.1},
 100014: {'type': 'securityCamera',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 100011,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': 1,
          'accel': 10.0,
          'damPow': 8,
          'hideModel': 0,
          'maxVel': 30.0,
          'modelPath': 0,
          'projector': Point3(0, 0, 25),
          'radius': 7.0,
          'switchId': 0,
          'trackTarget1': 100015,
          'trackTarget2': 100016,
          'trackTarget3': 0},
 100006: {'type': 'stomper',
          'name': 'copy of <unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-22.9004, -31.939, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'animateShadow': 1,
          'cogStyle': 1,
          'crushCellId': None,
          'damage': 10,
          'headScale': Point3(7, 3, 7),
          'modelPath': 0,
          'motion': 3,
          'period': 4.0,
          'phaseShift': 0.0,
          'range': 15.0,
          'removeCamBarrierCollisions': 0,
          'removeHeadFloor': 0,
          'shaftScale': Point3(0.5, 20, 0.5),
          'soundLen': 0,
          'soundOn': 1,
          'soundPath': 0,
          'style': 'vertical',
          'switchId': 0,
          'wantShadow': 1,
          'wantSmoke': 1,
          'zOffset': 0},
 100007: {'type': 'stomper',
          'name': 'copy of <unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(6.83388, -1.26706, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'animateShadow': 1,
          'cogStyle': 1,
          'crushCellId': None,
          'damage': 10,
          'headScale': Point3(7, 3, 7),
          'modelPath': 0,
          'motion': 3,
          'period': 4.0,
          'phaseShift': 0.3,
          'range': 15.0,
          'removeCamBarrierCollisions': 0,
          'removeHeadFloor': 0,
          'shaftScale': Point3(0.5, 20, 0.5),
          'soundLen': 0,
          'soundOn': 1,
          'soundPath': 0,
          'style': 'vertical',
          'switchId': 0,
          'wantShadow': 1,
          'wantSmoke': 1,
          'zOffset': 0},
 100018: {'type': 'stomper',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-37.5869, -1.26706, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'animateShadow': 1,
          'cogStyle': 1,
          'crushCellId': None,
          'damage': 10,
          'headScale': Point3(7, 3, 7),
          'modelPath': 0,
          'motion': 4,
          'period': 2.5,
          'phaseShift': 0.6,
          'range': 15.0,
          'removeCamBarrierCollisions': 0,
          'removeHeadFloor': 0,
          'shaftScale': Point3(0.5, 20, 0.5),
          'soundLen': 0,
          'soundOn': 1,
          'soundPath': 0,
          'style': 'vertical',
          'switchId': 0,
          'wantShadow': 1,
          'wantSmoke': 1,
          'zOffset': 0}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\coghq\LawbotOfficeGearRoom_Platform00.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:19:12 Pacific Daylight Time
