#!/usr/bin/python
import subprocess

rv = subprocess.Popen("networksetup -listallnetworkservices", shell=True, stdout=subprocess.PIPE).stdout.read()
lines = rv.split("\n");

for line in lines:
	if line.startswith("*"):
		print '"{}" is disabled.'.format(line[1:])
	elif line and not line.startswith("An aster"):
		rv = subprocess.Popen('networksetup -getinfo "{}" | grep -iE "^IP address"'.format(line), shell=True, stdout=subprocess.PIPE).stdout.read()
		if rv:
			print '"{}" {}'.format(line, rv[:-1])
		else:
			print '"{}" has no IP address.'.format(line)

