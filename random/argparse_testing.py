import argparse
import re

# Creates a new ArgumentParser object
parser = argparse.ArgumentParser()
# Defines how a single command line argument should be parsed
parser.add_argument('device_names', metavar='device_name', type=str, nargs='+',
                    help='list of device names')
args = parser.parse_args()
args_list = args.device_names
device_names_list = list(args_list)
print(device_names_list)

def test_input():
    # turn list into str
    args.device_names = ' '.join(args.device_names)
    # remove space from str
    args.device_names = args.device_names.replace(' ', '')
    if re.search(',', args.device_names):
        device_list = args.device_names.split(',')
    else:
        device_list = device_names_list
    print(device_list)
    
test_input()

# lambda device_names : re.split(','|' ', device_names)