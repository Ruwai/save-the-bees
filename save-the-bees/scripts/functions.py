'''
Use this script to store any functions that we will be using for our main script.
'''

import pandas as pd
import numpy as np
import scipy.stats as stats

class F(object):

    def __init__(self, mu):
        self.mu = mu

    def stnderr(self, a, b, p, q):

        mu = self.a + np.divide(((self.b - self.a)*self.p), (self.p+self.q))
        return mu