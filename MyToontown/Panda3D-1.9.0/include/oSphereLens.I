// Filename: oSphereLens.I
// Created by:  drose (25Feb11)
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
//     Function: OSphereLens::Constructor
//       Access: Public
//  Description:
////////////////////////////////////////////////////////////////////
INLINE OSphereLens::
OSphereLens() {
}

////////////////////////////////////////////////////////////////////
//     Function: OSphereLens::Copy Constructor
//       Access: Public
//  Description:
////////////////////////////////////////////////////////////////////
INLINE OSphereLens::
OSphereLens(const OSphereLens &copy) : Lens(copy) {
}

////////////////////////////////////////////////////////////////////
//     Function: OSphereLens::Copy Assignment Operator
//       Access: Public
//  Description:
////////////////////////////////////////////////////////////////////
INLINE void OSphereLens::
operator = (const OSphereLens &copy) {
  Lens::operator = (copy);
}

