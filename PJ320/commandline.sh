#!/bin/bash

# If there is a (new) zip file, unzip it and use it
if [  -f *.zip ] 
then 
  echo "Unzipping new Gerber file"
  unzip -o *.zip 
fi
rm -f *.nc

pcb2gcode \
  --back Gerber_BottomLayer.GBL --back-output Gerber_BottomLayer.nc \
  --drill Drill_PTH_Through.DRL --drill-output Drill_PTH_Through.nc \
  --milldrill-output Drill_PTH_milldrill.nc \
  --outline Gerber_BoardOutlineLayer.GKO --outline-output Gerber_BoardOutlineLayer.nc

# If there are a file for mount holes, use it.
if [ -f Drill_NPTH_Through.DRL ]
then
pcb2gcode \
  --drill Drill_NPTH_Through.DRL --drill-output Drill_NPTH_Through.nc \
  --outline Gerber_BoardOutlineLayer.GKO --outline-output Gerber_BoardOutlineLayer.nc
fi

# Cleanup, may be too much 
rm -f *.svg
rm -f *.GT?
rm -f *.GDL
rm -f *.GBS
rm -f How-to-order-PCB.txt
rm -f Drill_PTH_Through_Via.DRL

