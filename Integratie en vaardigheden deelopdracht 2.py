# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:32:58 2024

@author: daphn
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


#GEWICHTEN
m_windmolendeel = 400000 #kg
SWLmax = ((m_windmolendeel/94)*100) #kg

m_kraanhuis = (0.34*SWLmax) #kg
m_kraanboom = (0.17*SWLmax) #kg
m_hijsgerei = (0.06*SWLmax) #kg
m_kraan = (m_kraanboom + m_kraanhuis + m_hijsgerei + m_windmolendeel) #kg, inclusief windmolendeel
m_scheepslading = 6 * 230000

#ZWAARTEPUNTEN
ZPx_windmolendeel = 24.25 #zwaartpunt van het hangende windmolendeel op de x-as
ZPy_windmolendeel = 32 #zwaartepunt van het hangende windmolendeel op de y-as
ZPx_kraanhuis = 8 #zwaartepunt van het kraanhuis op de x-as
ZPy_kraanhuis = 32 #zwaartepunt van het kraanhuis op de y-as
ZPx_kraanboom = 16.125 #zwaartepunt van de kraanboom op de x-as
ZPy_kraanboom = 32 #zwaartepunt van de kraanboom op de y-as
ZPx_hijsgerei = 24.25 #zwaartepunt van het hijsgerei op de x-as
ZPy_hijsgerei = 32 #zwaartepunt van het hijsgerei op de y-as
ZPx_kraan = ((m_kraanhuis * ZPx_kraanhuis) + (m_kraanboom * ZPx_kraanboom) + (m_hijsgerei * ZPx_hijsgerei) + (ZPx_windmolendeel * m_windmolendeel)) / m_kraan #zwaartepunt van de kraan op de x-as, inclusief windmolendeel
ZPy_kraan = 32 #zwaartepunt van de kraan op de y-as
ZPx_boot = 10 #zwaartpunt van de boot op de x-as
ZPy_boot = 35 #zwaartepunt van de boot op de y-as

#AFMETINGEN
l_kraanboom = 32.5 #meter, lengte kraanboom
l_boot = 70 #meter, lengte boot
b_boot = 20 #meter, breedte boot
h_boot = 13 #meter, diepte boot
d_boot = 10 #meter, diepgang boot
ll_ballasttank = 70 #meter, lengte lange ballasttank
bl_ballasttank = 6.65 #meter, breedte lange ballasttank
dl_ballasttank = 13 #meter, diepte lange ballasttank
lk_ballasttank = 34 #meter, lengte korte ballasttank
bk_ballasttank = 6.70 #meter, breedte korte ballasttank
dk_ballasttank = 13 #meter, diepte korte ballasttank

pd_zijwanden = 0.02 #meter, plaatdikte zijwanden
pd_tankwanden = 0.01 #meter, plaatdikte tankwanden
pd_schot = 0.01 #meter, plaatdikte voor/achterschip

#OVERIGE GEGEVENS
soortelijk_staalgewicht = 7850 #kg/m3
soortelijk_zeewater = 1025 #kg/m3
f_verstijfers = 2.1 #factor 2.1 keer het totale gewicht
gv = 9.81 #m/s, gravitatieversnelling
app = 4.2 #meter
vg_tank3 = 0.72 #vullingsgraad tank 3


#------------------------------------------------------------------------------------------
#==========================================================================================

'TANK 1'

tankfilling1_m = np.genfromtxt(fname = 'Tank1_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 0,
                     filling_values = np.NaN)

tankfilling1_percentage = np.genfromtxt(fname = 'Tank1_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 1,
                     filling_values = np.NaN)

tankvolume1 = np.genfromtxt(fname = 'Tank1_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 2,
                     filling_values = np.NaN)

lcg1 = np.genfromtxt(fname = 'Tank1_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 3,
                     filling_values = np.NaN)
tcg1 = np.genfromtxt(fname = 'Tank1_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 4,
                     filling_values = np.NaN)

vcg1 = np.genfromtxt(fname = 'Tank1_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 5,
                     filling_values = np.NaN)


# TANK 1 PLOTTEN
fig, ax1 = plt.subplots()

# Linker y-as plot
line1, = ax1.plot(tankfilling1_percentage, lcg1, color="blue", label="lcg [m]")
line2, = ax1.plot(tankfilling1_percentage, tcg1, color="green", label="tcg [m]")
line3, = ax1.plot(tankfilling1_percentage, vcg1, color="orange", label="vcg [m]")
ax1.set_xlabel("tankfilling [% of h_tank]")
ax1.set_ylabel("distance [m]", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Tweede y-as toevoegen
ax2 = ax1.twinx()
line4, = ax2.plot(tankfilling1_percentage, tankvolume1, color="red", label="tankvolume [m³]")
ax2.set_ylabel("tankvolume [m³]", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Titel toevoegen
fig.suptitle("Tankdiagram tank 1 volume data")

# Gezamenlijke legenda toevoegen
lines = [line1, line2, line3, line4]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2)

# Grafiek tonen
plt.show()

# Bepalen van tankgewicht en momenten
tankweight1 = tankvolume1 * soortelijk_zeewater * gv
Mx1 = tankweight1 * lcg1
My1 = tankweight1 * tcg1
Mz1 = tankweight1 * vcg1

# MOMENTEN PLOTTEN TANK 1
fig, ax1 = plt.subplots()

# Linker y-as plot
line5, = ax1.plot(tankfilling1_percentage, My1, color="blue", label="My [kgm]")
line6, = ax1.plot(tankfilling1_percentage, Mz1, color="green", label="Mz [kgm]")
ax1.set_xlabel("tankfilling [% of h_tank]")
ax1.set_ylabel("My of Mz [kgm]", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Tweede y-as toevoegen
ax2 = ax1.twinx()
line7, = ax2.plot(tankfilling1_percentage, Mx1, color="red", label="Mx [kgm]")
ax2.set_ylabel("Mx [kgm]", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Titel toevoegen
fig.suptitle("Tank 1: momenten in x, y en z")

# Gezamenlijke legenda toevoegen
lines = [line5, line6, line7]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)

# Grafiek tonen
plt.show()


#--------------------------------------------------------------------------------------------
#================================================================================================

'TANK 2' 
tankfilling2_m = np.genfromtxt(fname = 'Tank2_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 0,
                     filling_values = np.NaN)

tankfilling2_percentage = np.genfromtxt(fname = 'Tank2_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 1,
                     filling_values = np.NaN)

tankvolume2 = np.genfromtxt(fname = 'Tank2_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 2,
                     filling_values = np.NaN)

lcg2 = np.genfromtxt(fname = 'Tank2_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 3,
                     filling_values = np.NaN)

tcg2 = np.genfromtxt(fname = 'Tank2_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 4,
                     filling_values = np.NaN)

vcg2 = np.genfromtxt(fname = 'Tank2_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 5,
                     filling_values = np.NaN)

# TANK 2 PLOTTEN
fig, ax1 = plt.subplots()

# Linker y-as plot
line14, = ax1.plot(tankfilling2_percentage, lcg2, color="blue", label="lcg [m]")
line15, = ax1.plot(tankfilling2_percentage, tcg2, color="green", label="tcg [m]")
line16, = ax1.plot(tankfilling2_percentage, vcg2, color="orange", label="vcg [m]")
ax1.set_xlabel("tankfilling [% of h_tank]")
ax1.set_ylabel("distance [m]", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Tweede y-as toevoegen
ax2 = ax1.twinx()
line17, = ax2.plot(tankfilling2_percentage, tankvolume2, color="red", label="tankvolume [m³]")
ax2.set_ylabel("tankvolume [m³]", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Titel toevoegen
fig.suptitle("Tankdiagram tank 2 volume data")

# Gezamenlijke legenda toevoegen
lines = [line14, line15, line16, line17]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2)

# Grafiek tonen
plt.show()

# Bepalen van tankgewicht en momenten
tankweight2 = tankvolume2 * soortelijk_zeewater * gv
Mx2 = tankweight2 * lcg2
My2 = tankweight2 * tcg2
Mz2 = tankweight2 * vcg2

# MOMENTEN PLOTTEN TANK 2
fig, ax1 = plt.subplots()

# Linker y-as plot
line18, = ax1.plot(tankfilling2_percentage, My2, color="blue", label="My [kgm]")
line19, = ax1.plot(tankfilling2_percentage, Mz2, color="green", label="Mz [kgm]")
ax1.set_xlabel("tankfilling [% of h_tank]")
ax1.set_ylabel("My of Mz [kgm]", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Tweede y-as toevoegen
ax2 = ax1.twinx()
line20, = ax2.plot(tankfilling2_percentage, Mx2, color="red", label="Mx [kgm]")
ax2.set_ylabel("Mx [kgm]", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Titel toevoegen
fig.suptitle("Tank 2: momenten in x, y en z")

# Gezamenlijke legenda toevoegen
lines = [line18, line19, line20]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)

# Grafiek tonen
plt.show()

#-------------------------------------------------------------------------------------------
#===========================================================================================
'TANK 3'

tankfilling3_m = np.genfromtxt(fname = 'Tank3_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 0,
                     filling_values = np.NaN)

tankfilling3_percentage = np.genfromtxt(fname = 'Tank3_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 1,
                     filling_values = np.NaN)

tankvolume3 = np.genfromtxt(fname = 'Tank3_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 2,
                     filling_values = np.NaN)

lcg3 = np.genfromtxt(fname = 'Tank3_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 3,
                     filling_values = np.NaN)

tcg3 = np.genfromtxt(fname = 'Tank3_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 4,
                     filling_values = np.NaN)

vcg3 = np.genfromtxt(fname = 'Tank3_Diagram_Volume_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 3,
                     usecols = 5,
                     filling_values = np.NaN)

# TANK 3 PLOTTEN
fig, ax1 = plt.subplots()

# Linker y-as plot
line28, = ax1.plot(tankfilling3_percentage, lcg3, color="blue", label="lcg [m]")
line29, = ax1.plot(tankfilling3_percentage, tcg3, color="green", label="tcg [m]")
line30, = ax1.plot(tankfilling3_percentage, vcg3, color="orange", label="vcg [m]")
ax1.set_xlabel("tankfilling [% of h_tank]")
ax1.set_ylabel("distance [m]", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Tweede y-as toevoegen
ax2 = ax1.twinx()
line31, = ax2.plot(tankfilling3_percentage, tankvolume3, color="red", label="tankvolume [m³]")
ax2.set_ylabel("tankvolume [m³]", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Titel toevoegen
fig.suptitle("Tankdiagram tank 3 volume data")

# Gezamenlijke legenda toevoegen
lines = [line28, line29, line30, line31]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2)

# Grafiek tonen
plt.show()

# Bepalen van tankgewicht en momenten
tankweight3 = tankvolume3 * soortelijk_zeewater *gv
Mx3 = tankweight3 * lcg3 #kgm
My3 = tankweight3 * tcg3 #kgm
Mz3 = tankweight3 * vcg3 #kgm

# MOMENTEN PLOTTEN TANK 3
fig, ax1 = plt.subplots()

# Linker y-as plot
line32, = ax1.plot(tankfilling3_percentage, My3, color="blue", label="My [kgm]")
line33, = ax1.plot(tankfilling3_percentage, Mz3, color="green", label="Mz [kgm]")
ax1.set_xlabel("tankfilling [% of h_tank]")
ax1.set_ylabel("My of Mz [kgm]", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Tweede y-as toevoegen
ax2 = ax1.twinx()
line34, = ax2.plot(tankfilling3_percentage, Mx3, color="red", label="Mx [kgm]")
ax2.set_ylabel("Mx [kgm]", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Titel toevoegen
fig.suptitle("Tank 3: momenten in x, y en z")

# Gezamenlijke legenda toevoegen
lines = [line32, line33, line34]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)

# Grafiek tonen
plt.show()

#========================================================================================
#------------------------------------------------------------------------------------------
hull_areas = np.genfromtxt(fname = 'HullAreaData_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 1,
                     usecols = 1,
                     filling_values = np.NaN)

area_spiegel = hull_areas[0]
area_huid = hull_areas[1]
area_dek = hull_areas[2]

lca = np.genfromtxt(fname = 'HullAreaData_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 1,
                     usecols = 2,
                     filling_values = np.NaN)

lca_spiegel = lca[0]
lca_huid = lca[1]
lca_dek = lca[2]

tca = np.genfromtxt(fname = 'HullAreaData_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 1,
                     usecols = 4,
                     filling_values = np.NaN)

tca_spiegel = tca[0]
tca_huid = tca[1]
tca_dek = tca[2]
#==============================================================================
m_spiegel = ((area_spiegel*pd_schot)*soortelijk_staalgewicht*f_verstijfers)
m_huid = ((area_huid*pd_zijwanden)*soortelijk_staalgewicht*f_verstijfers)
m_dek = ((area_dek*pd_zijwanden)*soortelijk_staalgewicht*f_verstijfers)

BHD_area = np.genfromtxt(fname = 'TankBHD_Data_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 2,
                     usecols = 0,
                     filling_values = np.NaN)

#VOLUMES
v_romp = ((area_dek + area_huid) * pd_zijwanden) + (area_spiegel * pd_schot)
v_tankschot1 = BHD_area[0] * pd_tankwanden
v_tankschot2 = BHD_area[1] * pd_tankwanden
v_tankschot3 = BHD_area[2] * pd_tankwanden
v_tankschot4 = BHD_area[3] * pd_tankwanden
v_tankschot5 = BHD_area[4] * pd_tankwanden
v_tankschot6 = BHD_area[5] * pd_tankwanden
v_tankschot7 = BHD_area[6] * pd_tankwanden
v_tankschot8 = BHD_area[7] * pd_tankwanden
v_totaal = v_romp + v_tankschot1 + v_tankschot2 + v_tankschot3 + v_tankschot4 + v_tankschot5 + v_tankschot6 + v_tankschot7 + v_tankschot8

v_tank1 = (ll_ballasttank * bl_ballasttank * dl_ballasttank)
v_tank2 = (lk_ballasttank * bk_ballasttank * dk_ballasttank)
v_tank3 = 3622.4919 #72 procent vulling

m_romp = v_romp * soortelijk_staalgewicht * f_verstijfers

m_tankschot1 = (v_tankschot1 * soortelijk_staalgewicht * f_verstijfers)
m_tankschot2 = (v_tankschot2 * soortelijk_staalgewicht * f_verstijfers)
m_tankschot3 = (v_tankschot3 * soortelijk_staalgewicht * f_verstijfers)
m_tankschot4 = (v_tankschot4 * soortelijk_staalgewicht * f_verstijfers)
m_tankschot5 = (v_tankschot5 * soortelijk_staalgewicht * f_verstijfers)
m_tankschot6 = (v_tankschot6 * soortelijk_staalgewicht * f_verstijfers)
m_tankschot7 = (v_tankschot7 * soortelijk_staalgewicht * f_verstijfers)
m_tankschot8 = (v_tankschot8 * soortelijk_staalgewicht * f_verstijfers)
m_tankschotten = m_tankschot1 + m_tankschot2 + m_tankschot3 + m_tankschot4 + m_tankschot5 + m_tankschot6 + m_tankschot7 + m_tankschot8

m_staal = (v_totaal * soortelijk_staalgewicht * f_verstijfers)
m_tank3 = (v_tank3 * soortelijk_zeewater)
#==============================================================================

#LCG/TCG
lcg_romp = ((lca_spiegel * area_spiegel) + (lca_huid * area_huid) + (lca_dek * area_dek)) / (area_spiegel + area_huid + area_dek)
lcg_kraan = ZPy_kraan #meter
lcg_scheepslading = 32

lcg_BHD = np.genfromtxt(fname = 'TankBHD_Data_Gr98_V1.0.txt',
                     delimiter = ',',
                     skip_header = 2,
                     usecols = 1,
                     filling_values = np.NaN)

tcg_kraan =  ZPx_kraan
tcg_scheepslading = -2.00
tcg_tank3 = -6.5503

#MOMENTEN DWARSSCHEEPS
dm_kraan = (m_kraan *tcg_kraan * gv) #moment kraan
dm_scheepslading = (m_scheepslading * tcg_scheepslading * gv) #moment scheepslading
dm_tank3 = (m_tank3 * tcg_tank3 * gv)
dm_tank1 = - dm_kraan - dm_scheepslading - dm_tank3 #moment tank 1


fMx = interp1d(My1, tankfilling1_percentage, kind = 'cubic', fill_value = "extrapolate")
vullingsgraad_tank1 = fMx(dm_tank1)

print ("1a. Vullingsgraad van tank 1 is", vullingsgraad_tank1)

ftcg1 = interp1d(tankfilling1_percentage, tcg1, kind = 'cubic', fill_value = "extrapolate")
tcg_tank1 = ftcg1(vullingsgraad_tank1)
#print(tcg_tank1)


BV = 12081.118
Fa = BV * gv * soortelijk_zeewater #buoyant volume, opwaartse kracht
m_tank1 = (dm_tank1 / tcg_tank1 / gv) #massa tank 1

m_bijnatotaal = (m_romp + m_kraan + m_scheepslading + m_tank1 + m_tank3 + m_tankschotten) # m_tank2 mist nog
Fneerwaarts = m_bijnatotaal * gv


m_tank2 = ((Fa - Fneerwaarts) / gv)
m_totaal = m_bijnatotaal + m_tank2


#VULLINGSGRAAD TANK 2
# vullingsgraad_tank2 = ((m_tank2 / (soortelijk_zeewater * v_tank2)) * 100)
# print('1b. Vullingsgraad van tank 2 =', vullingsgraad_tank2, '%')
fm2 = interp1d(tankweight2, tankfilling2_percentage, kind = 'cubic', fill_value = "extrapolate")
vullingsgraad_tank2 = fm2(m_tank2 * gv)
print('1b. Vullingsgraad tank 2 =', vullingsgraad_tank2)


flcg1 = interp1d(tankfilling1_percentage, lcg1, kind = 'cubic', fill_value = "extrapolate")
lcg_tank1 = flcg1(vullingsgraad_tank1)
#print(lcg_tank1)

lcg_tank3 = 30.9981

#MOMENTEN OVER Y
lsm_opw = (Fa * 31.6212)
lsm_romp = (m_romp * lcg_romp * gv)
lsm_kraan = (m_kraan * lcg_kraan * gv)
lsm_scheepslading = (m_scheepslading * lcg_scheepslading * gv)
lsm_tank1 = (m_tank1 * lcg_tank1 * gv)
lsm_tank3 = (m_tank3 * lcg_tank3 * gv)

lsm_tankschot1 = m_tankschot1 * lcg_BHD[0] * gv
lsm_tankschot2 = m_tankschot2 * lcg_BHD[1] * gv
lsm_tankschot3 = m_tankschot3 * lcg_BHD[2] * gv
lsm_tankschot4 = m_tankschot4 * lcg_BHD[3] * gv
lsm_tankschot5 = m_tankschot5 * lcg_BHD[4] * gv
lsm_tankschot6 = m_tankschot6 * lcg_BHD[5] * gv
lsm_tankschot7 = m_tankschot7 * lcg_BHD[6] * gv
lsm_tankschot8 = m_tankschot8 * lcg_BHD[7] * gv

lsm_tank2 = -(lsm_romp + lsm_kraan + lsm_scheepslading + lsm_tank1 + lsm_tank3 + lsm_tankschot1 + lsm_tankschot2 + lsm_tankschot3 + lsm_tankschot4 + lsm_tankschot5 + lsm_tankschot6 + lsm_tankschot7 + lsm_tankschot8) + lsm_opw

lcg_tank2 = (lsm_tank2 / (m_tank2 * gv))
print('1c. Zwaartepunt in lengte van tank 2 =', lcg_tank2, 'm')

print('2a. Massa van de romp =', m_romp)
print('2b. Massa van de tankschotten =', m_tankschot1 + m_tankschot2 + m_tankschot3 + m_tankschot4 + m_tankschot5 + m_tankschot6 + m_tankschot7 + m_tankschot8)
print('2c. Lcg van de romp =', lcg_romp)




print('2h. SWLmax =', SWLmax)
print('2i. Gewicht kraanboom + kraanhuis =', (m_kraanboom + m_kraanhuis))
print('2j. tcg kraanboom =', ZPx_kraanboom)
