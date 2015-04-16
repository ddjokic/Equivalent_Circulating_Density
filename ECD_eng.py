# -*- coding: utf-8 -*-
"""
Use script on your own risk - NO ANY KIND OF WARRANTY

@author: D. Djokic, 2015
"""

import math

def flow(t300,t600):
    #flow behaviour index, dimensionless
    n=3.32*math.log10(t600/t300)
    return n
    
def cons(t300, n):
    #consistency index in poise
    K=t300/(511**n)
    return K
    
dh = []
dp = []
l = []
v= []
vc = []
flowc = []
ps = []
ecd1=[]
print "NO ANY KIND OF WARRANTY"

t300 = int(input("Viscometer Dial Reading at 300 rpm: "))
t600 = int(input("Viscometer Dial Reading at 600 rpm: "))
TVD = float(input("True Vertical Depth [ft]: "))
Q = float(input("Flow rate [gpm]: "))
MW = float(input("Mud Weight [ppg]: "))
PV = float(input("Plastic viscosity of the mud [cp]: "))
SEG = int(input("Number of pipe segments: "))
#todo: drill collar and drill pipe

for cnt in range (0, SEG):
    Dh = float(input("Inner Diameter of the hole [in]: "))
    Dp = float(input("Outer Diameter of drill pipe or drill collar [in]: "))
    L = float(input("Length of drill pipe or drill collar [ft]: "))
    dh.append(Dh)
    dp.append(Dp)
    l.append(L)
    
n = flow(t300, t600)   
K = cons(t300,n)

for cnt in range (0,SEG):
#annular velocity v[ft/min]:
    velo=(24.5*Q)/(dh[cnt]**2-dp[cnt]**2)
    v.append(velo)
    
# critical velocity [ft/min]:
    veloc=(((3.878*10**4)*K/MW)**(1/(2-n)))*((2.4/(dh[cnt]-dp[cnt])*(2*n+1)/(3*n))**(n/(2-n)))
    vc.append(veloc)
    
#pressure loss [psi]
    if v[cnt]>vc[cnt]:
        FLW = "TURBULENT"
        PS = ((7.7*10**(-5))*(MW**0.8)*(Q**1.8)*(PV**0.2)*l[cnt])/(((dh[cnt]-dp[cnt])**3)*(dh[cnt]+dp[cnt])**1.8)
        
        flowc.append(FLW)
        ps.append(PS)
    else:
        FLW = "LAMINAR"
        PS = ((2.4*v[cnt]/(dh[cnt]-dp[cnt])*(2*n+1)/(3*n))**n)*K*l[cnt]/(300*(dh[cnt]-dp[cnt]))#greshka
        flowc.append(FLW)
        ps.append(PS)

if MW < 13:
#total pressure loss
    ploss = sum(ps)
#equivqlent circulating density
    ECD = (ploss/0.052/TVD)+MW
    for cnt in range (0, SEG):
        print ("Segment number: ", cnt+1)
        print ("Anullar velocity [ft/min]: ", round(v[cnt], 3))
        print ("Critical velocity [ft/min]: ", round(vc[cnt], 3))
        print ("Flow: ", flowc[cnt])
        print ("Pressure loss in segment [psi]: ", round(ps[cnt], 3))
        print (50*"*")
    print ("Total pressure loss [psi]: ", round(ploss, 3))
    print ("Equivalent Circulation Density [ppg]: ", round(ECD, 3))
else:
   print "Calculations for Mud Weight bigger that 13 ppg is not available, yet!"
