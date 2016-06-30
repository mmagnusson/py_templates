#!/usr/bin/python

#difference between os.system and subprocess.Popen is that subprocess allows redirection of STDOUT to a python variable

import subprocess

def subprocessFunction():
	com_str = 'uname -a'
	command = subprocess.Popen([com_str], stdout=subprocess.PIPE, shell=True)
	(output, error) = command.communicate()
	print(output)
	
def main():
	subprocessFunction()

if __name__=="__main__":
	main()