"""
This module is a vacuum window node in the linac or transport line
"""

import os
import math

# import the auxiliary classes
from orbit.utils import orbitFinalize, NamedObject, ParamsDictObject

# import general accelerator elements and lattice
from orbit.lattice import AccNode, AccActionsContainer, AccNodeBunchTracker

# import linac base node
from orbit.py_linac.lattice import BaseLinacNode

# import Collimator class from C++ code
# /src/orbit/MaterialInteractions/Collimator.cc
from orbit.core.collimator import Collimator

"""
//-------------------------------------------------------------------------
// C++ class Collimator has the following parameters:
//
// PARAMETERS
//   length: length in m
//   ma:	 material number. (0=carbon, 1=aluminum, 2=iron, 3=copper, 4=tantalum, 5=tungstun,
//           6=platinum, 7=lead, ma>=8 = black absorber)
//   densityfac: density factor (for materials mixed with air or water). 1.0 for pure.
//   shape:  shape of the collimator: 1=circle, 2=ellipse, 3=one sided
//           flat, 4=two sided flat, 5=rectangular (outside is collimator),
//           6=rectangular (inside is collimator).
//   a:      depending on shape, either (shape = 1) radius,
//           (shape = 2) semimajor axis, (shape = 3) distance to
//           flat edge, (shape = 4) minimum edge, (shape=5 or 6)
//           minimum horizontal edge.
//   b:      depending on shape, either (1) radius, (2) semimajor axis,
//           (3) zero  (4) maximum edge (5) (shape=5 or 6) maximum
//           horizontal edge.
//   c:      minimum vertical edge (used only in shapes 5 or 6)
//   d:      maximum vertical edge (used only in shapes 5 or 6)
//   angle:  tilt angle of collimator.
//--------------------------------------------------------------------------
"""


class VacuumWindowNode(BaseLinacNode):
    """
    The vacuum window node class for linac lattice
    """

    def __init__(self, length, ma, density_fac=1.0, name="vacuum_window", pos=0.0):
        """
        Constructor. Creates the vacuum window element.
        """
        BaseLinacNode.__init__(self, name)
        # ---- material
        self.ma = int(ma)
        self.materials_arr = ["carbon", "aluminum", "iron", "copper", "tantalum", "tungstun"]
        self.materials_arr += ["platinum", "lead", "black absorber"]
        # ---- by default the shape is circle
        shape = 1
        # ---- by default the radius is 0 m
        # ---- It means no particles will escape the collimator! See Collimator.cc
        radius = 0.0
        a = radius
        b = a
        # ----
        c = 1.0
        d = 1.0
        angle = 0.0
        # ----
        self.density_fac = density_fac
        self.collimator = Collimator(length, self.ma, density_fac, shape, a, b, c, d, angle, pos)
        self.setType("vacuum_window")
        self.setLength(length)
        self.setPosition(pos)

    def getMaterial(self):
        """
        Returns the material
        """
        if self.ma >= 0 and self.ma <= 8:
            return self.materials_arr[self.ma]
        return self.materials_arr[len(self.materials_arr) - 1]

    def getDensityfactor(self):
        """
        Returns density factor of the window material.
        """
        return self.density_fac

    def trackDesign(self, paramsDict):
        """
        For the design tracking it will do nothing.
        """
        pass

    def track(self, paramsDict):
        """
        The vacuum window class implementation of the AccNodeBunchTracker class track(paramsDict) method.
        """
        length = self.getLength(self.getActivePartIndex())
        if length <= 0.0:
            return
        bunch = paramsDict["bunch"]
        if "lostbunch" in paramsDict:
            lostbunch = paramsDict["lostbunch"]
            self.collimator.collimateBunch(bunch, lostbunch)
        else:
            self.collimator.collimateBunch(bunch)

    def setPosition(self, pos):
        """
        Sets the position of the vacuum window to put this info
        into the lost particles bunch for each lost particle.
        """
        BaseLinacNode.setPosition(self, pos)
        self.collimator.setPosition(pos)
