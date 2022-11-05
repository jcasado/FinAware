#!/bin/bash

DATAPOOL="https://land.copernicus.vgt.vito.be/PDF/datapool/Vegetation/Soil_Water_Index/Daily_SWI_1km_Europe_V1/2015/"

# Edit this part for your own username and password
USER="juliacasado"
PASS="SXqt5ceaH3FA"

# ?coord=4.4675,21.1128,25.7966,32.0656
wget -r --user=${USER} --password=${PASS} ${DATAPOOL}