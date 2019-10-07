from atomicrex.ase_calculator import Atomicrex
from ase.lattice.cubic import BodyCenteredCubic

__doc__ = """ This script demonstrates the usage of the Atomicrex ase
calculator.  """


atoms = BodyCenteredCubic(size=(2, 2, 2), symbol='Fe', latticeconstant=2.86)
calc = Atomicrex(file_name="main.xml")

atoms.set_calculator(calc)

f = atoms.get_forces()
print("Forces: {}".format(f))

e = atoms.get_potential_energy()
print("Total energy: {}".format(e))

p = atoms.get_stress()
print("Stress: {}".format(p))