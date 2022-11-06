# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 21:12:33 2022

@author: Janne Kalmari
"""

import pandas as pd
from scipy import stats
import numpy as np

years = np.array([2017,2018,2019,2020,2021,2022]) # Years available in the specimen file


def get_data(): # get the datafile and crop it. The filename is hardcoded into call for now.
    df = pd.read_excel(r'c:\Users\Dronepilot\Hack\Finland-Field.xlsx', sheet_name='Finland-Field')
#    df = df[['Year', 'pt1', 'pt2', 'pt3', 'tot']] #Testing...
    df = df[['Year', 'tot']]
    df = df.drop(df[df.tot < 0].index)
    return df

def cut_year(year): # cut the table into yearly tables with the specified end year
    tables = []
    vuodet = years[years == year]
#    vuodet = years[years <= year] # Sliding end year
    for item in vuodet :
        tables.append(data[data.Year == item][['tot']])        
    return tables

def normal(frames): # Calculate the yearly normal distributions (mean, stddev)
    normald=[]
    for item in frames:
        normald.append(item.mean())
        normald.append(item.std())
    return normald

def ttest(normald): # Perform t-tests for the yearly standard deviations and calculate a matrix (list) of p values on the differences.
    ttests=[]
    i,j = 0,0    
    while i < (len(normald)/2):
        j = i+1
        while j < (len(normald)/2):
         ttests.append(stats.ttest_ind_from_stats(normald[i], normald[i+1], 158, normald[j], normald[j+1], 158))
         j+=1
        i+=1
    if not ttests : # In case we are only looking at one year...
        ttests = normald
    return ttests

def ND(ttests): # Calculate the mean and standard distribution of the p values
    pvalues=[]
    for item in ttests :
        pvalues.append(item.pvalue[0])
    pseries=pd.Series(pvalues)
    return [pseries.mean(), pseries.std()] # Calculate and return the stddev and mean of the p values


tulos_mean = []
tulos_std = []

for item in years:
    data = get_data()
    taulut = cut_year(item)
    jakaumat = normal(taulut)
    parvot = ttest(jakaumat)
    tulos_mean.append(parvot[0])
    tulos_std.append(parvot[1])

'''
drought_likelihood = stats.norm(tulos_mean,tulos_std).cdf(0) # array of likelihoods of SWI of 0
swi_50 = stats.norm(tulos_mean,tulos_std).cdf(50) # array of likelihoods of SWI of 0
swi_100 = stats.norm(tulos_mean,tulos_std).cdf(100) # array of likelihoods of SWI of 0
swi_150 = stats.norm(tulos_mean,tulos_std).cdf(150) # array of likelihoods of SWI of 0

def score_count(nro) :
    score = stats.norm(tulos_mean,tulos_std).cdf(nro)
    return score.max()-score.min()
   
values = [] 
for item in np.arange(0,250):
    values.append(score_count(item))

values = np.array(values)
np.where(values == values.max()) # is 192
'''
swi_192 = stats.norm(tulos_mean,tulos_std).cdf(192) # array of likelihoods of SWI of 192 (maximum difference)
'''
array of results from above
[0.59976024],
[0.77135223],
[0.58700296],
[0.62491021],
[0.52958706],
[0.42805583]
# Use them to calculate the likelihood of the next year being difficult
# Translate to score 
'''

