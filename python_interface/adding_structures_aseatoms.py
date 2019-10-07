from __future__ import print_function, division
import atomicrex
from ase.io import read
from numpy.random import rand

print('Create job object.')
job = atomicrex.Job()

print('Parse XML input file with input parameters'
      ' and potential information.')
job.parse_input_file('main.xml')

print('Switch verbosity to "medium".')
job.set_verbosity(2)

print('Adding a user-defined structure')
conf = read('aluminum_cell_with_forces.traj')
structure = job.add_ase_structure("Al-ase", conf)
structure.compute_energy(compute_forces=True)
print('Potential energy: {}'.format(structure.get_potential_energy()))
print('Forces:')
for i, force in enumerate(structure.get_forces(), start=1):
    print('{:3}'.format(i), end='')
    print((3*' {:10.6f}').format(*force))
print('')

print('Forces:')
for i, force in enumerate(structure.get_forces(), start=1):
    print('{:3}'.format(i), end='')
    print((3*' {:10.6f}').format(*force))
print('')

print('Testing some ASE like method calls and properties')
structure = job.structures['Al-ase']
print(' positions')
print(structure.positions)
print(' get_positions()')
print(structure.get_positions())
print(' get_forces()')
print(structure.get_forces())
print(' get_cell()')
print(structure.get_cell())
print(' get_number_of_atoms()')
print(structure.get_number_of_atoms())

print('Handling target forces')
n = structure.get_number_of_atoms()
target_forces = rand(n, 3)
structure.set_target_forces(target_forces)
print('target_forces (1): {}'.format(structure.target_forces[:3]))
print('target_forces (2): {}'.format(structure.get_target_forces()[:3]))
