// Filename: eggCharacterData.I
// Created by:  drose (23Feb01)
//
////////////////////////////////////////////////////////////////////
//
// PANDA 3D SOFTWARE
// Copyright (c) Carnegie Mellon University.  All rights reserved.
//
// All use of this software is subject to the terms of the revised BSD
// license.  You should have received a copy of this license along
// with this source code in a file named "LICENSE."
//
////////////////////////////////////////////////////////////////////



////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::get_num_models
//       Access: Public
//  Description: Returns the total number of models associated with
//               this character.
//
//               A "model" here is either a character model (or one
//               LOD of a character model), or a character animation
//               file: in either case, a hierarchy of joints.
////////////////////////////////////////////////////////////////////
INLINE int EggCharacterData::
get_num_models() const {
  return _models.size();
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::get_model_index
//       Access: Public
//  Description: Returns the model_index of the nth model associated
//               with this character.  This model_index may be used to
//               ask questions about the particular model from the
//               EggCharacterCollection object, or from the individual
//               EggJointData and EggSliderData objects.
//
//               A "model" here is either a character model (or one
//               LOD of a character model), or a character animation
//               file: in either case, a hierarchy of joints.
////////////////////////////////////////////////////////////////////
INLINE int EggCharacterData::
get_model_index(int n) const {
  nassertr(n >= 0 && n < (int)_models.size(), 0);
  return _models[n]._model_index;
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::get_model_root
//       Access: Public
//  Description: Returns the model_root of the nth model associated
//               with this character.
//
//               This is the node at which the character, animation
//               bundle, or LOD officially began within its particular
//               egg file.
////////////////////////////////////////////////////////////////////
INLINE EggNode *EggCharacterData::
get_model_root(int n) const {
  nassertr(n >= 0 && n < (int)_models.size(), (EggNode *)NULL);
  return _models[n]._model_root;
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::get_egg_data
//       Access: Public
//  Description: Returns the EggData representing the egg file that
//               defined this particular model.  Note that one egg
//               file might contain multiple models.
////////////////////////////////////////////////////////////////////
INLINE EggData *EggCharacterData::
get_egg_data(int n) const {
  nassertr(n >= 0 && n < (int)_models.size(), (EggData *)NULL);
  return _models[n]._egg_data;
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::get_root_joint
//       Access: Public
//  Description: Returns the root joint of the character hierarchy.
//               This root joint does not represent an actual joint in
//               the hierarchy, but instead is a fictitious joint that
//               is the parent of all the top joints in the hierarchy
//               (since the hierarchy may actually contain zero or
//               more top joints).
////////////////////////////////////////////////////////////////////
INLINE EggJointData *EggCharacterData::
get_root_joint() const {
  return _root_joint;
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::find_joint
//       Access: Public
//  Description: Returns the first joint found with the indicated
//               name, or NULL if no joint has that name.
////////////////////////////////////////////////////////////////////
INLINE EggJointData *EggCharacterData::
find_joint(const string &name) const {
  return _root_joint->find_joint(name);
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::make_new_joint
//       Access: Public
//  Description: Creates a new joint as a child of the indicated joint
//               and returns it.  The new joint will be initialized to
//               the identity transform, so that in inherits the
//               net transform of the indicated parent joint.
////////////////////////////////////////////////////////////////////
INLINE EggJointData *EggCharacterData::
make_new_joint(const string &name, EggJointData *parent) {
  EggJointData *joint = parent->make_new_joint(name);
  _joints.push_back(joint);
  _components.push_back(joint);
  return joint;
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::get_num_joints
//       Access: Public
//  Description: Returns the total number of joints in the character
//               joint hierarchy.
////////////////////////////////////////////////////////////////////
INLINE int EggCharacterData::
get_num_joints() const {
  return _joints.size();
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::get_joint
//       Access: Public
//  Description: Returns the nth joint in the character joint
//               hierarchy.  This returns all of the joints in the
//               hierarchy in an arbitrary ordering.
////////////////////////////////////////////////////////////////////
INLINE EggJointData *EggCharacterData::
get_joint(int n) const {
  nassertr(n >= 0 && n < (int)_joints.size(), NULL);
  return _joints[n];
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::get_num_sliders
//       Access: Public
//  Description: Returns the number of sliders in the character
//               slider list.
////////////////////////////////////////////////////////////////////
INLINE int EggCharacterData::
get_num_sliders() const {
  return _sliders.size();
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::get_slider
//       Access: Public
//  Description: Returns the nth slider in the character slider list.
////////////////////////////////////////////////////////////////////
INLINE EggSliderData *EggCharacterData::
get_slider(int n) const {
  nassertr(n >= 0 && n < (int)_sliders.size(), NULL);
  return _sliders[n];
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::get_num_components
//       Access: Public
//  Description: Returns the total number of joints and sliders in
//               the character.
////////////////////////////////////////////////////////////////////
INLINE int EggCharacterData::
get_num_components() const {
  return _components.size();
}

////////////////////////////////////////////////////////////////////
//     Function: EggCharacterData::get_component
//       Access: Public
//  Description: Returns the nth joint or slider in the character.
//               This can be used to walk linearly through all joints
//               and sliders in the character when you don't care
//               about making a distinction between the two; it
//               returns the same objects that can also be discovered
//               via get_slider() and get_root_joint().
////////////////////////////////////////////////////////////////////
INLINE EggComponentData *EggCharacterData::
get_component(int n) const {
  nassertr(n >= 0 && n < (int)_components.size(), NULL);
  return _components[n];
}
