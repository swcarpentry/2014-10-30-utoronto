import sys
import numpy as np

def main():
	script = sys.argv[0]
	filename = sys.argv[1]
	data = np.loadtxt(filname, delimiter = ',')
	for m in data.mean(axis=1):
		print m

