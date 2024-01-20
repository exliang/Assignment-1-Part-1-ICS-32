
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

	if command == 'L': #list contents of directory 
		if len(command_list) == 2: #[COMMAND] [INPUT]
			if any(myPath.iterdir()): #check if directory isnt empty
				for currentPath in myPath.iterdir(): #list contents of the directory 
					print(currentPath) #FIXME: ensure your code properly sorts results into files first, followed by directories
		elif len(command_list) == 3: #[COMMAND] [INPUT] [[-]OPTION]
			option = command_list[2]
			#add more
		elif len(command_list) == 4:
			last_input = command_list[3] 

	elif command == 'Q':
		exit()

if __name__ == '__main__':
	main()