from math import exp, pi
from numpy import linspace, array
import matplotlib.pyplot as plt


#Function to velocity and displacement
def model_function(mu):
    e = 1.60217663*(10**(-19)) #--> electron charge(eV)

    Φ = 0.2*e #--> work function (eV) mobility
    T=300 #--> electrode temperature (K) - Room Temperature
    A = 120
    B = 11606*Φ
    J = (A*(T**2)*exp((-B)/T))/10000 #--> current density (amp/m^2)
    J0 = A*((B)**2)
    Jbar = J/J0


    Ep = 8.85418782*(10**(-12)) #--> Permitivity of free space (m^-3 kg^-1 s^4 A^2)
    m = 9.1093837*(10**(-31)) #--> mass of e (kg)

    mu0 = (e**(Ep**2))/(m*A*B)
    mubar = mu/mu0

    E = 10
    E0 = B
    Ebar = E/E0

    t = linspace(0,100,1000)
    t0 = Ep/(A*B)
    tbar = array([(t/t0) for t in t])


    vtbar_list = []
    for t in tbar:
        vtbar_list.append(mubar*((((mubar*Jbar)-Ebar)*(exp((-t)/mubar)-1))+(Jbar*t)))
    vtbar_array = array(vtbar_list)
    # print(vtbar_array)

    xtbar_list = []
    for t in tbar:
        xtbar_list.append(mubar*((((mubar*Jbar)-Ebar)*((-mubar*exp((-t)/mubar))-t+mubar))+(Jbar*(t**2)*0.5)))
    xtbar_array = array(xtbar_list)
    # print(xtbar_array)
    return vtbar_array, xtbar_array, tbar


#Plot graph for non-dimensionless Displacement against Non-Dimensionless Time
def plot_xt(mu_list, mu_index):
    fig, ax = plt.subplots(1, 1, figsize=(10,5))
    for mu, ind in zip(mu_list, mu_index):
        vtbar, xtbar, t = model_function(mu)
        print(ind, vtbar)
        ax.plot(t, xtbar, linewidth=1, label=f"{ind}: {mu}")
    ax.set_xlabel('time')
    ax.set_ylabel('')
    ax.set_title("ND-Displacement against ND-Time")
    ax.legend()
    # ax.set_yscale('log')
    # ax.set_xscale('log')
    plt.show()
    return

#Plot graph for non-dimensionless Velocity against Non-Dimensionless Time
def plot_vt(mu_list, mu_index):
    fig, ax = plt.subplots(1, 1, figsize=(10,5))
    for mu, ind in zip(mu_list, mu_index):
        vtbar, xtbar, t = model_function(mu)
        ax.plot(t, vtbar, linewidth=1, label=f"{ind}: {mu}")
    ax.set_xlabel('time')
    ax.set_ylabel('')
    ax.set_title("ND-Velocity against ND-Time")
    ax.legend()
    # ax.set_yscale('log')
    # ax.set_xscale('log')
    plt.show()
    return

mu_list = [0.14, 0.39, 0.0001, 1*(10**(-7))]
mu_index = ["Silicon", "Germanium", "OLED", "PTB7"]

# mu_list = [0.0001]
# mu_index = ["OLED"]
plot_xt(mu_list, mu_index)
plot_vt(mu_list, mu_index)