
# a1p1.py

# Emily Liang
# exliang@uci.edu
# 79453973

from pathlib import Path

def main():
	user_input()

def user_input():
	user_command = input() #format: [COMMAND] [INPUT] [[-]OPTION] [INPUT]
	command_list = user_command.split()

	command = command_list[0]
	path = command_list[1]
	myPath = Path(path)

	if myPath.exists(): #ensure that directory exists 
		if command == 'L': #list contents of directory 
			if len(command_list) == 2: #[COMMAND] [INPUT]
				list_directories(myPath)
			elif len(command_list) == 3: #[COMMAND] [INPUT] [[-]OPTION]
				option = command_list[2]
				if option == '-r':
					recursive_output()
				elif option == '-f': #output files only
					list_files(myPath)
			elif len(command_list) == 4: #[COMMAND] [INPUT] [[-]OPTION] [INPUT]
				option = command_list[2]
				if option == '-s': #output files that match the file name
					file_name = command_list[3] 
					if not file_name.exists(): #handling exception for if a file name doesn't exist 
						idk = input("File does not exist")
					matching_files(myPath, file_name)
				elif option == '-e':
					file_extension = command_list[3]
					matching_extension(myPath, file_extension)

		elif command == 'Q':
			exit()
	else:
		print("Directory doesn't exist. Try again.")

def list_directories(myPath):
	if any(myPath.iterdir()): #check if directory isnt empty
		dir_list = []
		file_list = []
		for currentPath in myPath.iterdir(): #list contents of the directory 
			if currentPath.is_file(): #if it's a file, put it in the file list
				file_list.append(currentPath)
			elif currentPath.is_dir(): #if it's a directory, put it in the directory list 
				dir_list.append(currentPath)
		file_list.extend(dir_list) #sorting results into files first, followed by directories
		combined_list = file_list
		for directory in combined_list:
			print(directory)

def list_files(myPath):
	if any(myPath.iterdir()): #check if directory isnt empty
		for currentPath in myPath.iterdir(): #list contents of the directory 
			if currentPath.is_file():
				print(currentPath)

def matching_files(myPath, file_name): 
	for currentPath in myPath.iterdir(): #list contents of the directory 
		if currentPath.is_file() and currentPath.name == file_name: #matching file name & must be a file
			print(currentPath)

def matching_extension(myPath, file_extension):
	for currentPath in myPath.iterdir(): #list contents of the directory 
		if currentPath.name.endswith(file_extension): #check if the file type is the same as what the user entered 
			print(currentPath)

def recursive_output():
	pass

if __name__ == '__main__':
	main()

# Citations:
# - https://docs.python.org/3/library/pathlib.html