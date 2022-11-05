# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:55:16 2022

@author: Janne Kalmari
"""

import netCDF4


FILENAME = 'test.nc'
satfile = netCDF4.Dataset(FILENAME)

swidata = satfile.variables['SWI_015'][:].filled(fill_value=-0.01)[0,:,:] # Why -0.01?

lon=satfile.variables['lon'][:]
lat=satfile.variables['lat'][:]

# Kokemäki area coordinates
# 22.3, 61.23 ,22.43, 61.33 
'''
Only needed once
minlon = next(x[0] for x in enumerate(lon) if x[1] > 22.3)
maxlon = next(x[0] for x in enumerate(lon) if x[1] > 22.43)
minlat = next(x[0] for x in enumerate(lat) if x[1] < 61.33)
maxlat = next(x[0] for x in enumerate(lat) if x[1] < 61.23)
'''
arealon = [3730, 3744]
arealat = [1195, 1206]
