# cubikopcbexample
Example of creating PCBs with Cubico, including an example of ESP32C3 temperature controller (from  cloudymike/fermctrl repo)

## Current best practice

### Steps, Overview

1. Prep GERBER file (routing parameter)  
2. Translate GERBER to NC (CNC go code) file  
3. Run CNC  
4. Postprocessing and soldering

### CNC steps

* Create files with script  
  * Calibrate hightmap, check outline of board so it is OK  
* ENgrave copper  
  * cleanup/vacuum  
* Engrave outline  
  * Missed one side ?? Maybe hightmap is no good?  
  * Vacuum  
* Drill holes.   
  * New hightmap with 2x2 measuring points  
    * Go to XY0.0 (macro) IMPORTANT  
    * Move Z \< 5mm  
    * Check that 0.0 is not on board cutout  
  * Load drill file  
    * It will stop for tool change. Ignore an click run again (we are just using one drill bit, 0.9mm)  
  * Vacuum, clean  
* Cut out board  
  * Switch to 1.8mm  
    * Tight fit with one of the wires, would have gone for 2mm otherwise	  
  * New hightmap  
    * Go to XY0.0  
    * Move Z \< 5mm  
    * Run heightmap again with 2x2 points  
  * Load boardoutlinelayer file  
  * Run  
  * Clean/Vacuum (some more cruft here)  
  * Deburr (used a scotchpad, OK, probably need fine sandpaper  
  * Remove board (and vacuum again..)  
  * Removed cart by twisting and then trimmed with wire cutter  
    * There is probably a better way to do this

### Software

#### Design/CAD **EasyEDA**

EasyEDA is working OK, and should probably stay with this.

Kicad seems to be popular, and may be worth trying, as it is opensource.   
Fritzing I have access to, and should be usable but it seems layout software is less strong.

#### CAM / Gcode generator **pcb2gcode**

Pcb2gcode seems to work fine. I do like the text oriented approach with a project file that defines the parameters.

Flatcam seems very popular as an alternative but had problems getting it working with right PyQT version.

#### Controller / link software UGS

UGS, Universal Gcode Sender seems to work fine and I was able to recompile it for Ubuntu so should be safe.

### CNC bits

##### Copper trace / engraving

A 20 degree V shaped engraving bit work, Genmitsu [70V20](https://www.sainsmart.com/products/sainsmart-genmitsu-nano-blue-coat-engraving-bits-20-degree-0-1mm?_pos=6&_fid=f912f189b&_ss=c). It seems like a slightly used bit is creating less burrs than a completely new one. Go figure.

#### Holes, drilling

Holes can be either just drilled or drillmilled. When I tried drillmilling with a 1mm drillbit, it broke the bit. I suggest that I stay with pure drilling. For this use PCB rated drill bits, Genmitsu [PD20A](https://www.sainsmart.com/products/genmitsu-30pcs-pcb-drill-bits-set-0-1mm-3-0mm-1-8-shank-pd30a?_pos=1&_sid=303f55c0b&_ss=r)

#### Holes milldrilling

For now, avoid this as it broke bits.

##### Board cutout

Using endmill bits, from Genmitsu [C08](https://www.sainsmart.com/products/sainsmart-genmitsu-nano-blue-coat-cnc-router-bits?variant=21761554972751)   (Ordered on [Amazon](https://www.amazon.com/dp/B07P7LGQJ6?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1))  
Suggestions goes from 1.5mm to 3mm, will probably try 2mm

### Settings for pcb2gcode

##### Drilling instead of milldrill

Set the min mildrill size larger than any hole in millproject file  
min-milldrill-hole-diameter= 4.0mm  
There are a set of available drills listed in millproject file, check that they match the sizes of holes in the drill file  
	drills-available=0.3mm,0.4mm,0.5mm,0.6mm,0.7mm,0.8mm,0.9mm, 1.101, 2.8, 3.201  
Check that the drillmill output file is empty when you have exported the drill file. There will probably be multiple holds in the drill file for drill bit changes. If we are good without change, just hit Run again when it is on Hold.

## Notes and links

### Repo for pcb2code

The repo seems active, last committed 2 months ago, with 31 contributors.

Here is the top level https://github.com/pcb2gcode  
Only using command line for now https://github.com/pcb2gcode/pcb2gcode

### Tutorial using pcb2code 

[Making PCBs at home: Milling the first layer (and why you need it)](https://whynot.fail/factory/making-pcbs-at-home-milling-the-first-layer/)  
Includes and example millproject file and a program to calculate depth of traces, `pcb_mill_calc.py`

### Compile pcb2code from scratch

\* https://github.com/pcb2gcode/pcb2gcode?tab=readme-ov-file  
\* liberbv hanging hack : https://github.com/pcb2gcode/pcb2gcode/issues/626

### Cubiko facebook

https://www.facebook.com/groups/584041651229213

### CNC\_PCB\_TOOLS, Python scripts for checking gcode files

https://github.com/mattwach/cnc\_pcb\_tools

### Detailed tutorial, but using FlatCAM 

Detailed tutorial: https://www.facebook.com/groups/584041651229213



## Directory structure
Inital structure includes all files including command script and millproject. 
This is not tenable but for initial projects, before I figure out what
is a good standard setup, this will do.

