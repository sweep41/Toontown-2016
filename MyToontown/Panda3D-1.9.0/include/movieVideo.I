// Filename: movieVideo.I
// Created by: jyelon (02Jul07)
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
//     Function: MovieVideo::get_filename
//       Access: Published
//  Description: Returns the movie's filename.  A movie is not
//               guaranteed to have a filename, if not, then this
//               function returns an empty filename.
////////////////////////////////////////////////////////////////////
INLINE const Filename &MovieVideo::
get_filename() const {
  return _filename;
}

////////////////////////////////////////////////////////////////////
//     Function: MovieVideo::get_subfile_info
//       Access: Published
//  Description: If the movie is to be loaded from a subfile on disk,
//               this returns the subfile info.  Check info.is_empty()
//               to see if this is valid data.
////////////////////////////////////////////////////////////////////
INLINE const SubfileInfo &MovieVideo::
get_subfile_info() const {
  return _subfile_info;
}
