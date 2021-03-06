// Filename: geomParticleRenderer.I
// Created by:  charles (05Jul00)
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
//  Function : set_geom_node
//    Access : public
////////////////////////////////////////////////////////////////////

// we're forcing a pool resize to remove every node in the vector.
// this is because nodes are reference-counted, and we have to
// explicitly remove them from the node they were previously parented
// to.

INLINE void GeomParticleRenderer::
set_geom_node(PandaNode *node) {
  nassertv(node != (PandaNode *)NULL);
  _geom_node = node;
  resize_pool(_pool_size);
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::set_x_scale_flag
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE void GeomParticleRenderer::
set_x_scale_flag(bool animate_x_ratio) {
  _animate_x_ratio = animate_x_ratio;
  init_geoms();
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::set_y_scale_flag
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE void GeomParticleRenderer::
set_y_scale_flag(bool animate_y_ratio) {
  _animate_y_ratio = animate_y_ratio;
  init_geoms();
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::set_z_scale_flag
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE void GeomParticleRenderer::
set_z_scale_flag(bool animate_z_ratio) {
  _animate_z_ratio = animate_z_ratio;
  init_geoms();
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::set_initial_x_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE void GeomParticleRenderer::
set_initial_x_scale(PN_stdfloat initial_x_scale) {
  _initial_x_scale = initial_x_scale;
  init_geoms();
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::set_final_x_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE void GeomParticleRenderer::
set_final_x_scale(PN_stdfloat final_x_scale) {
  _final_x_scale = final_x_scale;
  init_geoms();
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::set_initial_y_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE void GeomParticleRenderer::
set_initial_y_scale(PN_stdfloat initial_y_scale) {
  _initial_y_scale = initial_y_scale;
  init_geoms();
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::set_final_y_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE void GeomParticleRenderer::
set_final_y_scale(PN_stdfloat final_y_scale) {
  _final_y_scale = final_y_scale;
  init_geoms();
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::set_initial_z_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE void GeomParticleRenderer::
set_initial_z_scale(PN_stdfloat initial_z_scale) {
  _initial_z_scale = initial_z_scale;
  init_geoms();
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::set_final_z_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE void GeomParticleRenderer::
set_final_z_scale(PN_stdfloat final_z_scale) {
  _final_z_scale = final_z_scale;
  init_geoms();
}

////////////////////////////////////////////////////////////////////
//  Function : get_geom_node
//    Access : public
////////////////////////////////////////////////////////////////////
INLINE PandaNode *GeomParticleRenderer::
get_geom_node() {
  return _geom_node;
}

////////////////////////////////////////////////////////////////////
//  Function : get_color_interpolation_manager
//    Access : public
////////////////////////////////////////////////////////////////////
INLINE ColorInterpolationManager* GeomParticleRenderer::
get_color_interpolation_manager() const {
  return _color_interpolation_manager;
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::get_x_scale_flag
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE bool GeomParticleRenderer::
get_x_scale_flag() const {
  return _animate_x_ratio;
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::get_y_scale_flag
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE bool GeomParticleRenderer::
get_y_scale_flag() const {
  return _animate_y_ratio;
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::get_z_scale_flag
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE bool GeomParticleRenderer::
get_z_scale_flag() const {
  return _animate_z_ratio;
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::get_initial_x_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE PN_stdfloat GeomParticleRenderer::
get_initial_x_scale() const {
  return _initial_x_scale;
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::get_final_x_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE PN_stdfloat GeomParticleRenderer::
get_final_x_scale() const {
  return _final_x_scale;
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::get_initial_y_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE PN_stdfloat GeomParticleRenderer::
get_initial_y_scale() const {
  return _initial_y_scale;
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::get_final_y_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE PN_stdfloat GeomParticleRenderer::
get_final_y_scale() const {
  return _final_y_scale;
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::get_initial_z_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE PN_stdfloat GeomParticleRenderer::
get_initial_z_scale() const {
  return _initial_z_scale;
}

////////////////////////////////////////////////////////////////////
// Function : GeomParticleRenderer::get_final_z_scale
//   Access : public
////////////////////////////////////////////////////////////////////
INLINE PN_stdfloat GeomParticleRenderer::
get_final_z_scale() const {
  return _final_z_scale;
}
