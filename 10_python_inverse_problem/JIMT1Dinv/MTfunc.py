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
import numpy as np
#import matplotlib.pyplot as plt



# ============================================================================================
# Function
# def forwardMT1D(res,thick,frequency):
#     pi = np.pi
#     mu = 4 * pi * 1E-7
#     w = 2 * pi * frequency
#     # Z = np.zeros(len(res))
#     Z = np.sqrt(1j * w * mu * res[-1])
#
#     for i in range(len(res)-2,-1,-1):
#         print(i)
#         print(res[i])
#         Yj = np.sqrt(1j * w * mu * (1.0/res[i]))
#         Wj = Yj * res[i]
#         Ej = np.exp(-2 * Yj * thick[i])
#
#
#         RC = (Wj-Z)/(Wj+Z)
#         RE = RC * Ej
#         Z = Wj * ((1-RE)/(1+RE))
#
#     AppRes = (abs(Z)**2)/(mu * w)
#     Phase = np.arctan2(Z.imag,Z.real)
#
#     return AppRes,Phase


def forwardMT1D(res,thick,freq):
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

