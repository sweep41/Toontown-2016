// Filename: virtualFileComposite.I
// Created by:  drose (03Aug02)
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
//     Function: VirtualFileComposite::Constructor
//       Access: Public
//  Description: 
////////////////////////////////////////////////////////////////////
INLINE VirtualFileComposite::
VirtualFileComposite(VirtualFileSystem *file_system, const Filename &filename) :
  _file_system(file_system),
  _filename(filename)
{
}

////////////////////////////////////////////////////////////////////
//     Function: VirtualFileComposite::add_component
//       Access: Public
//  Description: Adds one more component to the composite directory.
//                The component should be a directory and the file
//                system and filename should match the composite.
////////////////////////////////////////////////////////////////////
INLINE void VirtualFileComposite::
add_component(VirtualFile *file) {
  nassertv(file->is_directory());
  nassertv(file->get_file_system() == _file_system);
  nassertv(file->get_filename() == _filename);
  
  _components.push_back(file);
}
