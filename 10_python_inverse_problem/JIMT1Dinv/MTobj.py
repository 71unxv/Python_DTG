"""
  Created on :
    18:40 GMT+7 - 07 Mar 2019
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

#import JIMT1Dinv.MTfunc as mt
#import matplotlib.pyplot as plt


# Import Library
import numpy as np
import matplotlib.pyplot as plt
import pickle


class ModelMT:

    def __init__(self, res, thick, Xcoor=0, Ycoor=0, Zcoor=0):
        self.res = res
        self.thick = thick
        self.Xcoor = Xcoor
        self.Ycoor = Ycoor
        self.Zcoor = Zcoor

    def plotModel(self):
        plt.step(self.res, np.cumsum(self.thick))
        plt.gca().invert_yaxis()
        plt.show()

    def save(self, FileName):
        with open(FileName, 'wb') as output:  # Python 3: open(..., 'wb')
            pickle.dump(self, output)

    def read(FileName):
        with open(FileName, 'rb') as input:  # Python 3: open(..., 'rb')
            hasilread = pickle.load(input)
        return hasilread


class DataMT:

    def __init__(self, AppRes, Phase, Frequency, Xcoor=0, Ycoor=0, Zcoor=0, AppResWeight=0, PhaseWeight=0):
        self.AppRes = AppRes
        self.Phase = Phase
        self.Frequency = Frequency
        self.Xcoor = Xcoor
        self.Ycoor = Ycoor
        self.Zcoor = Zcoor
        if AppResWeight == 0:
            self.AppResWeight = np.ones(len(AppRes))
        if PhaseWeight == 0:
            self.PhaseWeight = np.ones(len(Phase))

    def save(self, FileName):
        with open(FileName, 'wb') as output:  # Python 3: open(..., 'wb')
            pickle.dump(self, output)

    def read(FileName):
        with open(FileName, 'rb') as input:  # Python 3: open(..., 'rb')
            hasilread = pickle.load(input)
        return hasilread


def forwardMT1D(ModelMT,DataMT):
    for ii in range(len(DataMT.Frequency)):
        DataMT.AppRes[ii],DataMT.Phase[ii] = forwardFuncMT1D(ModelMT.res, ModelMT.thick, DataMT.Frequency[ii])
    return DataMT




def forwardFuncMT1D(res,thick,freq):

    # res = np.asarray(res)
    # thick = np.asarray(thick)
    # freq = np.asarray(freq)
    mu = 4 * np.pi * 1E-7
    w = 2 * np.pi * freq
    Z = np.sqrt(1j * w * mu * res[-1])
#    print(res[-1])
    for ii in range(len(res)-2,-1,-1):
        dj = np.sqrt(w * mu * (1.0/res[ii]) * 1j)
        wj = dj * res[ii]
        ej = np.exp (-2 * thick[ii]*dj)
#        print(res[ii])
        rj = (wj - Z)/(wj + Z)
        re = rj*ej
        Z = wj * ((1 - re)/(1 + re))

    AppRes = (abs(Z)**2)/(mu * w)
    Phase = np.arctan2(Z.imag,Z.real)
#    print("=== "*10)
    return AppRes,Phase


def calculateJacobMT1D(res,thick,freq,par):
    # dm/dx = f(m) - f(m+dm)/dm

    # App = np.zeros(len(freq))
    # Phase = np.zeros(len(freq))
    # App_dm = np.zeros(len(freq))
    # Phase_dm = np.zeros(len(freq))
    Jacob_App = np.zeros([len(freq),len(res)])
    Jacob_Phase = np.copy(Jacob_App)
    for ii in range(len(res)):
        res_dm = np.copy(res)
        dm = res_dm[ii] * par
        res_dm[ii] = res_dm[ii]+dm

        for jj in range(len(freq)):
            App, Phase = forwardMT1D(res, thick, freq[jj])
            App_dm, Phase_dm = forwardMT1D(res_dm, thick, freq[jj])

            Jacob_App[jj,ii] = (np.log(App) - np.log(App_dm))/np.log(dm)
            Jacob_Phase[jj,ii] = (np.log(Phase) - np.log(Phase_dm))/np.log(dm)
    Jacob = np.append(Jacob_App,Jacob_Phase,axis=0)
    return Jacob



#def clear_all():
#    """Clears all the variables from the workspace of the spyder application."""
#    gl = globals().copy()
#    for var in gl:
#        if var[0] == '_': continue
#        if 'func' in str(globals()[var]): continue
#        if 'module' in str(globals()[var]): continue
#
#        del globals()[var]
# if __name__ == "__main__":
#     clear_all()


# ============================================================================================
# Run Code! Run!

# clear_all()
#
# resistivity = np.array([100,100,500,500,500,100,1000])
# thickness = np.ones([len(resistivity)]) * 400
# freq = np.linspace(-4,4,160)
# freq = 10**freq
#
#
# App = np.zeros(len(freq))
# Phase = np.zeros(len(freq))
# for ii in range(np.size(freq)):
#     App[ii],Phase[ii] = forwardMT1D(resistivity,thickness,freq[ii])
#
# plt.subplot(121)
# plt.loglog(freq,App)
#
# plt.subplot(122)
# plt.plot(np.log(freq),np.rad2deg(Phase))
# plt.show()

# fig = plt.figure()
# # fig.add_subplot(121)
# fig.add_subplot(121).loglog(freq,App)
#
# fig.show()
# # fig.add_subplot(122)
# # fig.add_subplot(122).loglog(freq,Phase)
# # fig.show()

