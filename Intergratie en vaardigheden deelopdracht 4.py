# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:28:44 2024

@author: daphn
"""

import numpy as np
import matplotlib.pyplot as plt

#GEWICHTEN
m_windmolendeel = 230000 #kg
SWLmax = ((m_windmolendeel/94)*100) #kg
m_kraanhuis = (0.34*SWLmax) #kg
m_kraanboom = (0.17*SWLmax) #kg
m_hijsgerei = (0.06*SWLmax) #kg
m_kraan = (m_kraanboom + m_kraanhuis + m_hijsgerei + m_windmolendeel) #kg, inclusief windmolendeel
n = 4 #aantal windmolen stukken
m_deklading = n * 230000


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
vrijboord = np.linspace(1, 5, 5) #meter, diepte boot
d_boot = 10 #meter, diepgang boot
ll_ballasttank = l_boot #meter, lengte lange ballasttank
bl_ballasttank = 6.65 #meter, breedte lange ballasttank
dl_ballasttank = d_boot + vrijboord #meter, diepte lange ballasttank
lk_ballasttank = 34 #meter, lengte korte ballasttank
bk_ballasttank = 6.70 #meter, breedte korte ballasttank
dk_ballasttank = d_boot + vrijboord #meter, diepte korte ballasttank

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

#VOLUMES
v_romp = (2 * (ll_ballasttank * dl_ballasttank * pd_zijwanden)) + (2 * (b_boot * dl_ballasttank * pd_schot)) + (2 * (ll_ballasttank * b_boot * pd_zijwanden)) #volume van de romp
v_tankschot = (2 * (ll_ballasttank * dl_ballasttank * pd_tankwanden)) + (2 * (bk_ballasttank * dk_ballasttank * pd_tankwanden))
v_totaal = v_romp + v_tankschot
v_tank1 = (ll_ballasttank * bl_ballasttank * dl_ballasttank)
v_tank2 = (lk_ballasttank * bk_ballasttank * dk_ballasttank)
v_tank3 = (ll_ballasttank * bl_ballasttank * dl_ballasttank)

m_romp = (v_romp * soortelijk_staalgewicht * f_verstijfers) #kg
m_tankschotten = (v_tankschot * soortelijk_staalgewicht * f_verstijfers)
m_staal = (v_totaal * soortelijk_staalgewicht * f_verstijfers)
#m_tank3 = (v_tank3 * soortelijk_zeewater * vg_tank3)
m_tank3 = 4466007.0

#LCG/TCG
lcg_romp = ZPy_boot - app #meter
lcg_kraan = ZPy_kraan #meter
lcg_scheepslading = 32
lcg_tank1 = (ll_ballasttank / 2) - app
lcg_tank3 = (ll_ballasttank / 2) - app

tcg_romp = b_boot / 2
tcg_kraan = ZPx_kraan
tcg_scheepslading = -2.00
tcg_tank1 = -(0.5 * bk_ballasttank + 0.5 * bl_ballasttank)
tcg_tank2 = 0
tcg_tank3 = -(0.5 * bk_ballasttank + 0.5 * bl_ballasttank)

#MOMENTEN OVER X
Mx_kraan = (m_kraan * tcg_kraan * gv) #moment kraan
Mx_scheepslading = (m_deklading * tcg_scheepslading * gv) #moment scheepslading
Mx_tank3 = (m_tank3 * tcg_tank3 * gv) #moment tank 3
Mx_tank1 = Mx_kraan + Mx_scheepslading + Mx_tank3 #moment tank 1

#m_tank1 = (Mx_tank1 / tcg_tank1 / gv) #massa tank 1
m_tank1 = 3652557.7211730015

#VULLINGSGRAAD TANK 1
vg_tank1 = ((m_tank1 / (soortelijk_zeewater * v_tank1)) * 100)
#print('Vullingsgraad tank 1 =' , vg_tank1, '%')

#OPWAARTSE KRACHT BEREKENEN
Fa = soortelijk_zeewater * gv * l_boot * b_boot * d_boot #opwaartste kracht

#NEERWAARSTEKRACHT BEREKENEN
m_bijnatotaal = (m_staal + m_kraan + m_deklading + m_tank1 + m_tank3) # m_tank2 mist nog
Fneerwaarts = m_bijnatotaal * gv
#m_tank2 = (Fa - Fneerwaarts) / gv
m_tank2 = 3004287.323720615
m_totaal = m_bijnatotaal + m_tank2
m_ladingcapaciteit = (Fa / gv) - (m_staal + m_kraan + m_tank1 + m_tank2 + m_tank3)

#VULLINGSGRAAD TANK 2
vg_tank2 = ((m_tank2 / (soortelijk_zeewater * v_tank2)) * 100)
#print('Vullingsgraad van tank 2 =', vg_tank2, '%')

#MOMENTEN OVER Y
My_opw = (Fa * lcg_romp)
My_boot = (m_staal * lcg_romp * gv)
My_kraan = (m_kraan * lcg_kraan * gv)
My_scheepslading = (m_deklading * lcg_scheepslading * gv)
My_tank1 = (m_tank1 * lcg_tank1 * gv)
My_tank3 = (m_tank3 * lcg_tank3 * gv)
My_tank2 = -(My_kraan + My_scheepslading + My_boot + My_tank1 + My_tank3) + My_opw

lcg_tank2 = (My_tank2 / (m_tank2 * gv))
#print('Zwaartepunt in lengte van tank 2 =', lcg_tank2, 'm')





'------------------------------------------------------------------------------------------'
deplacement = l_boot * b_boot * d_boot

#VCG
vcg_romp = (vrijboord + d_boot) / 2
vcg_tankschotten = dl_ballasttank / 2
vcg_deklading = 10 + (vrijboord + d_boot)
vcg_kraanhuis = (vrijboord + d_boot) + 1
vcg_kraanboom = ((32.5 * np.sin(np.pi/3)) * 0.5) + (vrijboord + d_boot) + 1
vcg_hijsgerei = (32.5 * np.sin(np.pi/3)) + (vrijboord + d_boot) + 1
vcg_kraanlast = (32.5 * np.sin(np.pi/3)) + (vrijboord + d_boot) + 1
vcg_kraan_lading = (vcg_deklading * m_deklading + vcg_kraanhuis * m_kraanhuis + vcg_kraanboom * m_kraanboom + vcg_hijsgerei * m_hijsgerei) / (m_kraan + m_deklading - m_windmolendeel)

vcg_tank1 = ((vg_tank1 / 100) * dl_ballasttank) / 2
vcg_tank2 = ((vg_tank2 / 100) * dk_ballasttank) / 2
vcg_tank3 = (vg_tank3 * dl_ballasttank) / 2

vcg_tanktotaal = (vcg_tank1 * m_tank1 + vcg_tank2 * m_tank2 + vcg_tank3 * m_tank3) / (m_tank1 + m_tank2 + m_tank3)

KB = (d_boot / 2)
KG = (vcg_romp * m_romp + vcg_tankschotten * m_tankschotten + vcg_kraan_lading * (m_kraan + m_deklading - m_windmolendeel) + vcg_kraanlast * m_windmolendeel + vcg_tanktotaal * (m_tank1 + m_tank2 + m_tank3)) / (m_romp + m_tankschotten + m_kraan + m_deklading + m_tank1 + m_tank2 + m_tank3)

It_tank1 = ((bl_ballasttank**3 * ll_ballasttank) / 12) * soortelijk_zeewater
It_tank2 = ((bk_ballasttank**3 * lk_ballasttank) / 12 ) * soortelijk_zeewater
It_tank3 = ((bl_ballasttank**3 * ll_ballasttank) / 12) * soortelijk_zeewater
It_totaal = It_tank1 + It_tank2 + It_tank3

It_boot = (b_boot**3 * l_boot) / 12

BM = It_boot / deplacement * vrijboord / vrijboord

VVC_tank3 = It_tank3 / (deplacement * soortelijk_zeewater)
VVC = (It_tank1 + It_tank2 + It_tank3) / (deplacement * soortelijk_zeewater)

GM = KB + BM - KG
G_M = GM - VVC

# print("1a. GM = ", GM)
# print("1b. G'M = ", G_M)

# print("2a. vcg kraan en lading =", vcg_kraan_lading)
# print("2b. vcg romp =", vcg_romp)
# print("2c. vcg kraanlast =", vcg_kraanlast)
# print("2d. vcg schotten =", vcg_tankschotten)
# print("2e. vcg tankvulling =", vcg_tanktotaal)
# print("2f. VCB =", KB)
# print("2g. VVC tank 3 =", VVC_tank3)
# print("2h. BM =", BM)


fig, ax1 = plt.subplots()
massastaal_lengte = ax1.plot(vrijboord, GM, color="red", label="massa staal tegen lengte")
ax1.set_xlabel("Vrijboord van de boot (m)")
ax1.set_ylabel("GM", color="black")

plt.show



# # Maak de figuur en de eerste as
# fig, ax1 = plt.subplots()

# # Eerste plot (lengte vs deplacement)
# ax1.plot(vrijboord , KB, color="purple", label="KB")  # Nieuwe kleur
# ax1.set_xlabel("Vrijboord boot (m)")
# ax1.set_ylabel("KB", color="purple")
# ax1.tick_params(axis='y', labelcolor="purple")

# # Tweede as (staalgewicht)
# ax2 = ax1.twinx()
# ax2.plot(vrijboord , KG, color="orange", label="KG")  # Nieuwe kleur
# ax2.set_ylabel("KG", color="orange")
# ax2.tick_params(axis='y', labelcolor="orange")

# # Derde as (ladingscapaciteit)
# ax3 = ax1.twinx()
# ax3.spines["right"].set_position(("outward", 60))  # Verplaats derde as
# ax3.plot(vrijboord , BM, color="teal", label="BM")  # Nieuwe kleur
# ax3.set_ylabel("BM", color="teal")
# ax3.tick_params(axis='y', labelcolor="teal")

# # Voeg een legenda toe
# fig.tight_layout()  # Zorg dat labels niet overlappen
# plt.show()

