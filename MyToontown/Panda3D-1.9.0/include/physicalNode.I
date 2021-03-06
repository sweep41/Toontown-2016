// Filename: physicalNode.I
// Created by:  charles (01Aug00)
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
//  Function : clear
//    Access : public
////////////////////////////////////////////////////////////////////
INLINE void PhysicalNode::
clear() {
  _physicals.erase(_physicals.begin(), _physicals.end());
}

////////////////////////////////////////////////////////////////////
//  Function : get_physical
//    Access : public
////////////////////////////////////////////////////////////////////
INLINE Physical *PhysicalNode::
get_physical(int index) const {
  nassertr(index >= 0 && index < (int)_physicals.size(),
           (Physical *) NULL);
  return _physicals[index];
}

////////////////////////////////////////////////////////////////////
//  Function : get_num_physicals
//    Access : public
////////////////////////////////////////////////////////////////////
INLINE int PhysicalNode::
get_num_physicals() const {
  return _physicals.size();
}

////////////////////////////////////////////////////////////////////
//  Function : add_physical
//    Access : public
////////////////////////////////////////////////////////////////////
INLINE void PhysicalNode::
add_physical(Physical *physical) {
  _physicals.push_back(physical);
  physical->_physical_node = this;
}
