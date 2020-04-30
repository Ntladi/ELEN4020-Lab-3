import os
import sys

if (os.path.isdir("Environment")):
	os.system("rm -rf Environment")
os.system("virtualenv -p /usr/bin/python3.6 Environment")
