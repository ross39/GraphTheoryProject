import shuntingYard;

determineToContinue = None
print("Welcome to regex matcher")
print("Created by Ross Heaney G00345608")
print("======================")


while determineToContinue != 'exit':
	#take user regex in and search
	print("Enter regex expression")
	regex = input()
	postfix = ""
	#set postfix equal to return type of post.parse function
	postfix = shuntingYard.parse(regex)
	print(postfix)
	print("Press exit to exit or enter to continue")
	determineToContinue = input()
    

