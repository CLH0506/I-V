# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:21:42 2024

@author: daphn
"""
import numpy as np

#GEWICHTEN
m_windmolendeel = 230000 #kg
SWLmax = ((m_windmolendeel/94)*100) #kg

m_kraanhuis = (0.34*SWLmax) #kg
m_kraanboom = (0.17*SWLmax) #kg
m_hijsgerei = (0.06*SWLmax) #kg
m_kraan = (m_kraanboom + m_kraanhuis + m_hijsgerei + m_windmolendeel) #kg, inclusief windmolendeel
m_scheepslading = 4 * m_windmolendeel

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

diameter_windmolendeel = 8 #m

pd_zijwanden = 0.02 #meter, plaatdikte zijwanden
pd_tankwanden = 0.01 #meter, plaatdikte tankwanden
pd_schot = 0.01 #meter, plaatdikte voor/achterschip

#ZWAARTEPUNTEN
ZPx_windmolendeel = l_kraanboom * np.cos(60) #zwaartpunt van het hangende windmolendeel op de x-as
ZPy_windmolendeel = l_boot / 2 #zwaartepunt van het hangende windmolendeel op de y-as
ZPx_kraanhuis = 0 #zwaartepunt van het kraanhuis op de x-as
ZPy_kraanhuis = l_boot/2 #zwaartepunt van het kraanhuis op de y-as
ZPx_kraanboom = l_kraanboom * np.cos(60) / 2 #zwaartepunt van de kraanboom op de x-as
ZPy_kraanboom = l_boot / 2 #zwaartepunt van de kraanboom op de y-as
ZPx_hijsgerei = ZPx_windmolendeel #zwaartepunt van het hijsgerei op de x-as
ZPy_hijsgerei = l_boot / 2 #zwaartepunt van het hijsgerei op de y-as
ZPx_kraan = ((m_kraanhuis * ZPx_kraanhuis) + (m_kraanboom * ZPx_kraanboom) + (m_hijsgerei * ZPx_hijsgerei) + (ZPx_windmolendeel * m_windmolendeel)) / m_kraan #zwaartepunt van de kraan op de x-as, inclusief windmolendeel
ZPy_kraan = l_boot / 2 #zwaartepunt van de kraan op de y-as
ZPx_boot = 10 #zwaartpunt van de boot op de x-as
ZPy_boot = 35 #zwaartepunt van de boot op de y-as

#OVERIGE GEGEVENS
soortelijk_staalgewicht = 7850 #kg/m3
soortelijk_zeewater = 1025 #kg/m3
f_verstijfers = 2.1 #factor 2.1 keer het totale gewicht
gv = 9.81 #m/s, gravitatieversnelling
app = 4.2 #meter
vg_tank3 = 0.72 #vullingsgraad tank 3
