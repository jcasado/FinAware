#!/bin/bash

DATAPOOL="https://land.copernicus.vgt.vito.be/PDF/datapool/Vegetation/Soil_Water_Index/Daily_SWI_1km_Europe_V1/2015/"

# Edit this part for your own username and password
USER="juliacasado"
PASS="SXqt5ceaH3FA"

# ?coord=21.8264,60.6651,24.0964,63.1347


wget -r --user=${USER} --password=${PASS} ${DATAPOOL}?coord=21.8264,60.6651,24.0964,63.1347