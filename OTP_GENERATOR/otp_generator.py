import string
import random


## characters to generate OTP from
characters = list(string.digits)

def generate_random_OTP():
	## length of OTP from the user
	length = int(input("Enter otp length: "))

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant OTP
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))



## invoking the function
generate_random_OTP()
