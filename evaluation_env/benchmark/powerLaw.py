'''
Created on 5. 6. 2018

@author: Tom
'''
import numpy as np


def powerLaw(alpha, xmin=1):
        r = np.random.random()
        return xmin * (1 - r) ** (-1 / (alpha - 1))
