done = False


def isFinished():
	while True:
		userIn = raw_input("\nDo you want to continue? (y/n): ")
		if userIn.lower() == "n":
			return True
		elif userIn.lower() == "y":
			return False
		else:
			print '\nInvalid input, please use \'y\' or \'n\''

def printList(list):
	
	sentence = ""

	for s in list:
		sentence += s + " "

	print sentence



while done == False:
	meh = raw_input("\nEnter the thing bro: ")

	mehList = []
	i = 0

	for balls in meh.split():
		b = balls[0]
		balls2 = ""

		if balls[0] in ['a', 'e', 'i', 'o', 'u']:
			balls2 = balls.lower() + "ay"
		else:
			i = 1
			while i < len(balls) :
				balls2 = balls2 + balls[i]
				i = i + 1

			balls2 += balls[0].lower() + "ay"
		mehList.insert(i, balls2)
		i += 1	

	printList(mehList)	

	done = isFinished()
