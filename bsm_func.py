#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 12:33:46 2018

@author: edinsonrivera
"""

import pandas as pd
import numpy as np
from math import log, sqrt, exp
from scipy import stats
from scipy.optimize import fsolve

class option:
    def __init__(self, S0, t, M, K, r, sigma):
        
        self.S0 = S0    #initial underlying price
        self.t = t      # current date (datetime data)
        self.M = M      # Maturity date of option (datetime data)
        self.K = K      # strike price
        self.r = r      # risk-less rate
        self.sigma = sigma  # volatility of underlying
        
        
    def option_value():
        #here i will add some code here
        pass
    
    def d1(self):
        #CALCULATION of d1 part of normal distribution
        d1 = ((log(self.S0 / self.K) +  (self.r + 0.5 * self.sigma **2) * self.T) / (self.sigma * sqrt(self.T)))
        return d1
    
    
    
    def d2(self):
        #Calculation d2 part of normal distribution
        d2 = ((log(self.S0 / self.K) / (self.sigma * sqrt(self.T))) / (self.sigma * sqrt(self.T)))
        return d2
    
    def value(self):
        d1 = self.d1()
        d2 = self.d2()
        value = (self.S0 * stats.norm.cdf(d1, 0.0, 1.0) - self.K * exp(-self.r * self.T) * stats.norm.cdf(d2, 0.0, 1.0))
        return value
       
    
    
    
    
