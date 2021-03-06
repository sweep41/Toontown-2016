// Filename: identityStream.I
// Created by:  drose (09Oct02)
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
//     Function: IIdentityStream::Constructor
//       Access: Public
//  Description:
////////////////////////////////////////////////////////////////////
INLINE IIdentityStream::
IIdentityStream() : ISocketStream(&_buf) {
}

////////////////////////////////////////////////////////////////////
//     Function: IIdentityStream::Constructor
//       Access: Public
//  Description:
////////////////////////////////////////////////////////////////////
INLINE IIdentityStream::
IIdentityStream(BioStreamPtr *source, HTTPChannel *doc,
                bool has_content_length, size_t content_length) : 
  ISocketStream(&_buf) 
{
  open(source, doc, has_content_length, content_length);
}

////////////////////////////////////////////////////////////////////
//     Function: IIdentityStream::open
//       Access: Public
//  Description: 
////////////////////////////////////////////////////////////////////
INLINE IIdentityStream &IIdentityStream::
open(BioStreamPtr *source, HTTPChannel *doc, 
     bool has_content_length, size_t content_length) {
  clear((ios_iostate)0);
  _buf.open_read(source, doc, has_content_length, content_length);
  return *this;
}
