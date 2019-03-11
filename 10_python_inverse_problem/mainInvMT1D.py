"""
  Created on :
    1:21 GMT+7 - 09 Mar 2019 
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
import JIMT1Dinv.MTobj as mt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import copy
# ============================================================================================
# Function

# ============================================================================================
# Run Code! Run!

# read data
# initial data
#
# create jacob


# def runInversion(DataMT,ModelMT,InvparamMT):
    # dm = pinv(J'*J)*J'df

    # calcJacobMT1D(res, thick, freq, par):



### read Data
ModelDummyTrue = mt.ModelMT.read('modelDummy.mod')
DataDummy = mt.DataMT.read('dataDummy.MT')

### Plot Data
# fig01 = plt.figure(1)
# grd = GridSpec(2,2)
#
# plotModelRes = fig01.add_subplot(grd[:, 1])
# ModelDummyTrue.plotModel(plotModelRes)
#
# plotDataApp = fig01.add_subplot(grd[0,0])
# DataDummy.plotData(plotDataApp = plotDataApp)
# #
# #
# plotDataPhs = fig01.add_subplot(grd[1,0])
# DataDummy.plotData(plotDataPhs = plotDataPhs)
# # fig01.show()
# plt.pause(0.5)


#### create Initial Model

ModelInv = copy.copy(ModelDummyTrue)
ModelInv.res[:] = 100 #create 100 ohm initial model for all layers

### create Inversion Parameter
InvParMT = mt.InvParMT()

### forward modelling initial model
DataResult = mt.forwardMT1D(ModelInv,np.copy(DataDummy))

df2 = np.log(DataDummy.Phase)-np.log(DataResult.Phase)
df1 = np.log(DataDummy.AppRes)-np.log(DataResult.AppRes)
df = np.append(df1,df2)
df = df.T

### create Jacobian Matrix

Jacob = mt.calcJacobMT1D(ModelInv,DataDummy,InvParMT)

#
# (Jacob.T Jacob ) * Jacob.T * df
A = np.dot(Jacob.T,Jacob)
dm = np.linalg.multi_dot([np.linalg.pinv(A),Jacob.T,df])







