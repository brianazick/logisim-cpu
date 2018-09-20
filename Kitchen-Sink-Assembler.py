# SKELETON ASSEMBLER WRITTEN BY JOHN RIEFFEL
# MODIFIED AND IMPROVED BY BRIAN ZICK

import sys

from helperfunctions import *

opcodeDict = {'add':'00001', 'sub':'00010', 'and':'0001', 'or':'00100',
			  'addi':'10000', 'subi':'10001', 'and':'10010', 'ori':'10011',
			  'lw':'10100', 'sw':'10101', 'j':'10110', 'beq':'10111',
			  'slt':'00101', 'sgt':'00110'}

def ConvertAssemblyToMachineCode(inline):
	'''given a string corresponding to a line of assembly,
	strip out all the comments, parse it, and convert it into
	a string of binary values'''

	outstring = ''

	if inline.find('#') != -1:
		inline = inline[0:inline.find('#')] #get rid of anything after a comment
	if inline.strip() != '':
		words = inline.split() #assuming syntax words are separated by space, not comma
		operation = words[0]
		operands = words[1:]
		outstring += opcodeDict[operation]
		if outstring[0] == '1': #i-type instructions
			if outstring == '10110': #jump instruction
				offset = int(operands[0])+1
				j_dest = int2bs(offset,12)
				outstring += j_dest
			elif outstring == '10111': #beq instruction
				outstring += int2bs(operands[2],4)
				outstring += int2bs(operands[0][1:],4)
				outstring += int2bs(operands[1][1:],4)
			else:
				for oprand in operands:
					if oprand[0] == '$':
						outstring += int2bs(oprand[1:],4)
					elif oprand[-1] == ')':
						outstring += int2bs(oprand[-2],4)
						if oprand[0] == '-':
							outstring += int2bs(oprand[0:2],4)
						else:
							outstring += int2bs(oprand[0],4)
					else:
						outstring += int2bs(oprand,4)
		elif outstring[0] == '0': #r-type instructions
			print outstring
			for oprand in operands:
					if oprand[0] == '$':
						outstring += int2bs(oprand[1:],4)
					print outstring
	print outstring
	return outstring


def AssemblyToHex(infilename,outfilename):
	'''given an ascii assembly file , read it in line by line and convert each line of assembly to machine code
	then save that machinecode to an outputfile'''
	outlines = []
	with open(infilename) as f:
		lines = [line.rstrip() for line in f.readlines()]  #get rid of \n whitespace at end of line
		#if you are a python ninja, use list comprehension. and replace the for loop below
		# with this expression
		#outlines = [ConvertAssemblyToMachineCode(curline) for curline in lines]
		# but, no judgement if you prefer explicit for loops
		for curline in lines:
			outstring = ConvertAssemblyToMachineCode(curline)
			if outstring != '':
				outstring = bs2hex(outstring)
				outlines.append(outstring)
	f.close()

	with open(outfilename,'w') as of:
		of.write("v2.0 raw")
		of.write("\n")
		of.write("00000")
		of.write("\n")
		for outline in outlines:
			of.write(outline)
			of.write("\n")
	of.close()


if __name__ == "__main__":
	#in order to run this with command-line arguments
	# we need this if __name__ clause
	# and then we need to read in the subsequent arguments in a list.

	#### These two lines show you how to iterate through arguments ###
	#### You can remove them when writing your own assembler
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)

	## This is error checking to make sure the correct number of arguments were used
	## you'll have to change this if your assembler takes more or fewer args
	if (len(sys.argv) != 3):
		print('usage: python skeleton-assembler.py inputfile.asm outputfile.hex')
		exit(0)
	inputfile = sys.argv[1]
	outputfile = sys.argv[2]
	AssemblyToHex(inputfile,outputfile)
