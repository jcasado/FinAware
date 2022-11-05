# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 21:12:33 2022

@author: Janne Kalmari
"""

import pandas as pd
import numpy as np

data = pd.read_excel(r'c:\Users\Dronepilot\Hack\Finland-Field.xlsx', sheet_name='Finland-Field')

data = data[['Year', 'pt1', 'pt2', 'pt3', 'tot']]

data = data.drop(data[data.tot < 0].index)

years = [2017,2018,2019,2020,2021,2022]
taulut = []

for item in years :
    taulut.append(data[data.Year == item])

varianssit=[]
deltat=[]

for item in taulut :
    varianssit.append(item.var())
    deltat.append(item.std())

#numpyllä varianssien varianssi