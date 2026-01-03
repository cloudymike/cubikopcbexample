
postamble='''
M5      (Spindle off.)
G04 P1.000000
M9      (Coolant off.)
M2      (Program end.)
'''

for filetype in ["PTH","NPTH"]:
	inputfile='Drill_{0}_Through.nc'.format(filetype)
	with open(inputfile, 'r') as f:
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
		filename='Drill_{0}_{1}.nc'.format(filetype,Tcode)
		print('==========================',filename)
		with open(filename,'w') as of:
			for outline in bitsize['preamble']:
				print(outline,file=of)
			for outline in bitsize[Tcode]:
				print(outline,file=of)
			print(postamble,file=of)