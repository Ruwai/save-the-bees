'''
	This script will be the main script for creating
	executable commands for the simulation of CCD

	The main library I will be using will be SimPy, a 'discrete event simulation'
	for Python. There will also be an example simulation script in this
	scripts directory that will not be routed to the main functionality of this
	project.

'''
import numpy as np
import simpy
import collections as col
from math import erf, erfc, gamma, tau

rint = np.random.randint
choice = np.random.choice

# Simulation parameters

# time parameters
SIM_TIME_YEARS = 100 # this will represent the next 100 years.
MONTHS_IN_YEAR = [1,2,3,4,5,6,7,8,9,10,11,12]
WEEKS_IN_YEAR = list(range(1,53))
DAYS_IN_YEAR = list(range(1,366))


# location variables
STATES = ['CA']

# Initialize the amount of bees in our colonies.


# Initialize Climate Variables

# Initialize Pesiticide Usage Variables

