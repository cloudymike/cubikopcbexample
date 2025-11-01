#!/bin/bash

unzip -o *.zip 
rm -f *.nc

pcb2gcode \
  --back Gerber_BottomLayer.GBL --back-output Gerber_BottomLayer.nc \
  --drill Drill_PTH_Through.DRL --drill-output Drill_PTH_Through.nc \
  --milldrill-output Drill_PTH_milldrill.nc \
  --outline Gerber_BoardOutlineLayer.GKO --outline-output Gerber_BoardOutlineLayer.nc

# Cleanup, may be too much 
rm -f *.svg
rm -f *.GT?
rm -f *.GDL
rm -f *.GBS

