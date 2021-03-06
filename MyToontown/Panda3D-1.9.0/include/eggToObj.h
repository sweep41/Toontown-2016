// Filename: eggToObj.h
// Created by:  drose (25Feb12)
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

#ifndef EGGTOOBJ_H
#define EGGTOOBJ_H

#include "pandatoolbase.h"
#include "eggToSomething.h"
#include "eggToObjConverter.h"

////////////////////////////////////////////////////////////////////
//       Class : EggToObj
// Description :
////////////////////////////////////////////////////////////////////
class EggToObj : public EggToSomething {
public:
  EggToObj();

  void run();

protected:
  virtual bool handle_args(Args &args);

private:
  bool _triangulate_polygons;
};

#endif
