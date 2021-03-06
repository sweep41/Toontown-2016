// Filename: genericThread.I
// Created by:  drose (09Nov11)
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
//     Function: GenericThread::set_function
//       Access: Published
//  Description: Replaces the function that is called when the thread
//               runs.
////////////////////////////////////////////////////////////////////
INLINE void GenericThread::
set_function(GenericThread::ThreadFunc *function) {
  _function = function;
}

////////////////////////////////////////////////////////////////////
//     Function: GenericThread::get_function
//       Access: Published
//  Description: Returns the function that is called when the thread
//               runs.
////////////////////////////////////////////////////////////////////
INLINE GenericThread::ThreadFunc *GenericThread::
get_function() const {
  return _function;
}

////////////////////////////////////////////////////////////////////
//     Function: GenericThread::set_user_data
//       Access: Published
//  Description: Replaces the void pointer that is passed to the thread
//               function.  This is any arbitrary pointer; the thread
//               object does no processing on it.
////////////////////////////////////////////////////////////////////
INLINE void GenericThread::
set_user_data(void *user_data) {
  _user_data = user_data;
}

////////////////////////////////////////////////////////////////////
//     Function: GenericThread::get_user_data
//       Access: Published
//  Description: Returns the void pointer that is passed to the thread
//               function.
////////////////////////////////////////////////////////////////////
INLINE void *GenericThread::
get_user_data() const {
  return _user_data;
}
