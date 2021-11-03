"""
WARNING: This script needs python3.9.
"""
import argparse
import glob
import os
import get_diff_tc

parser = argparse.ArgumentParser(description='Check the difference between Tc in tc and j mode.'
                                             'Directory tree is assumed as:\n'
                                             'lattice_const/atomic_number/(scf_dir)/tc or j')
phelp = 'output file name'
parser.add_argument('output_file', help=phelp)

phelp = 'error criterion. default is 0.05.'
parser.add_argument('-ec', '--error_criterion', type=float, default=0.05, help=phelp)

args = parser.parse_args()

# get the path of all tc/ directory
dir_list = glob.glob('**/tc/', recursive=True)

# remove "tc/" part in the directory names
try:
    dir_list.remove('tc/')
except ValueError:
    pass
for i, dir_list_element in enumerate(dir_list):
    dir_list[i] = dir_list_element.removesuffix('tc/')

# check Tc in each directories
dir_name_tc = "/tc"
dir_name_j = "/j"
root_dir_name = os.getcwd()
for dir_path in dir_list:
    os.chdir(dir_path)
    tc_check_instance = get_diff_tc.TcFromTcandJmode(args.output_file, dir_name_tc, dir_name_j)
    tc_check_instance.store_2_curie_temp()
    if abs(tc_check_instance.relative_error) > args.error_criterion:
        print('Caution! Tc in the below directory has an error over the criterion.')
        print(dir_path)
    os.chdir(root_dir_name)

# print(dir_list)
