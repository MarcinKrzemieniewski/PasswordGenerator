# Note that this program is possibly not the most secure for generating passwords. 
# Though I've made it as secure my knowlege allows.
from secrets import randbelow 
import string

def get_char(x):
	which_char = randbelow(len(x))
	y = x[which_char]
	return y

def generator(length):
	numbers = string.digits
	letters = string.ascii_letters
	special = string.punctuation
	passwd = ""
	for i in range(length):
		which_char = randbelow(4)
		if which_char == 1:
			char = get_char(numbers)
		elif which_char == 2:
			char = get_char(letters)
		else:
			char = get_char(special)
		passwd += char
	return passwd

if __name__ == '__main__':
	integer = False
	while integer == False:
		length = input('How long would you like your password to be? Type 0 to exit the program: ')
		if str(length) == '0':
			raise SystemExit(0)
		try:
			length = int(length)
			print(f'\n{generator(length)}\n')
			integer = True
		except:
			print('Input must be an integer.')
	print('Please keep your passwords somewhere safe and not on your device.')