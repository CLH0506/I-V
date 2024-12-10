# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:21:42 2024

@author: daphn
"""
import numpy as np

"OVERIGE GEGEVENS"
soortelijk_staalgewicht = 7850 #kg/m3
soortelijk_zeewater = 1025 #kg/m3
f_verstijfers = 2.1 #factor 2.1 keer het totale gewicht
gv = 9.81 #m/s, gravitatieversnelling
app = 4.2 #meter
cb = ... #blokcoefficient
vg_tank3 = 0.72 #vullingsgraad tank 3
vg_tank1 = 0.45558 #vullingsgraad tank 1
vg_tank2 = 0.87578 #vullingsgraad tank 2
diameter_windmolendeel = 8 #m

'GEWICHTEN'
m_windmolendeel = 4000000 #kg
N_windmolendeel = m_windmolendeel * 9.81
SWLmax = ((m_windmolendeel/94)*100) #kg

m_kraanhuis = (0.34*SWLmax) #kg
m_kraanboom = (0.17*SWLmax) #kg
m_hijsgerei = (0.06*SWLmax) #kg
m_kraan = (m_kraanboom + m_kraanhuis + m_hijsgerei + m_windmolendeel) #kg, inclusief windmolendeel
m_deklading = 6 * m_windmolendeel

'AFMETINGEN'
l_boot = 70 #meter, lengte boot
b_boot = 20 #meter, breedte boot
vrijboord = 3 #meter, diepte boot
d_boot = 10 #meter, diepgang boot
ll_ballasttank = l_boot #meter, lengte lange ballasttank
bl_ballasttank = 6.65 #meter, breedte lange ballasttank
dl_ballasttank = d_boot + vrijboord #meter, diepte lange ballasttank
lk_ballasttank = 34 #meter, lengte korte ballasttank
bk_ballasttank = 6.70 #meter, breedte korte ballasttank
dk_ballasttank = d_boot + vrijboord #meter, diepte korte ballasttank

l_kraanboom = (b_boot / 2 + 4.5) / np.cos(60)

pd_zijwanden = 0.02 #meter, plaatdikte zijwanden
pd_tankwanden = 0.01 #meter, plaatdikte tankwanden
pd_schot = 0.01 #meter, plaatdikte voor/achterschip

deplacement = l_boot * b_boot * d_boot * cb

'ZWAARTEPUNTEN'
ZPx_windmolendeel = l_kraanboom * np.cos(60) #zwaartpunt van het hangende windmolendeel op de x-as
ZPy_windmolendeel = l_boot / 2 - app #zwaartepunt van het hangende windmolendeel op de y-as
ZPx_kraanhuis = 0 #zwaartepunt van het kraanhuis op de x-as
ZPy_kraanhuis = l_boot/2 - app #zwaartepunt van het kraanhuis op de y-as
ZPx_kraanboom = l_kraanboom * np.cos(60) / 2 #zwaartepunt van de kraanboom op de x-as
ZPy_kraanboom = l_boot / 2 - app #zwaartepunt van de kraanboom op de y-as
ZPx_hijsgerei = ZPx_windmolendeel #zwaartepunt van het hijsgerei op de x-as
ZPy_hijsgerei = l_boot / 2 - app #zwaartepunt van het hijsgerei op de y-as
ZPx_kraan = ((m_kraanhuis * ZPx_kraanhuis) + (m_kraanboom * ZPx_kraanboom) + (m_hijsgerei * ZPx_hijsgerei) + (ZPx_windmolendeel * m_windmolendeel)) / m_kraan #zwaartepunt van de kraan op de x-as, inclusief windmolendeel
ZPy_kraan = l_boot / 2 - app #zwaartepunt van de kraan op de y-as
ZPx_boot = b_boot / 2 #zwaartpunt van de boot op de x-as
ZPy_boot = l_boot / 2 - app #zwaartepunt van de boot op de y-as

vcg_windmolendeel = d_boot + vrijboord + 10
vcg_kraanhuis = d_boot + vrijboord
vcg_kraanboom = d_boot + vrijboord + l_kraanboom * np.sin(60) / 2
vcg_hijsgerei = d_boot + vrijboord + l_kraanboom * np.sin(60)
vcg_kraan = ((m_kraanhuis * vcg_kraanhuis) + (m_kraanboom * vcg_kraanboom) + (m_hijsgerei * vcg_hijsgerei) + (vcg_windmolendeel * m_windmolendeel)) / m_kraan #zwaartepunt van de kraan op de x-as, inclusief windmolendeel


'VOLUMES'
v_romp = ...
v_tankschotten = ...
v_tank1 = (ll_ballasttank * bl_ballasttank * dl_ballasttank)
v_tank2 = (lk_ballasttank * bk_ballasttank * dk_ballasttank)
v_tank3 = (ll_ballasttank * bl_ballasttank * dl_ballasttank)

m_romp = v_romp * soortelijk_staalgewicht * f_verstijfers
m_tankschotten = v_tankschotten * soortelijk_staalgewicht * f_verstijfers
m_tank1 = (v_tank1 * soortelijk_zeewater * vg_tank1)
m_tank2 = (v_tank2 * soortelijk_zeewater * vg_tank2)
m_tank3 = (v_tank3 * soortelijk_zeewater * vg_tank3)

vcg_romp = ...
vcg_tankschotten = ...
vcg_tank1 = (vg_tank1 * dl_ballasttank) / 2
vcg_tank2 = (vg_tank2 * dk_ballasttank) / 2
vcg_tank3 = (vg_tank3 * dl_ballasttank) / 2
vcg_deklading = 10 + (vrijboord + d_boot)

vcg_tanktotaal = (vcg_tank1 * m_tank1 + vcg_tank2 * m_tank2 + vcg_tank3 * m_tank3) / (m_tank1 + m_tank2 + m_tank3)

KB = d_boot / 2
KG = (vcg_romp * m_romp + vcg_tankschotten * m_tankschotten + vcg_kraan * m_kraan + vcg_deklading * m_deklading + vcg_tanktotaal * (m_tank1 + m_tank2 + m_tank3)) / (m_romp + m_tankschotten + m_kraan + m_deklading + m_tank1 + m_tank2 + m_tank3)

It_tank1 = ((bl_ballasttank**3 * ll_ballasttank) / 12) * soortelijk_zeewater
It_tank2 = ((bk_ballasttank**3 * lk_ballasttank) / 12 ) * soortelijk_zeewater
It_tank3 = ((bl_ballasttank**3 * ll_ballasttank) / 12) * soortelijk_zeewater
It_totaal = It_tank1 + It_tank2 + It_tank3

It_boot = (b_boot**3 * l_boot) / 12

BM = It_boot / deplacement

VVC_tank3 = It_tank3 / (deplacement * soortelijk_zeewater)
VVC = (It_tank1 + It_tank2 + It_tank3) / (deplacement * soortelijk_zeewater)

GM = KB + BM - KG
G_M = GM - VVC

