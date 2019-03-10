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


# ============================================================================================
# Function

# ============================================================================================
# Run Code! Run!

class ModelMT:

    def __init__(self,res,thick,Xcoor = 0,Ycoor = 0,Zcoor = 0):
        self.res = res
        self.thick = thick
        self.Xcoor = Xcoor
        self.Ycoor = Ycoor
        self.Zcoor = Zcoor

    def plotModel(self):

        plt.step(self.res,np.cumsum(self.thick))
        plt.gca().invert_yaxis()
        plt.show()

class DataMT:
    
    def __init__(self,AppRes,Phase,Xcoor = 0,Ycoor = 0,Zcoor = 0,AppResWeight = 0,PhaseWeight = 0):
        self.AppRes = AppRes
        self.Phase = Phase
        self.Xcoor = Xcoor
        self.Ycoor = Ycoor
        self.Zcoor = Zcoor
        if AppResWeight == 0:
            self.AppResWeight = np.ones(len(AppRes))
        if PhaseWeight == 0:
            self.PhaseWeight = np.ones(len(Phase))

    def plotAppRes(self):

        # TODO: add plot AppRes methods

    def plotPhase(self):

        # TODO: add plot methods

# class InvParam:
#     def __init__(self):
# JIMT1D.InvParam.maxIter
# JIMT1D.InvParam.Par
# JIMT1D.InvParam.minRMSE
# JIMT1D.InvParam.maxRMSE
# JIMT1D.InvParam.InvMethods
# JIMT1D.InvParam.LinearSolver
# JIMT1D.InvParam.modelWeight

# TODO: add InvParam Class


