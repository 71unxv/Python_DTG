"""
  Created on :
    1:30 GMT+7 - 09 Mar 2019 
  Author     :
    github.com/71unxv
    github.com/LutfiZakaria
______________________________________________________________________________________________
  Note       :
    Python For Geophysical data processing and Inverse Problem    
______________________________________________________________________________________________
    
   Cheers!
"""

# ============================================================================================
# Import Library
import numpy as np
import matplotlib.pyplot as plt
import JIMT1Dinv.MTfunc as mt
from matplotlib.gridspec import GridSpec


# ============================================================================================
# Function

# ============================================================================================
# Run Code! Run!

# mt.clear_all()

max_depth = 3000

resistivity = np.asarray([100,100,100,1000,900,800,500,300,50,30,20,0.1,20,300,300,400])
thickness = np.ones(len(resistivity)) * (max_depth/len(resistivity))
Frequency = 10 **(np.linspace(-4, 4, 40))

AppRes = np.zeros(len(Frequency))
Phase = np.copy(AppRes)
# for ii in range(len(Frequency)):
#     AppRes[ii],Phase[ii] = mt.forwardMT1D(resistivity, thickness, Frequency(ii))












fig01 = plt.figure(1)
grd = GridSpec(2,2) # create grid arrange template

plotModelRes = fig01.add_subplot(grd[:, 1])
plotModelRes.step((resistivity),np.cumsum(thickness))
plotModelRes.invert_yaxis()
plotModelRes.set_ylabel("Depth(m)")
plotModelRes.set_xlabel("Resistivity(ohm)")
plotModelRes.set_xscale("log")
plotModelRes.set_title("1D Resistivity Profile")
plotModelRes.grid()

# plotDataApp = fig01.add_subplot(grd[0,0])
# plotDataApp.plot(Frequency,Phase)
# plotDataApp.set_xscale("log")
# plotDataApp.set_xlabel("Frequency")
# plotDataApp.set_yscale("log")
# plotDataApp.set_ylabel("Apparent Resistivity")
#
#
#
#
# plotDataPhs = fig01.add_subplot(grd[0,0])
# plotDataPhs.plot(Frequency, AppRes)
# plotDataPhs.set_xscale("log")
# plotDataPhs.set_xlabel("Frequency")
# plotDataPhs.set_yscale("log")
# plotDataPhs.set_ylabel("Apparent Resistivity")


fig01.suptitle("Forward Modelling MT 1D")
fig01.show()


