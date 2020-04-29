import os
import sys

if (not os.path.isdir("../Word_Count_env")):
	print("Creating Virtual Environment")
	os.system("virtualenv -p /usr/bin/python3.6 ../Word_Count_env")