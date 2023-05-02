#Imports Section
import os
from random import choice

#First we make the lists
numA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numB = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numC = [2, 4]

#next define the Test FUNCTION
def test(type):
	Q = 0
	right = 0
	notright = 0
	while Q < Q_amount:
		A = choice(numA)
		B = choice(numB)
		#Change the question type based on the type of test
		if "add" in type:
			answer = A + B
			sign = "+"
		if "sub" in type:
			answer = A - B
			sign = "-"
		if "mult" in type:
			answer = A * B
			sign = "*"
		if "div" in type:
			B = choice(numC)
			answer = A / B
			sign = "/"
		Q += 1

		try:
			if "div" in type:
				useranswer = float(input(f'\nWhat is {A}{sign}{B}? '))
			else:
				useranswer = int(input(f'\nWhat is {A}{sign}{B}? '))
		except ValueError:
			useranswer = answer + 1
		if useranswer == answer:
			print('CORRECT nice work!')
			right = right + 1
		else:
			print(f'Incorrect the correct answer was: {answer}')
			notright = notright + 1

#Grading
	else:
		print(
		 f'---You got {right} question(s) right and\nYou got {notright} question(s) wrong---'
		)
		score = (right / Q) * 100
		print('---' + str(score) + '%---')
		if score > 89:
			print('--AMAZING--')
		elif score > 79:
			print('--GREAT--')
		elif score > 69:
			print('--COOL--')
		elif score > 59:
			print('--EH--')
		else:
			print('--OOF--')
trynum = int(1)
while trynum > 0:
	#next we make a choice
	Mathtype = int(
	 input('What type of test would you like?\n1.Addtion\n2.Subtraction\n3.Multiplication\n4.Division\nType the number here: '))
	Q_amount = int(input('\nHow many questions: '))
	if Mathtype == 1:
		test("add")
		trynum -= 1
	elif Mathtype == 2:
		test("sub")
		trynum -= 1
	elif Mathtype == 3:
		test("mult")
		trynum -= 1
	elif Mathtype == 4:
		test("div")
		trynum -= 1
	#Allow infinite reattempts without restarting code
	try2 = int(input('Press 1 to try again\n(press 0 to stop) '))
	if try2 == 1:
		trynum = try2
		os.system('clear')
else:
	print("END")
