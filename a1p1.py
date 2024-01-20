
# a1p1.py

# Emily Liang
# exliang@uci.edu
# 79453973

def main():
	user_input()

def user_input():
	command = input() #format: [COMMAND] [INPUT] [[-]OPTION] [INPUT]
	if command[0] == 'L': #list contents of directory 
		pass
	elif command[0] == 'Q':
		exit()
if __name__ == '__main__':
	main()