""" Created on : Sun Mar 10 11:44:13 2019
    author: 
        github.com/71unxv
        github.com/LutfiZakaria
        
    Note:
    
     Python for Geophysical Data Processing and Inverse Problem  
    _______________________________________________________________________________

    Cheers!
"""
# Import Library
#   ==============================================================================================================
import numpy as np
import pandas as pd
#import seaborn as sns

#%matplotlib inline
import matplotlib.pyplot as plt

# Function
#   ==============================================================================================================


# run code! Run!!
#   ==============================================================================================================

Topo = pd.read_csv('topoSBY.csv',names=['x','y','z'])

#extent = x_min, x_max, y_min, y_max = [Topo.x.min()-1000, Topo.x.max()+1000, Topo.y.min()-1000, Topo.y.max()+1000]
# 


