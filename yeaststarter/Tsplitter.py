
postamble='''
M5      (Spindle off.)
G04 P1.000000
M9      (Coolant off.)
M2      (Program end.)
'''

with open('Drill_PTH_Through.nc', 'r') as f:
	#gcode = [line.rstrip('\n') for line in f]
	gcode = f.readlines()

bitsize={}
Tcode='preamble'
bitsize[Tcode]=[]
Tlist=[]
for line in gcode:
	#print(line)
	if line[0] == 'T':
		Tcode=line.rstrip('\n')
		bitsize[Tcode]=[]
		Tlist.append(Tcode)
	else:
		bitsize[Tcode].append(line.rstrip('\n'))

for Tcode in Tlist:
	filename='Drill_PTH_{0}.nc'.format(Tcode)
	print('==========================',filename)
	for outline in bitsize['preamble']:
		print(outline)
	for outline in bitsize[Tcode]:
		print(outline)
	print(postamble)