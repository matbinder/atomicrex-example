from __future__ import print_function, division
import atomicrex

print('Create job object')
job = atomicrex.Job()

print('Parse XML input file with input parameters'
      ' and potential information.')
job.parse_input_file('main.xml')

print('Switch verbosity to "medium"')
job.set_verbosity(2)

print('Adding a structure from the library')
structure = job.add_library_structure('Al-fcc',
                                      'fcc',
                                      {'alat': 4.032, 'type': 'Al'})
structure.modify_property('atomic-energy', -3.36, 200.0)
structure.modify_property('bulk-modulus', 80.9, 0.1)
structure.modify_property('C11', 114.0, 100.0)
structure.modify_property('C12', 61.9)
structure.modify_property('C44', 31.6)
print('')

print('Testing some ASE like method calls')
print('.positions: ', structure.positions)
print('.get_positions: ', structure.get_positions())
print('.get_cell:')
print(structure.get_cell())
print('.get_number_of_atoms: ', structure.get_number_of_atoms())
print('')

print('Computing properties.')
structure.compute_properties()
print('')

print('Printing properties.')
structure.print_properties()
print('')

print('Adding another structure from the library')
structure = job.add_library_structure('Al-bcc',
                                      'body-centered cubic',
                                      {'alat': 4.032, 'type': 'Al'})
print('')

print('Demonstrating the conversion to an ASE atoms object.')
conf = structure.get_atoms(job)
print(' cell')
print(conf.cell)
print(' atoms')
for k, atom in enumerate(conf, start=1):
    print(' {:3}'.format(k))
    print(atom)
print('')

print('Adding more structures from the library')
structure = job.add_library_structure('my-simple-cubic',
                                      'sc',
                                      {'alat': 3.0, 'type': 'Al'})
print(' id: {} (nat = {})'.format(structure.id,
                                  structure.get_number_of_atoms()))
print(structure.cell)
structure = job.add_library_structure('my-diamond',
                                      'dia',
                                      {'alat': 1.0, 'type': 'Al'})
print(' id: {} (nat = {})'.format(structure.id,
                                  structure.get_number_of_atoms()))
print(structure.cell)
structure = job.add_library_structure('my-hcp',
                                      'hcp',
                                      {'alat': 2.5,
                                       'clat': 4.0,
                                       'type': 'Al'})
print(' id: {} (nat = {})'.format(structure.id,
                                  structure.get_number_of_atoms()))
print(structure.cell)
structure = job.add_library_structure('my-omega',
                                      'omega',
                                      {'alat': 2.5,
                                       'ca_ratio': 0.69,
                                       'type': 'Al'})
print(' id: {} (nat = {})'.format(structure.id,
                                  structure.get_number_of_atoms()))
print(structure.cell)
structure = job.add_library_structure('my-L10',
                                      'L10',
                                      {'alat': 2.5,
                                       'ca_ratio': 0.69,
                                       'type_A': 'Al',
                                       'type_B': 'Al'})
print(' id: {} (nat = {})'.format(structure.id,
                                  structure.get_number_of_atoms()))
print(structure.cell)
print('')
