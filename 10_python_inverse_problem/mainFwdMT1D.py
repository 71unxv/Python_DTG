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
import JIMT1Dinv.MTobj as mt
from matplotlib.gridspec import GridSpec





max_depth = 3000

resistivity = np.asarray([100,100,100,1000,900,800,500,300,50,30,20,0.1,20,300,300,400])
thickness = np.ones(len(resistivity)) * (max_depth/len(resistivity))

ModelDummy = mt.ModelMT(resistivity,thickness)

Frequency = 10 **(np.linspace(-4, 4, 40))
AppRes = np.zeros(len(Frequency))
Phase = np.copy(AppRes)

DataDummy = mt.DataMT(AppRes,Phase,Frequency)


DataDummy = mt.forwardMT1D(ModelDummy,DataDummy)

fig01 = plt.figure(1)
grd = GridSpec(2,2) # create grid arrange template

plotModelRes = fig01.add_subplot(grd[:, 1])
plotModelRes.step((ModelDummy.res),np.cumsum(ModelDummy.thick))
plotModelRes.invert_yaxis()
plotModelRes.set_ylabel("Depth(m)")
plotModelRes.set_xlabel("Resistivity(ohm)")
plotModelRes.set_xscale("log")
plotModelRes.set_title("1D Resistivity Profile")
plotModelRes.grid()

plotDataApp = fig01.add_subplot(grd[0,0])
plotDataApp.plot(DataDummy.Frequency,DataDummy.Phase,("k."))
plotDataApp.set_xscale("log")
plotDataApp.set_xlabel("Frequency")
plotDataApp.set_yscale("log")
plotDataApp.set_ylabel("Phase")
plotDataApp.grid()



plotDataPhs = fig01.add_subplot(grd[1,0])
plotDataPhs.plot(DataDummy.Frequency,DataDummy.AppRes,("r."))
plotDataPhs.set_xscale("log")
plotDataPhs.set_xlabel("Frequency")
plotDataPhs.set_yscale("log")
plotDataPhs.set_ylabel("Apparent Resistivity")
plotDataPhs.grid()

fig01.suptitle("Forward Modelling MT 1D")
fig01.show()



DataDummy.save('dataDummy.MT')
ModelDummy.save('modelDummy.mod')







