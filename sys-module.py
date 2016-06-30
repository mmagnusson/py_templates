#!/usr/bin/python

# using 'sys' module functions, python3 -> reading py3 docs for more
# example from http://www.primalsecurity.net/introduction-to-python-for-security-professionals/
# 

import sys

def takeTerminalArguments():
	script = sys.argv[0]
	ip = sys.argv[1]
	port = sys.argv[2]
	
	print("[+] Script name is: "+script)
	print("[+] The IP is: "+ip+" and the port is: "+port)
	
def main():
	takeTerminalArguments()
	
if __name__=="__main__":
	main()