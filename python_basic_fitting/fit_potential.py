import atomicrex
from scipy.optimize import minimize
import argparse

__doc__ = """ This script demonstrates the application of the python interface
for parameter optimization.  """

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('mode', choices=['atomicrex', 'scipy'],
                    help='Use either the internal or a scipy optimizer.')
args = parser.parse_args()

# initialize job
job = atomicrex.Job()
job.parse_input_file('main.xml')
job.set_verbosity(2)

# fitting
job.prepare_fitting()
print('initial residual: %g' % job.calculate_residual())
if args.mode == 'atomicrex':
    job.perform_fitting()
elif args.mode == 'scipy':
    pass
    initial_params = job.get_potential_parameters()
    resopt = minimize(job.calculate_residual,
                      initial_params,
                      options={'disp': False,
                               'eps': 1e-4,
                               'gtol': 1e-10},
                      method='L-BFGS-B')
residual = job.calculate_residual()
print('final residual: %g' % job.calculate_residual())

# output properties
for name, structure in sorted(job.structures.items()):
    print('')
    print(' Structure: %s' % name)
    structure.compute_properties()
    structure.print_properties()

# parameters
job.print_potential_parameters()
