#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 12:33:46 2018

@author: edinsonrivera
"""

import pandas as pd
import numpy as np
import math


class option:
    def __init__(self, S0, t, M, K, r, sigma):
        
        self.S0 = S0    #initial underlying price
        self.t = t      # current date 
        self.M = M      # Maturity date of option
        self.K = K      # strike price
        self.r = r      # risk-less rate
        self.sigma = sigma  # volatility of underlying
        
        
    def option_value():
        
        #add calculation of the option value
        #normal distributon
        #here i will add some code here
        pass
    