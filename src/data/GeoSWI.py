# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:23:56 2022

@author: Janne Kalmari
"""

import netCDF4
#import numpy as np
from pandas import DataFrame as df
#from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

FILENAME ='test.nc'
#PATH='c:/users/Dronepilot/Hack/Programmid/'

infile = FILENAME
satfile=netCDF4.Dataset(infile)

fields=[]
pellot = [[(8.659,52.19), (8.659,52.210), (8.667,52.210), (8.667,52.19)] , [(8.60,52.21), (8.60,52.23), (8.62,52.23), (8.62,52.21)], [(8.51,52.26), (8.51,52.28), (8.53,52.28), (8.53,52.26)], [(8.66,52.20), (8.66,52.215), (8.68,52.215), (8.68,52.20)], [(8.611,52.19), (8.611,52.225), (8.62,52.225), (8.62,52.19)]]

swidata=[]
swi=['SWI_002', 'SWI_005', 'SWI_010', 'SWI_015', 'SWI_020', 'SWI_040', 'SWI_060', 'SWI_100'] # Why these?


def polygonize(lista): # Use lista to create the used polygons, where lista is an array of arrays of cornerpoint coordinates
    for item in lista:
        fields.append(Polygon(item))
        
def swiff(lista): # Use lista (list of column names in satfile) to generate the list of satellite measured moisture values from netCDF file
    for item in lista:
        swidata.append(satfile.variables[item][:].filled(fill_value=-0.01)[0,:,:]) # Why -0.01?
        # pitäisikö käyttää nollaa ja tehdä DataFrame, josta poistaa turhat nollat?

def gather(): # Gather info into a table (pandas dataframe)
#Longitude, Latitude, 8 SWI values, field number?
    fieldnr = 0
    column_names = []   # Not pretty...
    column_names.append(['Lon', 'lat'])
    column_names.append(swi)
    column_names.append('Field')
    frame = df({}, columns = column_names)
    for item in pellot: # Singular field
        fieldnr += 1
        for ite in item: # Single coordinate points inside the field
            counter = 0
            newrow = []
            ii = ite[0]
            jj = ite[1]
            newrow.append(lon[ii])
            newrow.append(lat[jj])
            for it in swi: # get SWI pointdata for each swivalue from swidata
                newrow.append(swidata[counter][ii,jj])
                counter += 1
                
            frame = frame.append(newrow) # add to DataFrame
            
    return frame
                
                


lon=satfile.variables['lon'][:]
lat=satfile.variables['lat'][:]

nrows=lat.shape[0]
ncols=lon.shape[0]




    