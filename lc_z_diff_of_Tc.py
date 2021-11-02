import argparse

parser = argparse.ArgumentParser(description='Check the difference between Tc in tc and j mode.'
                                             'Directory tree is assumed as:\n'
                                             'lattice_const/atomic_number/(scf_dir)/tc or j')

phelp = 'start lattice constant'
parser.add_argument('lattice_cconst_start', type=float, help=phelp)

phelp = 'end lattice constant '
parser.add_argument('lattice_const_end', type=float, help=phelp)

phelp = 'division number (number of the directories) of lattice constant'
parser.add_argument('division_num_lattice_const', type=int, help=phelp)

phelp = 'start atomic number'
parser.add_argument('atomic_num_start', type=float, help=phelp)

phelp = 'end atomic number'
parser.add_argument('atomic_num_end', type=float, help=phelp)

phelp = 'division number (number of the directories) of atomic number'
parser.add_argument('division_num_atomic_num', type=int, help=phelp)

phelp = 'output file name'
parser.add_argument('output_file', help=phelp)

args = parser.parse_args()
