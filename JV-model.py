from math import exp, pi
from numpy import linspace, array, roots,logspace
import matplotlib.pyplot as plt

#fixed variables
Ebar_list = list(linspace(0,100,100, endpoint=True))
Ebar_list = Ebar_list[1:]


#Transit time for varying Ebar
def transit_time(Ebar_list, Dbar, mubar, step):
    Ebar_tr = {}
    for Ebar in Ebar_list:
        Jbar = ((Ebar**2)*exp((-1)/Ebar))/10000

        tr = 0
        xt = 0
        while xt < Dbar:
            t = tr
            xt = mubar*((((mubar*Jbar)-Ebar)*((-mubar*exp((-t)/mubar))-t+mubar))+(Jbar*(t**2)*0.5))
            tr += 1/step
        Ebar_tr[Ebar] = tr
    return Ebar_tr


# Velocity for varying Ebar
def velocity_tr(Ebar_tr_dict, mubar):
    vel_tr = {}
    for Ebar, tr in Ebar_tr_dict.items():
        Jbar = ((Ebar**2)*exp((-1)/Ebar))/10000
        velocity = mubar*((((mubar*Jbar)-Ebar)*(exp((-tr)/mubar)-1))+(Jbar*tr))
        vel_tr[Ebar] = velocity
    return vel_tr


def vel2_trep_int(Ebar_tr_dict, mubar):
    vel_trep = {}
    for Ebar, tr in Ebar_tr_dict.items():
        Jbar = ((Ebar**2)*exp((-1)/Ebar))/10000
        
        xdelta_pts = list(linspace(0, tr, 1000, endpoint=True))
        total_area = 0
        counter = 1
        while counter < len(xdelta_pts):
            #width
            x1 = xdelta_pts[counter]
            x0 = xdelta_pts[counter-1]
            xdelta = x1 - x0

            #height
            vel0 = mubar*((((mubar*Jbar)-Ebar)*(exp((-x0)/mubar)-1))+(Jbar*x0))
            vel1 = mubar*((((mubar*Jbar)-Ebar)*(exp((-x1)/mubar)-1))+(Jbar*x1))
            trep_height = (vel1+vel0)/2

            #Area calculation
            trep_area = xdelta*trep_height
            total_area += trep_area
            counter += 1
        vel_trep[Ebar] = total_area
    return vel_trep


def voltbar(vel_tr_dict, vel2_int_dict, mubar):
    volt_bar = {}
    #vel_tr_dict items list
    Ebar_list = vel_tr_dict.keys()
    vel_list = vel_tr_dict.values()
    int_vel2_list = vel2_int_dict.values()
    for Ebar, vel, int_vel2 in zip(Ebar_list, vel_list, int_vel2_list):
        vbar = ((vel**2)/2) + (1/mubar)*(int_vel2)
        volt_bar[Ebar] = vbar
    return volt_bar


#Jbar with varying Ebar 
def Jbar(Ebar_list, beta = 2):
    Jbar_dict = {}
    for Ebar in Ebar_list:
        Jbar_val =(((Ebar**beta)*exp((-1)/Ebar))/10000)
        Jbar_dict[Ebar] = Jbar_val
    return Jbar_dict


###############################################################################################################
#First Working Code
#Plotting function


# def plot_JV(voltbar_dict, Jbar_dict):
#     fig, ax = plt.subplots(1, 1, figsize=(10,5))
#     Jbar_val_list = Jbar_dict.values()
#     voltbar_val_list = voltbar_dict.values()
#     print(type(voltbar_val_list))

#     ax.plot(voltbar_val_list, Jbar_val_list, linewidth=1, label="JV")
#     ax.set_xlabel('Vbar')
#     ax.set_ylabel('Jbar')
#     ax.set_title("")
#     ax.legend()
#     ax.set_yscale('log')
#     ax.set_xscale('log')
#     plt.show()
#     return

# Dbar = (10**(-2))
# mubar = (10**(-1))
# step = 10000

# Ebar_tr_dict = transit_time(Ebar_list, Dbar, mubar, step)
# vel_tr_dict = velocity_tr(Ebar_tr_dict, mubar)
# vel2_int_dict = vel2_trep_int(Ebar_tr_dict, mubar)
# voltbar_dict = voltbar(vel_tr_dict, vel2_int_dict, mubar)
# Jbar_dict = Jbar(Ebar_list)
# plot_JV(voltbar_dict, Jbar_dict)


##########################################################################################################################################
#fixed mubar varying Dbar
#Plotting function


# def JV_fixmu_varyD(voltbar_list, Jbar_dict, Dbar_list):
#     fig, ax = plt.subplots(1, 1, figsize=(6,4))
#     Jbar_val_list = Jbar_dict.values()
#     for vbar_list, dbar_list in zip(voltbar_list, Dbar_list):
#         ax.plot(vbar_list, Jbar_val_list, linewidth=1, label=f"Dbar: {dbar_list}")
#     ax.set_xlabel('Vbar')
#     ax.set_ylabel('Jbar')
#     ax.set_title("Graph of Jbar against Vbar\nFixed beta(=3), Fixed µbar(=10), Varying Dbar(=0.01-100)")
#     ax.legend(loc = 'lower right')
#     ax.set_yscale('log')
#     ax.set_xscale('log')
#     plt.show()
#     return

# mubar = (10**(1))
# Jbar_dict = Jbar(Ebar_list, beta=3)
# Dbar_list = [(10**(-2)),(10**(-1)),(10**(0)), (10**(1)), (10**(2))]
# step = 5000

# voltbar_list = []
# for Dbar in Dbar_list:
#     Ebar_tr_dict = transit_time(Ebar_list, Dbar, mubar, step)
#     print(Ebar_tr_dict)
#     vel_tr_dict = velocity_tr(Ebar_tr_dict, mubar)
#     print(vel_tr_dict)
#     vel2_int_dict = vel2_trep_int(Ebar_tr_dict, mubar)
#     voltbar_dict = voltbar(vel_tr_dict, vel2_int_dict, mubar)
#     print(voltbar_dict)
#     voltbar_list.append(list(voltbar_dict.values()))
# JV_fixmu_varyD(voltbar_list, Jbar_dict, Dbar_list)

###################################################################################################################################################

# Dbar_list = [(10**(-2)),(10**(-1)),(10**(0)), (10**(1)), (10**(2))]
# mubar_list = [(10**(-2)),(10**(-1)),(10**(0)), (10**(1)), (10**(2))]
# beta_list = [0.5, 1, 1.5, 2, 2.5, 3]
# step_divisor = [10000, 10000, 1000, 100, 100]

####################################################################################################################################################
#fixed D varying mu
def JV_fixD_varymu(voltbar_list, Jbar_dict, mubar_list):
    fig, ax = plt.subplots(1, 1, figsize=(6,4))
    Jbar_val_list = Jbar_dict.values()
    for vbar_list, mbar_list in zip(voltbar_list, mubar_list):
        ax.plot(vbar_list, Jbar_val_list, linewidth=1, label=f"µ: {mbar_list}")
    ax.set_xlabel('Vbar')
    ax.set_ylabel('Jbar')
    ax.set_title("Graph of Jbar against Vbar\nFixed beta(=3), Fixed Dbar(=0.1), Varying µ(=0.01-100)")
    ax.legend(loc = 'lower right')
    ax.set_yscale('log')
    ax.set_xscale('log')
    # ax.set_ylim([(10**(-16)), 10**(5)])
    # ax.set_xlim([(10**(-3)), (10**(4))])
    plt.show()
    return

mubar_list = [(10**(-2)),(10**(-1)),(10**(0)), (10**(1)), (10**(2))]
Jbar_dict = Jbar(Ebar_list, beta=3)
Dbar = (10**(-1))
step = 5000

voltbar_list = []
for mubar in mubar_list:
    Ebar_tr_dict = transit_time(Ebar_list, Dbar, mubar, step)
    print(Ebar_tr_dict)
    vel_tr_dict = velocity_tr(Ebar_tr_dict, mubar)
    print(vel_tr_dict)
    vel2_int_dict = vel2_trep_int(Ebar_tr_dict, mubar)
    voltbar_dict = voltbar(vel_tr_dict, vel2_int_dict, mubar)
    print(voltbar_dict)
    voltbar_list.append(list(voltbar_dict.values()))
JV_fixD_varymu(voltbar_list, Jbar_dict, mubar_list)


