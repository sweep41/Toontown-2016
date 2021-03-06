// Filename: bulletDebugNode.I
// Created by:  enn0x (23Jan10)
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
//     Function: BulletDebugNode::Destructor
//       Access: Published
//  Description:
////////////////////////////////////////////////////////////////////
INLINE BulletDebugNode::
~BulletDebugNode() {

}

////////////////////////////////////////////////////////////////////
//     Function: BulletDebugNode::show_wireframe
//       Access: Published
//  Description: 
////////////////////////////////////////////////////////////////////
INLINE void BulletDebugNode::
show_wireframe(bool show) {

  _wireframe = show;
  draw_mask_changed();
}

////////////////////////////////////////////////////////////////////
//     Function: BulletDebugNode::show_constraints
//       Access: Published
//  Description: 
////////////////////////////////////////////////////////////////////
INLINE void BulletDebugNode::
show_constraints(bool show) {

  _constraints = show;
  draw_mask_changed();
}

////////////////////////////////////////////////////////////////////
//     Function: BulletDebugNode::show_bounding_boxes
//       Access: Published
//  Description: 
////////////////////////////////////////////////////////////////////
INLINE void BulletDebugNode::
show_bounding_boxes(bool show) {

  _bounds = show;
  draw_mask_changed();
}

////////////////////////////////////////////////////////////////////
//     Function: BulletDebugNode::show_normals
//       Access: Published
//  Description: 
////////////////////////////////////////////////////////////////////
INLINE void BulletDebugNode::
show_normals(bool show) {

  _drawer._normals = show;
}

