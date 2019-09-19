#!/usr/bin/env python3

file_name = input("Enter a filename: ")

my_file=open(file_name,'a')

#print(f"File {file_name} was created")

print("Enter content of the file: ")
content = 'something'
while content != '':
	content = input()
	my_file.write(content)
	my_file.write('\n')
	
my_file.close()
