
import os
import shutil

root_path = os.getcwd()
dirs = ["/aww", "/oldschoolcool", "/pics", "/dankmemes", "/astrophotography", "/NatureIsFuckingLit"]

def rename(filename, dir):
	input = "{}/{}".format(root_path+dir, filename)
	output = "{}{}_{}".format(root_path+"/unclustered", dir, filename)
	# print(input)
	# print(output)
	shutil.copy(input, output)
	

for dir in dirs:
	for file in os.listdir(root_path+dir):
		if file.endswith('.jpg'):
			print(file)
			rename(file, dir)
