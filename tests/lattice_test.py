import sys
import math
import time

from orbit.lattice import AccLattice, AccNode, AccActionsContainer

# import the XmlDataAdaptor XML parser
from orbit.utils.xml import XmlDataAdaptor

from orbit.bunch_generators import TwissContainer
from orbit.bunch_generators import WaterBagDist3D, GaussDist3D, KVDist3D

from orbit.core.bunch import Bunch, BunchTwissAnalysis

#---- New Lattice
from bunch_lattice.lattice import BunchLattice
from bunch_lattice.parsers import SNS_BunchLatticeFactory


from sns_linac_bunch_generator import SNS_Linac_BunchGenerator

#==================================================
#    START of Test SCRIPT
#==================================================

lattice = BunchLattice("test_lattice")

xml_lattice_file_name = "sns_pup_linac.xml"

seq_names = ["MEBT","DTL1","DTL2","DTL3","DTL4","DTL5","DTL6"]
seq_names = ["MEBT", "DTL1", "DTL2", "DTL3", "DTL4", "DTL5", "DTL6", "CCL1", "CCL2", "CCL3", "CCL4", "SCLMed", "SCLHigh", "HEBT1", "HEBT2"]

acc_da = XmlDataAdaptor.adaptorForFile(xml_lattice_file_name)

bunch_lattice_factory = SNS_BunchLatticeFactory()

accLattice = bunch_lattice_factory.getAccLatticeFromDA(seq_names,acc_da)

# -----TWISS Parameters at the entrance of MEBT ---------------
# transverse emittances are unnormalized and in pi*mm*mrad
# longitudinal emittance is in pi*eV*sec
e_kin_ini = 0.0025  # in [GeV]
mass = 0.939294  # in [GeV]
gamma = (mass + e_kin_ini) / mass
beta = math.sqrt(gamma * gamma - 1.0) / gamma
print("relat. gamma=", gamma)
print("relat.  beta=", beta)
frequency = 402.5e6
v_light = 2.99792458e8  # in [m/sec]

# ------ emittances are normalized - transverse by gamma*beta and long. by gamma**3*beta
(alphaX, betaX, emittX) = (-1.9620, 0.1831, 0.21)
(alphaY, betaY, emittY) = (1.7681, 0.1620, 0.21)
(alphaZ, betaZ, emittZ) = (0.0196, 0.5844, 0.24153)

alphaZ = -alphaZ

# ---make emittances un-normalized XAL units [m*rad]
emittX = 1.0e-6 * emittX / (gamma * beta)
emittY = 1.0e-6 * emittY / (gamma * beta)
emittZ = 1.0e-6 * emittZ / (gamma**3 * beta)
print(" ========= XAL Twiss ===========")
print(" aplha beta emitt[mm*mrad] X= %6.4f %6.4f %6.4f " % (alphaX, betaX, emittX * 1.0e6))
print(" aplha beta emitt[mm*mrad] Y= %6.4f %6.4f %6.4f " % (alphaY, betaY, emittY * 1.0e6))
print(" aplha beta emitt[mm*mrad] Z= %6.4f %6.4f %6.4f " % (alphaZ, betaZ, emittZ * 1.0e6))

# ---- long. size in mm
sizeZ = math.sqrt(emittZ * betaZ) * 1.0e3

# ---- transform to pyORBIT emittance[GeV*m]
emittZ = emittZ * gamma**3 * beta**2 * mass
betaZ = betaZ / (gamma**3 * beta**2 * mass)

print(" ========= PyORBIT Twiss ===========")
print(" aplha beta emitt[mm*mrad] X= %6.4f %6.4f %6.4f " % (alphaX, betaX, emittX * 1.0e6))
print(" aplha beta emitt[mm*mrad] Y= %6.4f %6.4f %6.4f " % (alphaY, betaY, emittY * 1.0e6))
print(" aplha beta emitt[mm*MeV] Z= %6.4f %6.4f %6.4f " % (alphaZ, betaZ, emittZ * 1.0e6))

twissX = TwissContainer(alphaX, betaX, emittX)
twissY = TwissContainer(alphaY, betaY, emittY)
twissZ = TwissContainer(alphaZ, betaZ, emittZ)

print("Start Bunch Generation.")
bunch_gen = SNS_Linac_BunchGenerator(twissX, twissY, twissZ)

# set the initial kinetic energy in GeV
bunch_gen.setKinEnergy(e_kin_ini)

# set the beam peak current in mA
bunch_gen.setBeamCurrent(38.0)

bunch_in = bunch_gen.getBunch(nParticles=1000, distributorClass=WaterBagDist3D)
# bunch_in = bunch_gen.getBunch(nParticles = 100000, distributorClass = GaussDist3D)
# bunch_in = bunch_gen.getBunch(nParticles = 10000, distributorClass = KVDist3D)

print("Bunch Generation completed.")

# set up design
accLattice.trackDesignBunch(bunch_in)

print("Design tracking completed.")

# track through the lattice
paramsDict = {"old_pos": -1.0, "count": 0, "pos_step": 0.1}
actionContainer = AccActionsContainer("Test Design Bunch Tracking")

pos_start = 0.0

twiss_analysis = BunchTwissAnalysis()

#file_out = open("pyorbit_twiss_sizes_ekin.dat", "w")
file_out = open("pyorbit_twiss_sizes_ekin_pup.dat", "w")

s = " Node   position "
s += "   alphaX betaX emittX  normEmittX"
s += "   alphaY betaY emittY  normEmittY"
s += "   alphaZ betaZ emittZ  emittZphiMeV"
s += "   sizeX sizeY sizeZ_deg"
s += "   eKin Nparts "
file_out.write(s + "\n")
print(" N node   position    sizeX  sizeY  sizeZdeg  eKin Nparts ")


def action_entrance(paramsDict):
    node = paramsDict["node"]
    bunch = paramsDict["bunch"]
    pos = paramsDict["path_length"]
    if paramsDict["old_pos"] == pos:
        return
    if paramsDict["old_pos"] + paramsDict["pos_step"] > pos:
        return
    paramsDict["old_pos"] = pos
    paramsDict["count"] += 1
    gamma = bunch.getSyncParticle().gamma()
    beta = bunch.getSyncParticle().beta()
    twiss_analysis.analyzeBunch(bunch)
    x_rms = math.sqrt(twiss_analysis.getTwiss(0)[1] * twiss_analysis.getTwiss(0)[3]) * 1000.0
    y_rms = math.sqrt(twiss_analysis.getTwiss(1)[1] * twiss_analysis.getTwiss(1)[3]) * 1000.0
    z_rms = math.sqrt(twiss_analysis.getTwiss(2)[1] * twiss_analysis.getTwiss(2)[3]) * 1000.0
    z_to_phase_coeff = bunch_gen.getZtoPhaseCoeff(bunch)
    z_rms_deg = z_to_phase_coeff * z_rms / 1000.0
    nParts = bunch.getSizeGlobal()
    (alphaX, betaX, emittX) = (twiss_analysis.getTwiss(0)[0], twiss_analysis.getTwiss(0)[1], twiss_analysis.getTwiss(0)[3] * 1.0e6)
    (alphaY, betaY, emittY) = (twiss_analysis.getTwiss(1)[0], twiss_analysis.getTwiss(1)[1], twiss_analysis.getTwiss(1)[3] * 1.0e6)
    (alphaZ, betaZ, emittZ) = (twiss_analysis.getTwiss(2)[0], twiss_analysis.getTwiss(2)[1], twiss_analysis.getTwiss(2)[3] * 1.0e6)
    norm_emittX = emittX * gamma * beta
    norm_emittY = emittY * gamma * beta
    # ---- phi_de_emittZ will be in [pi*deg*MeV]
    phi_de_emittZ = z_to_phase_coeff * emittZ
    eKin = bunch.getSyncParticle().kinEnergy() * 1.0e3
    s = " %45s  %4.5f " % (node.getName(), pos + pos_start)
    s += "   %6.4f  %6.4f  %6.4f  %6.4f   " % (alphaX, betaX, emittX, norm_emittX)
    s += "   %6.4f  %6.4f  %6.4f  %6.4f   " % (alphaY, betaY, emittY, norm_emittY)
    s += "   %6.4f  %6.4f  %6.4f  %6.4f   " % (alphaZ, betaZ, emittZ, phi_de_emittZ)
    s += "   %5.3f  %5.3f  %5.3f " % (x_rms, y_rms, z_rms_deg)
    s += "  %10.6f   %8d " % (eKin, nParts)
    file_out.write(s + "\n")
    file_out.flush()
    s_prt = " %5d  %35s  %4.5f " % (paramsDict["count"], node.getName(), pos + pos_start)
    s_prt += "  %5.3f  %5.3f   %5.3f " % (x_rms, y_rms, z_rms_deg)
    s_prt += "  %10.4f   %8d " % (eKin, nParts)
    print(s_prt)


def action_exit(paramsDict):
    action_entrance(paramsDict)


actionContainer.addAction(action_entrance, AccActionsContainer.ENTRANCE)
actionContainer.addAction(action_exit, AccActionsContainer.EXIT)

time_start = time.process_time()

accLattice.trackBunch(bunch_in, paramsDict=paramsDict, actionContainer=actionContainer)

time_exec = time.process_time() - time_start
print("time[sec]=", time_exec)

file_out.close()

print ("Stop.")
sys.exit(0)


elem1 = AccNode("el-1")
elem2 = AccNode("el-2")
elem3 = AccNode("el-3")

elem1.setLength(1.1)
elem2.setLength(2.1)
elem3.setLength(3.1)

lattice.addNode(elem1)
lattice.addNode(elem2)
lattice.addNode(elem3)

elem1_1 = AccNode("el-1-1")
elem1_1.setnParts(2)
elem1_1_1 = AccNode("el-1-1-1")
elem1_1_2 = AccNode("el-1-1-2")
elem1_1_3 = AccNode("el-1-1-3")
elem1_1_4 = AccNode("el-1-1-4")

elem1.addChildNode(elem1_1, AccNode.ENTRANCE)
elem1_1.addChildNode(elem1_1_1, AccNode.ENTRANCE)
elem1_1.addChildNode(elem1_1_2, AccNode.BODY, 0)
elem1_1.addChildNode(elem1_1_3, AccNode.BODY, 1)
elem1_1.addChildNode(elem1_1_4, AccNode.EXIT)


elem1_2 = AccNode("el-1-2")
elem2.addChildNode(elem1_2, AccNode.EXIT)

acts = AccActionsContainer()


def Blanks(n):
    s = ""
    for i in range(n):
        s += " "
    return s


nLevel = [0]
nElems = [0]


def funcEntrance(paramsDict):
    nLevel[0] += 1
    node = paramsDict["node"]
    if "print" in paramsDict and paramsDict["print"] == True:
        print(Blanks(nLevel[0]), "ENTER level=", nLevel[0], " node=", node.getName())
        nElems[0] += 1


def funcExit(paramsDict):
    node = paramsDict["node"]
    if "print" in paramsDict and paramsDict["print"] == True:
        print(Blanks(nLevel[0]), "EXIT  level=", nLevel[0], " node=", node.getName())
    nLevel[0] -= 1


def funcTrack(paramsDict):
    node = paramsDict["node"]
    if "print" in paramsDict and paramsDict["print"] == True:
        print(Blanks(nLevel[0]), "BODY TRACK through node =", node.getName(), " level=", nLevel[0])


acts.addAction(funcEntrance, AccActionsContainer.ENTRANCE)
acts.addAction(funcTrack, AccActionsContainer.BODY)
acts.addAction(funcExit, AccActionsContainer.EXIT)

lattice.initialize()

print("Total length=", lattice.getLength())

nodes = lattice.getNodes()
for node in nodes:
    print("node=", node.getName(), " s start,stop = %4.3f %4.3f " % lattice.getNodePositionsDict()[node])


d = {"print": True}

lattice.trackActions(acts, d)

print("Total number of nodes=", nElems[0])
# ========Speed test==========================
count = 1
while count < 100000:
    # lattice.initialize()
    lattice.trackActions(acts)
    if count % 10000 == 0:
        print("i=", count, " time= %9.8f " % (posix.times()[0] / count))
    count += 1

print("====STOP===")

sys.exit(0)
