""" Classes for Lattice and Acccelerator Nodes """

#---- Lattice library from file LatticeLib.py
from .LatticeLib import Lattice, BunchLattice, RF_Cavity, Sequence

#---- AccNodes from BunchAccNodes.py
from .BunchAccNodes import BunchAccNode
from .BunchAccNodes import MagnetNode
from .BunchAccNodes import MarkerNode, Drift, Quad, AbstractRF_Gap, Bend
from .BunchAccNodes import Solenoid
from .BunchAccNodes import DCorrectorH, DCorrectorV
from .BunchAccNodes import ThickKick

#---- Lattice functions from LatticeFunc.py
from .BunchLatticeFunc import GetGlobalQuadGradient
from .BunchLatticeFunc import GetGlobalQuadGradientDerivative
from .BunchLatticeFunc import GetGlobalRF_AxisField
from .BunchLatticeFunc import getNodeForNameFromWholeLattice
from .BunchLatticeFunc import getNodePosDictForWholeLattice
from .BunchLatticeFunc import getAllNodesInLattice
from .BunchLatticeFunc import getAllMagnetsInLattice

#---- Aperture nodes from BunchApertureNodes.py
from .BunchApertureNodes import BunchApertureNode
from .BunchApertureNodes import CircleBunchApertureNode
from .BunchApertureNodes import EllipseBunchApertureNode
from .BunchApertureNodes import RectangleBunchApertureNode
from .BunchApertureNodes import PhaseBunchApertureNode
from .BunchApertureNodes import EnergyBunchApertureNode

#---- Overlapping bunch tracking nodes from FieldOverlappingBunchNodes.py
from .FieldOverlappingBunchNodes import AxisField_and_Quad_RF_Gap
from .FieldOverlappingBunchNodes import OverlappingQuadsBunchNode

#---- RF gap bunch tracking nodes from BunchRfGapNodes.py
from .BunchRfGapNodes import BunchRF_Gap, AxisFieldRF_Gap, RF_AxisFieldsStore

#---- Transport matrix generators from TransportMatrixGenBunchNodes.py
from .TransportMatrixGenBunchNodes import TrMatrixGenBunchNode
from .TransportMatrixGenBunchNodes import TrMatricesController

from .LinacDiagnosticsNodes import LinacBPM

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
__all__.append("MagnetNode")
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

#---- Transport matrix generators from TransportMatrixGenBunchNodes.py
__all__.append("TrMatrixGenBunchNode")
__all__.append("TrMatricesController")

__all__.append("LinacBPM")