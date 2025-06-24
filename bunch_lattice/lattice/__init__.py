## \brief The base classes of PyORBIT lattice structure.
##
## Classes:
## - Lattice       - Class. The general lattice.
## - BunchAccNodes         - Module. Collection of the accelerator nodes for bunch tracking: drifts, quads, RF gaps etc..
## - BunchRfGapNodes       - Module. Collection of RF Gap models for bunch tracking

#---- Lattice library from file LatticeLib.py
from bunch_lattice.lattice.LatticeLib import Lattice, BunchLattice, RF_Cavity, Sequence

#---- AccNodes from BunchAccNodes.py
from bunch_lattice.lattice.BunchAccNodes import BunchAccNode
from bunch_lattice.lattice.BunchAccNodes import MarkerNode, Drift, Quad, AbstractRF_Gap, Bend
from bunch_lattice.lattice.BunchAccNodes import Solenoid
from bunch_lattice.lattice.BunchAccNodes import DCorrectorH, DCorrectorV
from bunch_lattice.lattice.BunchAccNodes import ThickKick

#---- Lattice functions from LatticeFunc.py
from bunch_lattice.lattice.BunchLatticeFunc import GetGlobalQuadGradient
from bunch_lattice.lattice.BunchLatticeFunc import GetGlobalQuadGradientDerivative
from bunch_lattice.lattice.BunchLatticeFunc import GetGlobalRF_AxisField
from bunch_lattice.lattice.BunchLatticeFunc import getNodeForNameFromWholeLattice
from bunch_lattice.lattice.BunchLatticeFunc import getNodePosDictForWholeLattice
from bunch_lattice.lattice.BunchLatticeFunc import getAllNodesInLattice
from bunch_lattice.lattice.BunchLatticeFunc import getAllMagnetsInLattice

#---- Aperture nodes from BunchApertureNodes.py
from bunch_lattice.lattice.BunchApertureNodes import BunchApertureNode
from bunch_lattice.lattice.BunchApertureNodes import CircleBunchApertureNode
from bunch_lattice.lattice.BunchApertureNodes import EllipseBunchApertureNode
from bunch_lattice.lattice.BunchApertureNodes import RectangleBunchApertureNode
from bunch_lattice.lattice.BunchApertureNodes import PhaseBunchApertureNode
from bunch_lattice.lattice.BunchApertureNodes import EnergyBunchApertureNode

#---- Overlapping bunch tracking nodes from FieldOverlappingBunchNodes.py
from bunch_lattice.lattice.FieldOverlappingBunchNodes import AxisField_and_Quad_RF_Gap
from bunch_lattice.lattice.FieldOverlappingBunchNodes import OverlappingQuadsBunchNode

#---- RF gap bunch tracking nodes from BunchRfGapNodes.py
from bunch_lattice.lattice.BunchRfGapNodes import BunchRF_Gap, AxisFieldRF_Gap, RF_AxisFieldsStore

"""
from orbit.py_linac.lattice.LinacTransportMatrixGenNodes import LinacTrMatrixGenNode
from orbit.py_linac.lattice.LinacTransportMatrixGenNodes import LinacTrMatricesController

from orbit.py_linac.lattice.LinacDiagnosticsNodes import LinacBPM
"""

__all__ = []

#---- Lattice library from file LatticeLib.py
__all__.append("Lattice")
__all__.append("BunchLattice")
__all__.append("RF_Cavity")
__all__.append("Sequence")

#---- AccNodes from BunchAccNodes.py
__all__.append("BunchAccNode")
__all__.append("MarkerNode")
__all__.append("Drift")
__all__.append("Quad")
__all__.append("AbstractRF_Gap")
__all__.append("Bend")
__all__.append("Solenoid")
__all__.append("DCorrectorH")
__all__.append("DCorrectorV")
__all__.append("ThickKick")

#---- Lattice functions from LatticeFunc.py
__all__.append("GetGlobalQuadGradient")
__all__.append("GetGlobalQuadGradientDerivative")
__all__.append("GetGlobalRF_AxisField")
__all__.append("getNodeForNameFromWholeLattice")
__all__.append("getNodePosDictForWholeLattice")
__all__.append("getAllNodesInLattice")
__all__.append("getAllMagnetsInLattice")

#---- Aperture bunch tracking nodes from BunchApertureNodes.py
__all__.append("BunchApertureNode")
__all__.append("CircleBunchApertureNode")
__all__.append("EllipseBunchApertureNode")
__all__.append("RectangleBunchApertureNode")
__all__.append("PhaseBunchApertureNode")
__all__.append("EnergyBunchApertureNode")

#---- Overlapping bunch tracking nodes from FieldOverlappingBunchNodes.py
__all__.append("AxisField_and_Quad_RF_Gap")
__all__.append("OverlappingQuadsBunchNode")

#---- RF gap and auxilary classes from BunchRfGapNodes.py
__all__.append("BunchRF_Gap")
__all__.append("AxisFieldRF_Gap")
__all__.append("RF_AxisFieldsStore")

"""
__all__.append("LinacTrMatrixGenNode")
__all__.append("LinacTrMatricesController")

__all__.append("LinacBPM")
"""