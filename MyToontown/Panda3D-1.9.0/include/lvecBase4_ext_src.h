// Filename: lvecBase4_ext_src.h
// Created by:  rdb (13Sep13)
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
//       Class : Extension<LVecBase4>
// Description : This class defines the extension methods for
//               LVecBase4, which are called instead of
//               any C++ methods with the same prototype.
////////////////////////////////////////////////////////////////////
template<>
class Extension<FLOATNAME(LVecBase4)> : public ExtensionBase<FLOATNAME(LVecBase4)> {
public:
  INLINE_LINMATH PyObject *__reduce__(PyObject *self) const;
  INLINE_LINMATH PyObject *__getattr__(const string &attr_name) const;
  INLINE_LINMATH int __setattr__(PyObject *self, const string &attr_name, PyObject *assign);
  INLINE_LINMATH void __setitem__(int i, FLOATTYPE v);
  INLINE_LINMATH void python_repr(ostream &out, const string &class_name) const;
};

////////////////////////////////////////////////////////////////////
//       Class : Extension<UnalignedLVecBase4>
// Description : This class defines the extension methods for
//               UnalignedLVecBase4, which are called instead of
//               any C++ methods with the same prototype.
////////////////////////////////////////////////////////////////////
template<>
class Extension<FLOATNAME(UnalignedLVecBase4)> : public ExtensionBase<FLOATNAME(UnalignedLVecBase4)> {
public:
  INLINE_LINMATH void __setitem__(int i, FLOATTYPE v);
};

#include "lvecBase4_ext_src.I"
