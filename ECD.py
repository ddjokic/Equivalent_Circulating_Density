#/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Source:
Formulas and Calculation for Drilling, Production and Workover, 2nd Edition

Use scripts on your own risk - no any kind of warranty.

@author: D. Djokic, 2015
"""
dh=[]
dp=[]
l=[]
av=[]
apl=[]

print "Source: Formulas and Calculation for Drilling, Production and Workover, 2nd Edition"
print "NO ANY KIND OF WARRANTY"
SEG = int(input("Number of Segments of Drill pipe - Different Dia: "))
for n in range(0, SEG):
     print ("\n")
     print ("Segment: ", n+1)
     Dh = float(input("Inner Diameter of the Hole or Casing [in]: "))
     Dp = float(input("Outer Diameter of Drill Pipe or Drill Collar [in]: "))
     L = float(input("Length of Annular Section [ft]: "))
     dh.append(Dh)
     dp.append(Dp)
     l.append(L)
     
print ("\n")
CR = float(input("Mud Cirulation Rate [gpm]: "))
TVD = float(input("True Vertical Depth [ft]: "))
MW = float(input("Mud Weight [ppg]: "))

for n in range(0, SEG):
    AV = 24.5*CR/(dh[n]**2-dp[n]**2)
    av.append(AV)
    APL = (1.4327*10**(-7))*MW*l[n]*(av[n]**2)/(dh[n]-dp[n])
    apl.append(APL)
    
APLS = sum(apl)

ECD = MW+APLS/(0.052*TVD)

print("\n")
for n in range(0,SEG):
    print ("Segment: ", n+1)
    print ("Annular Velocity [ft/min] = ", round(av[n],3))
    print ("Pressure loss in segment [psi]: ", round(apl[n],3))

print(30*"**")
print ("Total annular pressure loss between depth and surface [psi] = ", round(APLS,3))
print ("Equivalent Circulating Density [ppg] = ", round(ECD,3))