# -*- coding: utf-8 -*
import os

rootPath = os.getcwd()
# os.chdir(rootPath)

# fils = os.listdir(rootPath)
for x,y,z in os.walk(rootPath):
	print(x,y,z)
	pass