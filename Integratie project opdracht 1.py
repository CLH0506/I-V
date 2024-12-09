# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:56:16 2024

@author: daphn
"""

#GEWICHTEN
m_windmolendeel = 230000 #kg
SWLmax = ((m_windmolendeel/94)*100) #kg
m_kraanhuis = (0.34*SWLmax) #kg
m_kraanboom = (0.17*SWLmax) #kg
m_hijsgerei = (0.06*SWLmax) #kg
m_kraan = (m_kraanboom + m_kraanhuis + m_hijsgerei + m_windmolendeel) #kg, inclusief windmolendeel
n = 4 #aantal windmolen stukken
m_scheepslading = n * 230000


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

#VOLUMES
v_romp = (2 * (ll_ballasttank * dl_ballasttank * pd_zijwanden)) + (2 * (b_boot * dl_ballasttank * pd_schot)) + (2 * (ll_ballasttank * b_boot * pd_zijwanden)) #volume van de romp
v_tankschot = (2 * (ll_ballasttank * dl_ballasttank * pd_tankwanden)) + (2 * (bk_ballasttank * dk_ballasttank * pd_tankwanden))
v_totaal = v_romp + v_tankschot
v_tank1 = (ll_ballasttank * bl_ballasttank * dl_ballasttank)
v_tank2 = (lk_ballasttank * bk_ballasttank * dk_ballasttank)
v_tank3 = (ll_ballasttank * bl_ballasttank * dl_ballasttank)

m_romp = (v_romp * soortelijk_staalgewicht * f_verstijfers) #kg
m_tankschot = (v_tankschot * soortelijk_staalgewicht * f_verstijfers)
m_staal = (v_totaal * soortelijk_staalgewicht * f_verstijfers)
m_tank3 = (v_tank3 * soortelijk_zeewater * vg_tank3)

#LCG/TCG
lcg_romp = ZPy_boot - app #meter
lcg_kraan = ZPy_kraan #meter
lcg_scheepslading = 32
lcg_tank1 = (70 / 2) - app
lcg_tank3 = (70 / 2) - app

tcg_romp = b_boot / 2
tcg_kraan = ZPx_kraan
tcg_scheepslading = -2.00
tcg_tank1 = -(0.5 * bk_ballasttank + 0.5 * bl_ballasttank)
tcg_tank2 = 0
tcg_tank3 = -(0.5 * bk_ballasttank + 0.5 * bl_ballasttank)

#MOMENTEN OVER X
Mx_kraan = (m_kraan * tcg_kraan * gv) #moment kraan
Mx_scheepslading = (m_scheepslading * tcg_scheepslading * gv) #moment scheepslading
Mx_tank3 = (m_tank3 * tcg_tank3 * gv) #moment tank 3
Mx_tank1 = Mx_kraan + Mx_scheepslading + Mx_tank3 #moment tank 1

m_tank1 = (Mx_tank1 / tcg_tank1 / gv) #massa tank 1

#VULLINGSGRAAD TANK 1
vg_tank1 = ((m_tank1 / (soortelijk_zeewater * v_tank1)) * 100)
print('Vullingsgraad tank 1 =' , vg_tank1, '%')

#OPWAARTSE KRACHT BEREKENEN
Fa = soortelijk_zeewater * gv * l_boot * b_boot * d_boot #opwaartste kracht

#NEERWAARSTEKRACHT BEREKENEN
m_bijnatotaal = (m_staal + m_kraan + m_scheepslading + m_tank1 + m_tank3) # m_tank2 mist nog
Fneerwaarts = m_bijnatotaal * gv
m_tank2 = (Fa - Fneerwaarts) / gv
m_totaal = m_bijnatotaal + m_tank2

#VULLINGSGRAAD TANK 2
vg_tank2 = ((m_tank2 / (soortelijk_zeewater * v_tank2)) * 100)
print('Vullingsgraad van tank 2 =', vg_tank2, '%')

#MOMENTEN OVER Y
My_opw = (Fa * lcg_romp)
My_boot = (m_staal * lcg_romp * gv)
My_kraan = (m_kraan * lcg_kraan * gv)
My_scheepslading = (m_scheepslading * lcg_scheepslading * gv)
My_tank1 = (m_tank1 * lcg_tank1 * gv)
My_tank3 = (m_tank3 * lcg_tank3 * gv)
My_tank2 = -(My_kraan + My_scheepslading + My_boot + My_tank1 + My_tank3) + My_opw

lcg_tank2 = (My_tank2 / (m_tank2 * gv))
print('Zwaartepunt in lengte van tank 2 =', lcg_tank2, 'm')


print(0.51 * SWLmax)
print(m_romp)
print(m_tankschot)
print(lcg_romp)