#!/usr/bin/python
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Enable or disable a network adapter')
parser.add_argument('-n', '--adapter-name', default='Thunderbolt Ethernet',
                    help='Toggle network adapter')
args = parser.parse_args()
adapter = args.adapter_name

rv = subprocess.Popen('networksetup -getnetworkserviceenabled "{}"'.format(adapter), shell=True, stdout=subprocess.PIPE).stdout.read()
if 'Enabled' in rv:
	print('{} is enabled. Disabling...'.format(adapter))
	toggle = 'off'
else:
	print('{} is disabled. Enabling...'.format(adapter))
	toggle = 'on'
subprocess.Popen('networksetup -setnetworkserviceenabled "{}" {}'.format(adapter, toggle), shell=True, stdout=subprocess.PIPE)

